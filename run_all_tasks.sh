#!/bin/bash

# Create data directory
mkdir -p data

# Prepare testfile of size 1G
fio --name=prepare --rw=write --size=1G --filename=testfile --bs=1M \
    --ioengine=libaio --direct=1 --runtime=1 --time_based=1 \
    --output=prepare_output.txt

# Remove prepare output file
rm -f prepare_output.txt

# Task 1
echo "Starting Task 1"

percentages="0 12 25 38 50 63 75 88 100"

for access_pattern in 'rw' 'randrw'; do
  for pct in $percentages; do
    output_file="data/task1_${access_pattern}_pct${pct}.txt"
    echo "Running Task 1 with $access_pattern and write percentage $pct%"
    for rep in {1..10}; do
      filename_prefix="data/task1_${access_pattern}_pct${pct}_rep${rep}"
      fio default.fio --rw=$access_pattern --rwmixwrite=$pct \
          --write_bw_log=$filename_prefix --log_avg_msec=1000 \
          --eta=never --output=temp_output.txt
      # Process the bw log file
      bw_log_file="${filename_prefix}_test_bw.log"
      if [ -f "$bw_log_file" ]; then
        # Extract bandwidth data and append to output file
        awk '{print $2}' "$bw_log_file" >> "$output_file"
      fi
      # Clean up
      rm -f "$bw_log_file"
    done
    rm -f temp_output.txt
  done
done

# Task 2
echo "Starting Task 2"

blocksizes="1k 2k 4k 8k 16k 32k 64k 128k 256k 512k 1024k"

for bs in $blocksizes; do
  output_file="data/task2_bs${bs}.txt"
  echo "Running Task 2 with blocksize $bs"
  for rep in {1..10}; do
    filename_prefix="data/task2_bs${bs}_rep${rep}"
    fio default.fio --bs=$bs --write_bw_log=$filename_prefix --log_avg_msec=1000 \
        --eta=never --output=temp_output.txt
    # Process the bw log file
    bw_log_file="${filename_prefix}_test_bw.log"
    if [ -f "$bw_log_file" ]; then
      awk '{print $2}' "$bw_log_file" >> "$output_file"
    fi
    rm -f "$bw_log_file"
  done
  rm -f temp_output.txt
done

# Task 3
echo "Starting Task 3"

output_file="data/task3.txt"

for rep in {1..10}; do
  filename_prefix="data/task3_rep${rep}"
  fio default.fio --rw=write --bssplit=4k/30:16k/60:64k/10 \
      --write_bw_log=$filename_prefix --write_lat_log=$filename_prefix \
      --log_avg_msec=1000 --eta=never --output=temp_output.txt
  # Process the bw and lat log files
  bw_log_file="${filename_prefix}_test_bw.log"
  lat_log_file="${filename_prefix}_test_lat.log"
  if [ -f "$bw_log_file" ] && [ -f "$lat_log_file" ]; then
    # Paste the bandwidth and latency data side by side
    paste <(awk '{print $2}' "$bw_log_file") <(awk '{print $2}' "$lat_log_file") >> "$output_file"
  fi
  # Clean up
  rm -f "$bw_log_file" "$lat_log_file"
  rm -f temp_output.txt
done

# Task 4
echo "Starting Task 4"

numjobs_list="1 2 4 6 8"

for nj in $numjobs_list; do
  output_file="data/task4_numjobs${nj}.txt"
  echo "Running Task 4 with numjobs=$nj"
  for rep in {1..10}; do
    filename_prefix="data/task4_numjobs${nj}_rep${rep}"
    fio default.fio --numjobs=$nj --write_bw_log=$filename_prefix \
        --log_avg_msec=1000 --eta=never \
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
