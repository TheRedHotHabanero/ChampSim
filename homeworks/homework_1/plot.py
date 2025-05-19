import pandas as pd
import matplotlib.pyplot as plt

# Загрузка таблицы
df = pd.read_csv("/home/karina/prog/ChampSim/homeworks/homework_1/final_table.txt", delim_whitespace=True)

# Удаляем строку GMEAN (последняя строка с NaN в Trace)
df = df[df['Trace'] != 'GMEAN']

# Настраиваем размер и шрифт
plt.rcParams.update({'font.size': 8})
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 8), sharex=True)

# Строим IPC
ax1.plot(df['Trace'], df['IPC_bimodal'], label='Bimodal', marker='o')
ax1.plot(df['Trace'], df['IPC_model_1'], label='Model 1 (Freq)', marker='o')
ax1.plot(df['Trace'], df['IPC_model_2'], label='Model 2 (Prob)', marker='o')
ax1.set_title("IPC per Trace")
ax1.set_ylabel("IPC")
ax1.legend()
ax1.grid(True)

# Строим MPKI
ax2.plot(df['Trace'], df['MPKI_bimodal'], label='Bimodal', marker='o')
ax2.plot(df['Trace'], df['MPKI_model_1'], label='Model 1 (Freq)', marker='o')
ax2.plot(df['Trace'], df['MPKI_model_2'], label='Model 2 (Prob)', marker='o')
ax2.set_title("MPKI per Trace")
ax2.set_ylabel("MPKI")
ax2.set_xlabel("Trace")
ax2.legend()
ax2.grid(True)
plt.xticks(rotation=90)

plt.tight_layout()
plt.savefig("predictor_comparison.png", dpi=300)
plt.show()
