#include <random>
#include "markov_model_2.h"

// the eonly place to change
bool markov_model_2::predict_branch(champsim::address ip)
{
    auto value = frequency_table[hash(ip)];

    // instead of value with max freq we take the prediction based on probability
    // (freq1 / (freq1 + freq2))
    std::size_t taken = value.TAKEN;
    std::size_t not_taken = value.NTAKEN;
    std::size_t total = taken + not_taken;


    if (total == 0) { // in fact is unreachable
        return true;
    }

    // Generating random numbers
    static std::random_device rd;
    static std::mt19937 gen(rd());
    std::uniform_real_distribution<> dist(0.0, 1.0);

    // (freq1 / (freq1 + freq2))
    double p = static_cast<double>(taken) / static_cast<double>(total);
    return dist(gen) < p;
}

// the same as for model 1
void markov_model_2::last_branch_result(champsim::address ip, champsim::address branch_target, bool taken, uint8_t branch_type)
{
    taken ? ++(frequency_table[hash(ip)].TAKEN) : ++(frequency_table[hash(ip)].NTAKEN);
}
