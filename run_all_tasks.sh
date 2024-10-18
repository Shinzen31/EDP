#!/bin/bash

# Function to convert bandwidth to KB/s
function convert_to_kb() {
  local bw_str=$1
  local num=$(echo $bw_str | grep -oP '^[0-9.]+')
  local unit=$(echo $bw_str | grep -oP '[KMG]?i?B/s$')
  case $unit in
    'B/s')
      factor=0.001
      ;;
    'KiB/s')
      factor=1
      ;;
    'KB/s')
      factor=1
      ;;
    'MiB/s')
      factor=1024
      ;;
    'MB/s')
      factor=1024
      ;;
    'GiB/s')
      factor=1048576
      ;;
    'GB/s')
      factor=1048576
      ;;
    *)
      factor=1
      ;;
  esac
  result=$(echo "$num * $factor" | bc)
  echo $result
}

# Function to parse bandwidth from fio output
function parse_bw() {
  local file=$1
  local read_bw=$(grep 'READ:' $file | grep -oP 'bw=\s*\K[0-9.]+[KMG]?i?B/s')
  local write_bw=$(grep 'WRITE:' $file | grep -oP 'bw=\s*\K[0-9.]+[KMG]?i?B/s')

  # Convert to KB/s
  read_bw_kb=$(convert_to_kb $read_bw)
  write_bw_kb=$(convert_to_kb $write_bw)

  total_bw_kb=$(echo "$read_bw_kb + $write_bw_kb" | bc)
  echo $total_bw_kb
}

# Prepare testfile of size 1G
fio --name=prepare --rw=write --size=1G --filename=testfile --bs=1M --ioengine=libaio --direct=1 --runtime=1 --time_based=1 --output=prepare_output.txt

# Remove prepare job file
rm prepare_output.txt

# Task 1
echo "Starting Task 1"

percentages="0 12 25 38 50 63 75 88 100"

for access_pattern in 'rw' 'randrw'; do
  for pct in $percentages; do
    output_file="task1_${access_pattern}_pct${pct}.txt"
    echo "Running Task 1 with $access_pattern and write percentage $pct%"
    for rep in {1..5}; do
      fio default.fio --rw=$access_pattern --rwmixwrite=$pct --output=temp_output.txt
      # Extract total bandwidth
      total_bw=$(parse_bw temp_output.txt)
      echo $total_bw >> $output_file
    done
    rm temp_output.txt
  done
done

# Task 2
echo "Starting Task 2"

blocksizes="1k 2k 4k 8k 16k 32k 64k 128k 256k 512k 1024k"

for bs in $blocksizes; do
  output_file="task2_bs${bs}.txt"
  echo "Running Task 2 with blocksize $bs"
  for rep in {1..5}; do
    fio default.fio --bs=$bs --output=temp_output.txt
    # Extract total bandwidth
    total_bw=$(parse_bw temp_output.txt)
    echo $total_bw >> $output_file
  done
  rm temp_output.txt
done

# Task 3
echo "Starting Task 3"

output_file="task3.txt"

for rep in {1..5}; do
  fio default.fio --rw=write --bssplit=4k/30:16k/60:64k/10 --output=temp_output.txt
  # Extract total bandwidth
  total_bw=$(parse_bw temp_output.txt)
  # Extract average latency in microseconds
  avg_lat=$(grep 'clat (usec):' temp_output.txt | grep -oP 'avg=\s*\K[0-9.]+')
  if [ -z "$avg_lat" ]; then
    avg_lat=$(grep 'clat (msec):' temp_output.txt | grep -oP 'avg=\s*\K[0-9.]+')
    avg_lat=$(echo "$avg_lat * 1000" | bc) # Convert msec to usec
  fi
  echo "$total_bw $avg_lat" >> $output_file
done

rm temp_output.txt

# Task 4
echo "Starting Task 4"

numjobs_list="1 2 4 6 8"

for nj in $numjobs_list; do
  output_file="task4_numjobs${nj}.txt"
  echo "Running Task 4 with numjobs=$nj"
  for rep in {1..5}; do
    fio default.fio --numjobs=$nj --output=temp_output.txt
    # Extract total bandwidth
    total_bw=$(parse_bw temp_output.txt)
    echo $total_bw >> $output_file
  done
  rm temp_output.txt
done

echo "All tasks completed."
