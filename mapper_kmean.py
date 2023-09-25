#!/usr/bin/env python

import sys
import os

initial_centroids = []
centroid_id = 0
# Read initial centroids from the file
with open("/Users/hanxingsharpayyu/Desktop/MIE1826_cloud_based_big_data/assignment1/initial_centroids.txt", "r") as f:
    for line in f:
        x, y = map(float, line.strip().split(',')) # comma between x and y but tab b/w each point
        initial_centroids.append((centroid_id, x, y))
        centroid_id += 1


# Get the iteration number
#iteration = int(os.environ.get('current_iteration'),1)
with open("/Users/hanxingsharpayyu/Desktop/MIE1826_cloud_based_big_data/assignment1/iteration.txt", "r") as f:
    iteration = int(f.read())
# print("mapper iteration: ", iteration) ##### this was the issue cuz it got printed as the output of the mapper!!!
centroids_list = []
centroids = initial_centroids
if iteration == 1:
        centroids = initial_centroids
else: 
    #output_file = f"/Users/hanxingsharpayyu/Desktop/MIE1826_cloud_based_big_data/assignment1/output_{iteration-1}.txt" #for local test
    output_file = f"/Users/hanxingsharpayyu/Desktop/MIE1826_cloud_based_big_data/assignment1/get_centroids/centroids{iteration-1}.txt/part-00000" #for hadoop
    with open(output_file, "r") as f:
        for line in f:
            centroid_id, centroid_coordinates = map(str.strip, line.split('\t'))
            x, y = map(float, centroid_coordinates.strip().split(','))
            centroids_list.append((int(centroid_id), x, y))
    centroids = centroids_list

for line in sys.stdin: # system input is data_points.txt
    x, y = map(float, line.strip().split(','))

    distances = [(centroid_id, (x - cx) ** 2 + (y - cy) ** 2) for centroid_id, cx, cy in centroids]
    # Find nearest centroid and emit
    nearest_centroid_id = min(distances, key=lambda x: x[1])[0]
    print(f'{nearest_centroid_id}\t{x},{y}')


# output of mapper should be:
# key value pair of each data point
# cluster 0, x,y
# cluster 1, x,y
# cluster 2, x,y
# .... repeat for all data points