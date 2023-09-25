#!/bin/bash

# Set the number of iterations
NUM_ITERATIONS=20
time_record="time_record_k6.txt"

################## LOCALLY ##################
# test to make sure it works first on local machine
# Iterate for the specified number of times
# for ((i = 1; i <= NUM_ITERATIONS; i++)); do
#   # echo "current_iteration  $i"
#   #export current_iteration=$i # a shell script that sets an env variable called current_iteration, make it available.
#   echo $i > iteration.txt
#   #start_time=$(date +%s)

#   #cat data_points.txt | python3 mapper_kmean.py | python3 reducer_kmean.py > outputtest_$i.txt
#   cat data_points.txt | python3 mapper_kmean.py > mapper_output_$i.txt
#   cat mapper_output_$i.txt | python3 reducer_kmean.py > outputtest_$i.txt
#   # end_time=$(date +%s)
#   # duration=$((end_time - start_time))
#   # echo "iteration $i duration: $duration" >> $time_record

# done

################## Hadoop ################## 
# Loop through iterations
for ((i = 1; i <= NUM_ITERATIONS; i++)); do
  OUTPUT_DIR="/user/hanxingsharpayyu/kmeanclustering_6/output_iteration_$i"
  start_time=$(date +%s)
  echo "current_iteration  $i"
  echo $i > iteration.txt
  hadoop jar /Users/hanxingsharpayyu/hadoop/hadoop-3.3.0/share/hadoop/tools/lib/hadoop-streaming-3.3.0.jar \
    -files /Users/hanxingsharpayyu/Desktop/MIE1826_cloud_based_big_data/assignment1/mapper_kmean.py,/Users/hanxingsharpayyu/Desktop/MIE1826_cloud_based_big_data/assignment1/reducer_kmean.py \
    -mapper 'python3 mapper_kmean.py' \
    -reducer 'python3 reducer_kmean.py' \
    -input /input_kmean/data_points.txt \
    -output "$OUTPUT_DIR"
  
  hdfs dfs -get "$OUTPUT_DIR" /Users/hanxingsharpayyu/Desktop/MIE1826_cloud_based_big_data/assignment1/get_centroids/centroids$i.txt
  end_time=$(date +%s)
  duration=$((end_time-start_time))
  echo "iteration $i duration: $duration seconds" >> $time_record
done  

# # try just iteration = 1
# hadoop jar /Users/hanxingsharpayyu/hadoop/hadoop-3.3.0/share/hadoop/tools/lib/hadoop-streaming-3.3.0.jar \
#     -files /Users/hanxingsharpayyu/Desktop/MIE1826_cloud_based_big_data/assignment1/mapper_kmean.py,/Users/hanxingsharpayyu/Desktop/MIE1826_cloud_based_big_data/assignment1/reducer_kmean.py \
#     -mapper 'python3 mapper_kmean.py' \
#     -reducer 'python3 reducer_kmean.py' \
#     -input /input_kmean/data_points.txt \
#     -output /user/hanxingsharpayyu/outp6




