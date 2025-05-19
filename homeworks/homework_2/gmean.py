import pandas as pd
import numpy as np

data = pd.read_csv("/home/karina/prog/ChampSim/homeworks/homework_2/final_table.txt", sep=r"\s+")
data = data.drop(columns=["Trace"])
gmeans = data.apply(lambda col: np.prod(col) ** (1 / len(col)))
print(gmeans)
