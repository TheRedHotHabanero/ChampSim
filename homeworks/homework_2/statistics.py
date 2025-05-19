import pandas as pd
from pathlib import Path

files = [
    ("/home/karina/prog/ChampSim/homeworks/homework_2/drrip/results.txt", "DRRIP"),
    ("/home/karina/prog/ChampSim/homeworks/homework_2/lru/results.txt", "LRU"),
    ("/home/karina/prog/ChampSim/homeworks/homework_2/mru/results.txt", "MRU"),
    ("/home/karina/prog/ChampSim/homeworks/homework_2/plru/results.txt", "PLRU")
]

combined_df = None

for filename, model in files:
    df = pd.read_csv(filename, delim_whitespace=True, usecols=["Trace", "L2_MISS_RATE"])
    df = df.dropna(subset=["L2_MISS_RATE"])
    df["L2_MISS_RATE"] = pd.to_numeric(df["L2_MISS_RATE"], errors='coerce')
    df = df.rename(columns={"L2_MISS_RATE": f"MISS_RATE_{model}"})
    
    if combined_df is None:
        combined_df = df
    else:
        combined_df = pd.merge(combined_df, df, on="Trace", how="outer")

combined_df = combined_df.sort_values("Trace")
combined_df.to_csv("combined_miss_rates.csv", index=False)
print(combined_df.to_string(index=False))
