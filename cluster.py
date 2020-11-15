#!/usr/bin/env python3

import numpy as np
from sklearn.cluster import KMeans
from pandas import read_csv

data = read_csv("SpotifyFeatures.csv")

print(head

kmeans_model = KMeans(n_clusters=26, random_state=1).fit(X)
