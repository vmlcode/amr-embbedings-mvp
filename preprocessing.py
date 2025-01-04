import os
import pandas as pd 
from utils import ReadFasta, kmer

sensible_data = os.listdir("./db/WGS/Sensible")
resistant_data = os.listdir("./db/WGS/Resistant")

df = pd.DataFrame({"wgs": [], "AMR": []})
print(df)

for file in sensible_data:
    read = ReadFasta(f"./db/WGS/Sensible/{file}")
    df.loc[len(df)] = [str(read["seq"]), 0]

for file in resistant_data:
    read = ReadFasta(f"./db/WGS/Resistant/{file}")
    df.loc[len(df)] = [str(read["seq"]), 1]

print(df)

for seq in df["wgs"]:
    df["kmer"] = [kmer(seq, 10) for seq in df["wgs"]]

print(df)