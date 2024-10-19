#!/bin/bash

for i in {1..5};
do
    fio test.fio --output-format=json --output=test_$i.json --write_bw_log=test_bw_$i.log --write_lat_log=test_lat_$i --log_avg_msec=1000 --log_max_value=1 
    sleep 1
done 