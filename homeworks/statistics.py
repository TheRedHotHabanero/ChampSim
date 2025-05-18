import json
import math
from pathlib import Path

def parse_file(file_path):
    data = []
    with open(file_path, "r") as f:
        for line in f:
            if line.strip():
                d = eval(line.strip())
                trace_name = Path(d["trace"]).name.split("-")[0]  # e.g., 600.perlbench_s
                data.append((trace_name, d["IPC"], d["MPKI"]))
    return data

def gmean(values):
    product = 1.0
    n = len(values)
    for v in values:
        product *= v
    return product ** (1 / n) if n > 0 else 0

files = {
    "bimodal": "/home/karina/prog/ChampSim/homeworks/homework_1/bimodal/results.txt",
    "model_1": "/home/karina/prog/ChampSim/homeworks/homework_1/model_1/results.txt",
    "model_2": "/home/karina/prog/ChampSim/homeworks/homework_1/model_2/results.txt",
}

model_data = {}
for model, path in files.items():
    model_data[model] = {}
    for trace_name, ipc, mpki in parse_file(path):
        model_data[model][trace_name] = (ipc, mpki)

all_traces = sorted(set().union(*[d.keys() for d in model_data.values()]))

print(f"{'Trace':<24} {'IPC_bimodal':<12} {'MPKI_bimodal':<13} {'IPC_model_1':<12} {'MPKI_model_1':<13} {'IPC_model_2':<12} {'MPKI_model_2':<13}")

ipc_sums = {"bimodal": [], "model_1": [], "model_2": []}
mpki_sums = {"bimodal": [], "model_1": [], "model_2": []}

for trace in all_traces:
    row = [trace]
    for model in ["bimodal", "model_1", "model_2"]:
        ipc, mpki = model_data.get(model, {}).get(trace, (None, None))
        row.append(f"{ipc:.3f}" if ipc is not None else "N/A")
        row.append(f"{mpki:.3f}" if mpki is not None else "N/A")
        if ipc is not None: ipc_sums[model].append(ipc)
        if mpki is not None: mpki_sums[model].append(mpki)
    print(f"{row[0]:<24} {row[1]:<12} {row[2]:<13} {row[3]:<12} {row[4]:<13} {row[5]:<12} {row[6]:<13}")

# GMEAN
print("-" * 95)
print(f"{'GMEAN':<24} "
      f"{gmean(ipc_sums['bimodal']):<12.3f} {gmean(mpki_sums['bimodal']):<13.3f} "
      f"{gmean(ipc_sums['model_1']):<12.3f} {gmean(mpki_sums['model_1']):<13.3f} "
      f"{gmean(ipc_sums['model_2']):<12.3f} {gmean(mpki_sums['model_2']):<13.3f}")
