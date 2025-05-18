#include "mru.h"

#include <algorithm>
#include <cassert>

mru::mru(CACHE* cache)
  : replacement(cache),
    NUM_SET(cache->NUM_SET),
    NUM_WAY(cache->NUM_WAY),
    access_order(static_cast<std::size_t>(NUM_SET * NUM_WAY), 0)
{}

unsigned& mru::get_order(long set, long way) {
  return access_order.at(static_cast<std::size_t>(set * NUM_WAY + way));
}

long mru::find_victim(uint32_t, uint64_t, long set, const champsim::cache_block*, champsim::address,
                      champsim::address, access_type)
{
  auto begin = std::next(access_order.begin(), set * NUM_WAY);
  auto end = std::next(begin, NUM_WAY);

  auto victim = std::max_element(begin, end);

  assert(begin <= victim && victim < end);
  return std::distance(begin, victim);
}

void mru::update_replacement_state(uint32_t, long set, long way, champsim::address,
                                   champsim::address, champsim::address, access_type, uint8_t)
{
  get_order(set, way) = ++current_timestamp;
}
