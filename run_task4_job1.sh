#!/bin/bash

# Prepare testfile of size 1G
fio --name=prepare --rw=write --size=1G --filename=testfile --bs=1M \
    --ioengine=libaio --direct=1 --runtime=1 --time_based=1 \
    --output=prepare_output.txt

# Remove prepare output file
rm -f prepare_output.txt


# Task 4
echo "Starting Task 4"

numjobs_list="1"

for nj in $numjobs_list; do
  output_file="data/task4_numjobs${nj}.txt"
  echo "Running Task 4 with numjobs=$nj"
  for rep in {1..5}; do
    filename_prefix="data/task4_numjobs${nj}_rep${rep}"
    fio default.fio --numjobs=$nj --write_bw_log=$filename_prefix \
        --log_avg_msec=4000 --eta=never \
        --output=temp_output.txt
    # Process the bw log file
    bw_log_file="${filename_prefix}_test_bw.log"
    if [ -f "$bw_log_file" ]; then
      awk '{print $2}' "$bw_log_file" >> "$output_file"
    fi
    rm -f "$bw_log_file"
  done
  rm -f temp_output.txt
done

echo "All tasks completed."
