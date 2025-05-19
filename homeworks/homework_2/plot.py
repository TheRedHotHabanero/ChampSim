import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

df = pd.read_csv("/home/karina/prog/ChampSim/homeworks/homework_2/final_table.txt", sep=r"\s+")
df.columns = df.columns.str.strip()

df["Trace"] = df["Trace"].str.replace(".txt", "", regex=False)
df = df.sort_values("Trace")

scale = 4
plt.figure(figsize=(15, 15))
plt.plot(df["Trace"], df["MISS_RATE_DRRIP"], label="DRRIP", marker='o', markersize=scale)
#plt.plot(df["Trace"], df["MISS_RATE_LRU"], label="LRU", marker='o', markersize=scale)
#plt.plot(df["Trace"], df["MISS_RATE_MRU"], label="MRU", marker='o', markersize=scale)
plt.plot(df["Trace"], df["MISS_RATE_PLRU"], label="PLRU", marker='o', markersize=scale)


plt.xlabel("Trace")
plt.ylabel("L2 Miss Rate")
plt.title("L2 Cache Miss Rate by Replacement Policy")
plt.legend()
plt.grid(True)
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("/home/karina/prog/ChampSim/homeworks/homework_2/Figure_drrip_and_plru.png", dpi=300)
