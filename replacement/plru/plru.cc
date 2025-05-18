#include "plru.h"

#include <algorithm>
#include <cassert>

plru::plru(CACHE* cache)
    : plru(cache, cache->NUM_SET, cache->NUM_WAY) {}

plru::plru(CACHE* cache, long sets, long ways)
    : replacement(cache), NUM_WAY(ways), ways_trees(sets, pseudo_lru_ways_tree(ways)) {}

long plru::find_victim(uint32_t cpu, uint64_t instr_id, long set,
                             const champsim::cache_block* current_set,
                             champsim::address ip, champsim::address full_addr,
                             access_type type)
{
  return ways_trees.at(static_cast<std::size_t>(set)).victim();
}

void plru::replacement_cache_fill(uint32_t cpu, long set, long way,
                                        champsim::address full_addr, champsim::address ip,
                                        champsim::address victim_addr, access_type type)
{
  ways_trees.at(static_cast<std::size_t>(set)).update(way);
}

void plru::update_replacement_state(uint32_t cpu, long set, long way,
                                          champsim::address full_addr, champsim::address ip,
                                          champsim::address victim_addr,
                                          access_type type, uint8_t hit)
{
  if (hit && type != access_type::WRITE) {
    // Skip update for writeback hits
    ways_trees.at(static_cast<std::size_t>(set)).update(way);
  }
}

pseudo_lru_ways_tree::pseudo_lru_ways_tree(long ways)
{
  std::size_t level_nodes = 1;
  while (ways > 1) {
    levels.emplace_back(level_nodes, pointer_direction::LEFT);
    ways /= 2;
    level_nodes *= 2;
  }
}

long pseudo_lru_ways_tree::victim()
{
  long index = 0;
  for (const auto& level : levels) {
    if (level.at(index) == pointer_direction::LEFT)
      index = 2 * index;
    else
      index = 2 * index + 1;
  }
  return index;
}

void pseudo_lru_ways_tree::update(long way)
{
  long index = way / 2;
  for (auto it = levels.rbegin(); it != levels.rend(); ++it) {
    auto& level = *it;
    auto& node = level.at(index);
    node = (node == pointer_direction::LEFT) ? pointer_direction::RIGHT : pointer_direction::LEFT;
    index /= 2;
  }
}
