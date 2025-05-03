#ifndef BRANCH_MARKOV_MODEL_1_H
#define BRANCH_MARKOV_MODEL_1_H

#include <array>

#include "address.h"
#include "modules.h"
#include "msl/fwcounter.h"

// REalization based on bimodal.h
class markov_model_1 : champsim::modules::branch_predictor
{
	[[nodiscard]] static constexpr auto hash(champsim::address ip) { return ip.to<unsigned long>() % PRIME; }

  	static constexpr std::size_t TABLE_SIZE = 16384;
  	static constexpr std::size_t PRIME = 16381;
  	// static constexpr std::size_t BITS = 2;

  	// task: instead of bit counter in bimodal predictor
  	struct FREQ {
  	  std::size_t TAKEN = 0; // BITS has std::size_t type, so it be again std::size_t type for freq
  	  std::size_t NTAKEN = 0;
  	};

  	std::array<FREQ, TABLE_SIZE> frequency_table;

public:
  	using branch_predictor::branch_predictor;
	
  	// void initialize_branch_predictor();
  	bool predict_branch(champsim::address ip);
  	void last_branch_result(champsim::address ip, champsim::address branch_target, bool taken, uint8_t branch_type);
};

#endif
