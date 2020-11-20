#!/usr/bin/env python3

import pandas as pd
from collections import Counter


df = pd.read_csv("SpotifyFeatures.csv")

df = df[df.genre != "A Capella"]

c = Counter(df.genre)

m = c.most_common()[-1][1]
print(m)

c = Counter()

df = df.sample(frac=1)

rows = [True] * len(df)
for i, val in enumerate(df.genre):
    c[val] += 1
    if c[val] > m:
        rows[i] = False

df = df[rows]

df.to_csv("equal.csv", index=False)


print(len(df))
