#include "markov_model_1.h"

// REalization based on bimodal.cc
bool markov_model_1::predict_branch(champsim::address ip)
{
    auto value = frequency_table[hash(ip)];
    return value.TAKEN > value.NTAKEN;
}

void markov_model_1::last_branch_result(champsim::address ip, champsim::address branch_target, bool taken, uint8_t branch_type)
{
    taken ? ++(frequency_table[hash(ip)].TAKEN) : ++(frequency_table[hash(ip)].NTAKEN);
}
