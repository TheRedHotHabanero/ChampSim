import re
import os
import pandas as pd
from pathlib import Path

def extract_l2_stats(file_path):
    access = None
    miss = None
    with open(file_path, 'r') as f:
        for line in f:
            if "cpu0->cpu0_L2C TOTAL" in line:
                match = re.search(r'ACCESS:\s+(\d+)\s+HIT:\s+(\d+)\s+MISS:\s+(\d+)', line)
                if match:
                    access = int(match.group(1))
                    miss = int(match.group(3))
                    break
    miss_rate = miss / access if access and access > 0 else None
    return access, miss, miss_rate

def main(logs_dir):
    rows = []
    logs_dir = Path(logs_dir)
    for file in logs_dir.glob("*.txt"):
        access, miss, miss_rate = extract_l2_stats(file)
        rows.append({
            "Trace": file.name,
            "L2_ACCESS": access,
            "L2_MISS": miss,
            "L2_MISS_RATE": round(miss_rate, 4) if miss_rate is not None else "N/A"
        })

    df = pd.DataFrame(rows)
    df = df.sort_values("Trace")
    print(df.to_string(index=False))
    df.to_csv("l2_cache_miss_summary.csv", index=False)

if __name__ == "__main__":
    main("/home/karina/prog/ChampSim/homeworks/homework_2/mru")
