#include "mru.h"

#include <algorithm>
#include <cassert>

mru::mru(CACHE* cache)
  : replacement(cache),
    NUM_SET(cache->NUM_SET),
    NUM_WAY(cache->NUM_WAY),
    last_used_cycles(static_cast<std::size_t>(NUM_SET * NUM_WAY), 0),
    cycle(0)
{}

unsigned& mru::get_last_used(long set, long way) {
  return last_used_cycles.at(static_cast<std::size_t>(set * NUM_WAY + way));
}

long mru::find_victim(uint32_t, uint64_t, long set, const champsim::cache_block*, champsim::address,
                      champsim::address, access_type)
{
  auto begin = std::next(last_used_cycles.begin(), set * NUM_WAY);
  auto end = std::next(begin, NUM_WAY);

  auto victim = std::max_element(begin, end); // MRU = элемент с максимальным временем последнего доступа
  assert(begin <= victim && victim < end);
  return std::distance(begin, victim);
}

void mru::replacement_cache_fill(uint32_t, long set, long way, champsim::address,
                                 champsim::address, champsim::address, access_type)
{
  get_last_used(set, way) = cycle++;
}

void mru::update_replacement_state(uint32_t, long set, long way, champsim::address,
                                   champsim::address, champsim::address, access_type type, uint8_t hit)
{
  if (hit && type != access_type::WRITE) {
    get_last_used(set, way) = cycle++;
  }
}
