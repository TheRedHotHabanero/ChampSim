#pragma once

#include <vector>
#include "cache.h"
#include "modules.h"

class mru : public replacement
{
public:
  mru(CACHE* cache);
  
  long find_victim(uint32_t, uint64_t, long set, const champsim::cache_block*,
                   champsim::address, champsim::address, access_type) override;

  void replacement_cache_fill(uint32_t, long set, long way, champsim::address,
                              champsim::address, champsim::address, access_type) override;

  void update_replacement_state(uint32_t, long set, long way, champsim::address,
                                champsim::address, champsim::address, access_type, uint8_t) override;

private:
  const long NUM_SET;
  const long NUM_WAY;
  std::vector<unsigned> last_used_cycles;
  unsigned cycle = 0;

  unsigned& get_last_used(long set, long way);
};
