import pandas as pd
import numpy as np
import os

np.random.seed(42)

houses = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]

traits = {
    "Gryffindor":  {"courage": (8, 2), "ambition": (5, 2), "loyalty": (6, 2), "intelligence": (6, 2), "bravery": (9, 1)},
    "Slytherin":   {"courage": (5, 2), "ambition": (9, 1), "loyalty": (4, 2), "intelligence": (7, 2), "bravery": (5, 2)},
    "Hufflepuff":  {"courage": (5, 2), "ambition": (4, 2), "loyalty": (9, 1), "intelligence": (5, 2), "bravery": (5, 2)},
    "Ravenclaw":   {"courage": (5, 2), "ambition": (5, 2), "loyalty": (5, 2), "intelligence": (9, 1), "bravery": (5, 2)},
}

data = []
for _ in range(200):
    house = np.random.choice(houses)
    row = {"house": house}
    for trait, (mean, std) in traits[house].items():
        row[trait] = max(1, min(10, int(np.random.normal(mean, std))))
    data.append(row)

df = pd.DataFrame(data)
os.makedirs("data", exist_ok=True)
df.to_csv("data/hogwarts_dataset.csv", index=False)
print(f"Dataset generated: {len(df)} samples")
print(df.head())
