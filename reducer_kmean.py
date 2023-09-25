#!/usr/bin/env python

import sys
from collections import defaultdict

# Dictionary to store points for each centroid
cluster_points = defaultdict(list)

for line in sys.stdin:
    centroid, point = line.strip().split('\t')
    cluster_points[int(centroid)].append(tuple(map(float, point.split(','))))

# Compute new centroids
new_centroids = []
for centroid, points in cluster_points.items():
    num_points = len(points)
    sum_x = sum(p[0] for p in points)
    sum_y = sum(p[1] for p in points)
    new_x = sum_x / num_points if num_points > 0 else 0
    new_y = sum_y / num_points if num_points > 0 else 0
    new_centroids.append((new_x, new_y))

# Output new centroids
for i, centroid in enumerate(new_centroids):
    print(f'{i}\t{centroid[0]},{centroid[1]}')

## input of reducer should be like:
# after magic:
# cluster 0[(x,y),(x,y),(x,y)....]
# cluster 1[(x,y),(x,y),(x,y)....]
# cluster 2[(x,y),(x,y),(x,y)....]
### output of reducer should be:
# cluster 0, x,y
# repeat for all clusters and all points in each cluster