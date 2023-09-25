This project is to experiment using Hadoop to process large amounts of data on a pseudo-distributed node. 

### line count with map reduce
1. make sure things can executed on my local desktop:
cat shakespeare.txt |python3 mapper.py |sort |python3 reducer.py

2. create new directory on HDFS and upload file
cd /Users/hanxingsharpayyu/hadoop/hadoop-3.3.0
hdfs dfs -mkdir /shakespeare
hdfs dfs -put /Users/../Desktop/.../shakespeare.txt /shakespeare

3. execute mapreduce
hadoop jar /Users/.../hadoop/hadoop-3.3.0/share/hadoop/tools/lib/hadoop-streaming-3.3.0.jar \
-files /Users/hanxingsharpayyu/Desktop/.../wordcount/mapper.py,/Users/../Desktop/.../wordcount/reducer.py \
-mapper 'python3 mapper.py' \
-reducer 'python3 reducer.py' \
-input /shakespeare/shakespeare.txt \
-output outp/output_shakespeare2

4. cat output file
hdfs dfs -cat /user/.../output_shakespeare/part-00000

### k mean clustering with map reduce
locally:
1. one iteration, make sure it works
cat data_points.txt |python3 mapper_kmean.py |python3 reducer_kmean.py
2. adding iterations, via: ./run_iterations.sh
3. add time record

Hadoop:
-  create new directory on HDFS (/kmean_clustering and output_kmeanclustering)and upload file (data_points.txt)) 
-  use hdfs dfs -get "/hadoop/centorids/path" "/local/path" at the end of each iteration to get the new centroids, so the next iteration can use the new centroids. 
-  ./run_iterations.sh
- merge the output files 
(hdfs dfs -getmerge /user/.../output_kmeanclustering/output_iteration_* merged_output.txt)
- repeat the same for k = 6 (output into output_kmeanclustering)
