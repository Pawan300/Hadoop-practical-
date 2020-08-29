# Hadoop-practical-

For running this practicals:
- Prerequisite => Hadoop , Python

Common commands for the hadoop

* For loading data into hdfs
   - hdfs dfs -put filename hdfs_location
* For making directory 
   - hdfs dfs -mkdir /user/hadoop/new_location
* For deleting directory
   - hdfs dfs -rm -r /user/hadoop/new_location
* For merging result in the file
   - hdfs dfs -getmerge /user/hadoop/new_location filename
* Run program
   - hadoop jar location_JAR \
     -input location_input \
     -output location_output \
     -mapper mapper_location \
     -reducer reducer_location \
     -numReduceTasks number_Of_reducer

Point to be notice:
- every time you are running hadoop make sure output location should not already existed.
- numReduceTasks also making sure that keys in output are sorted for >1.