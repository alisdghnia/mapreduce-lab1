#!/bin/sh

# Start Hadoop services
../../start.sh

# Remove existing HDFS directories if they exist
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab1/output/

# Create new HDFS directory for input
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /lab1/input/

# Copy log file from local filesystem to HDFS
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../mapreduce-test-data/access.log /lab1/input/

# Run the Hadoop MapReduce job
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../../mapreduce-test-python/lab1/mapper_1.py    -mapper ../../mapreduce-test-python/lab1/mapper_1.py \
-file ../../mapreduce-test-python/lab1/reducer_1.py   -reducer ../../mapreduce-test-python/lab1/reducer_1.py \
-input /lab1/input/* -output /lab1/output/

# Output the results to the console
/usr/local/hadoop/bin/hdfs dfs -cat /lab1/output/part-00000

# Clean up: remove the HDFS directories used for input and output
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab1/output/

# Stop Hadoop services
../../stop.sh
