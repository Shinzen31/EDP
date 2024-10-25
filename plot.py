import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statistics


# task1 read-write
med_bw_read = []
med_bw_write = []
avg_bw_read = []
avg_bw_write = []
std_bw_read = []
std_bw_write = []

pct = [0, 12, 25, 38, 50, 63, 75, 88, 100]

for k in pct:
    temp_read_bw = []
    temp_write_bw = []

    for i in [1, 2, 3, 4, 5]:
        read_file = f'data/task1_rw_pct{k}_rep{i}_bw.1.log'
        try:
            df = pd.read_csv(read_file, header=None)
            for index, row in df.iterrows():
                if row[2] == 0:  
                    temp_read_bw.append(row[1])  
                elif row[2] == 1:  
                    temp_write_bw.append(row[1])  

        except FileNotFoundError:
            print(f"File {read_file} not found")
            continue

    med_bw_read.append(np.median(temp_read_bw))
    med_bw_write.append(np.median(temp_write_bw))
    avg_bw_read.append(np.mean(temp_read_bw))
    avg_bw_write.append(np.mean(temp_write_bw))
    std_bw_read.append(np.std(temp_read_bw))
    std_bw_write.append(np.std(temp_write_bw))

    
print(f"Read bandwidth (task1) median:", med_bw_read, "mean value:", avg_bw_read, "standard deviation:", std_bw_read)
print(f"Write bandwidth (task1) median:", med_bw_write, "mean value:", avg_bw_write, "standard deviation:", std_bw_write)

plt.figure(figsize=(10, 6))
plt.errorbar(pct, avg_bw_read, yerr=std_bw_read, fmt='o', label='Average Read BW', capsize=5, color='blue')
plt.scatter(pct, med_bw_read, label='Median Read BW', color='cyan')
plt.errorbar(pct, avg_bw_write, yerr=std_bw_write, fmt='o', label='Average Write BW', capsize=5, color='red')
plt.scatter(pct, med_bw_write, label='Median Write BW', color='magenta')

plt.title('Read and Write Bandwidth with Median, Mean, and Std Dev')
plt.xlabel('Write Percentages')
plt.ylabel('Bandwidth')
plt.legend()
plt.grid(True)
plt.savefig('task1_rw_bw.png')
plt.show()



# task1 random read-write
med_bw_read = []
med_bw_write = []
avg_bw_read = []
avg_bw_write = []
std_bw_read = []
std_bw_write = []

for k in pct:
    temp_read_bw = []
    temp_write_bw = []

    for i in [1, 2, 3, 4, 5]:
        read_file = f'data/task1_randrw_pct{k}_rep{i}_bw.1.log'
        try:
            df = pd.read_csv(read_file, header=None)
            for index, row in df.iterrows():
                if row[2] == 0:  
                    temp_read_bw.append(row[1])  
                elif row[2] == 1:  
                    temp_write_bw.append(row[1])  

        except FileNotFoundError:
            print(f"File {read_file} not found")
            continue

    med_bw_read.append(np.median(temp_read_bw))
    med_bw_write.append(np.median(temp_write_bw))
    avg_bw_read.append(np.mean(temp_read_bw))
    avg_bw_write.append(np.mean(temp_write_bw))
    std_bw_read.append(np.std(temp_read_bw))
    std_bw_write.append(np.std(temp_write_bw))

print(f"Read bandwidth (task1 random) median:", med_bw_read, "mean value:", avg_bw_read, "standard deviation:", std_bw_read)
print(f"Write bandwidth (task1 random) median:", med_bw_write, "mean value:", avg_bw_write, "standard deviation:", std_bw_write)

plt.figure(figsize=(10, 6))
plt.errorbar(pct, avg_bw_read, yerr=std_bw_read, fmt='o', label='Average Read BW', capsize=5, color='blue')
plt.scatter(pct, med_bw_read, label='Median Read BW', color='cyan')
plt.errorbar(pct, avg_bw_write, yerr=std_bw_write, fmt='o', label='Average Write BW', capsize=5, color='red')
plt.scatter(pct, med_bw_write, label='Median Write BW', color='magenta')

plt.title('Random Read and Write Bandwidth with Median, Mean, and Std Dev')
plt.xlabel('Write Percentages')
plt.ylabel('Bandwidth')
plt.legend()
plt.grid(True)
plt.savefig('task1_rand_rw_bw.png')
plt.show()

# task2
med_bw_read = []
avg_bw_read = []
std_bw_read = []
med_bw_write = []
avg_bw_write = []
std_bw_write = []

req_size = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

for k in req_size:
    temp_read_bw = []
    temp_write_bw = []

    for i in [1, 2, 3, 4, 5]:
        read_file = f'data/task2_bs{k}k_rep{i}_bw.1.log'
        try:
            df = pd.read_csv(read_file, header=None)
            for index, row in df.iterrows():
                if row[2] == 0:  
                    temp_read_bw.append(row[1])  
                elif row[2] == 1:  
                    temp_write_bw.append(row[1])  

        except FileNotFoundError:
            print(f"File {read_file} not found")
            continue

    if len(temp_read_bw) > 0:  
        med_bw_read.append(np.median(temp_read_bw))
        avg_bw_read.append(np.mean(temp_read_bw))
        std_bw_read.append(np.std(temp_read_bw))
    else:
        print(f"No data for read bandwidth at k={k}")
        med_bw_read.append(None)
        avg_bw_read.append(None)
        std_bw_read.append(None)

    if len(temp_write_bw) > 0: 
        med_bw_write.append(np.median(temp_write_bw))
        avg_bw_write.append(np.mean(temp_write_bw))
        std_bw_write.append(np.std(temp_write_bw))
    else:
        print(f"No data for write bandwidth at k={k}")
        med_bw_write.append(None)
        avg_bw_write.append(None)
        std_bw_write.append(None)

print(f"Read bandwidth (task2) median:", med_bw_read, "mean value:", avg_bw_read, "standard deviation:", std_bw_read)
print(f"Write bandwidth (task2) median:", med_bw_write, "mean value:", avg_bw_write, "standard deviation:", std_bw_write)

plt.figure(figsize=(10, 6)) 
plt.errorbar(req_size, avg_bw_read, yerr=std_bw_read, fmt='o', label='Average Read BW', capsize=5, color='blue')
plt.scatter(req_size, med_bw_read, label='Median Read BW', color='cyan')
plt.errorbar(req_size, avg_bw_write, yerr=std_bw_write, fmt='o', label='Average Write BW', capsize=5, color='red')
plt.scatter(req_size, med_bw_write, label='Median Write BW', color='magenta')

plt.title('Read and Write Bandwidth with Median, Mean, and Std Dev')
plt.xlabel('Request Size')
plt.xscale('log')
plt.ylabel('Bandwidth')
plt.legend()
plt.grid(True)
plt.savefig('task2_bw_req_size.png')
plt.show()

# task4
med_bw_read = []
avg_bw_read = []
std_bw_read = []
med_bw_write = []
avg_bw_write = []
std_bw_write = []

parallel = [1, 2, 4, 6, 8]

for k in parallel:
    temp_read_bw = []
    temp_write_bw = []

    for i in [1, 2, 3, 4, 5]:
        read_file = f'data/task4_numjobs{k}_rep{i}_bw.1.log'
        try:
            df = pd.read_csv(read_file, header=None)
            for index, row in df.iterrows():
                if row[2] == 0:  
                    temp_read_bw.append(row[1])  
                elif row[2] == 1:  
                    temp_write_bw.append(row[1])  

        except FileNotFoundError:
            print(f"File {read_file} not found")
            continue

    med_bw_read.append(np.median(temp_read_bw))
    avg_bw_read.append(np.mean(temp_read_bw))
    std_bw_read.append(np.std(temp_read_bw))
    med_bw_write.append(np.median(temp_write_bw))
    avg_bw_write.append(np.mean(temp_write_bw))
    std_bw_write.append(np.std(temp_write_bw))

print(f"Read bandwidth (task4) median:", med_bw_read, "mean value:", avg_bw_read, "standard deviation:", std_bw_read)
print(f"Write bandwidth (task4) median:", med_bw_write, "mean value:", avg_bw_write, "standard deviation:", std_bw_write)

plt.figure(figsize=(10, 6))
plt.errorbar(parallel, avg_bw_read, yerr=std_bw_read, fmt='o', label='Average Read BW', capsize=5, color='blue')
plt.scatter(parallel, med_bw_read, label='Median Read BW', color='cyan')
plt.errorbar(parallel, avg_bw_write, yerr=std_bw_write, fmt='o', label='Average Write BW', capsize=5, color='red')
plt.scatter(parallel, med_bw_write, label='Median Write BW', color='magenta')

plt.title('Read and Write Bandwidth with Median, Mean, and Std Dev')
plt.xlabel('Number of Jobs')
plt.ylabel('Bandwidth')
plt.legend()
plt.grid(True)
plt.savefig('task4_numjobs_bw.png')
plt.show()


# task3 bandwidth 
med_bw_read = []
avg_bw_read = []
std_bw_read = []
med_bw_write = []
avg_bw_write = []
std_bw_write = []

for i in [1, 2, 3, 4, 5]:
    read_file = f'data/task3_rep{i}_bw.1.log'

    try:
        df = pd.read_csv(read_file, header=None)

        temp_read_bw = []
        temp_write_bw = []

        for index, row in df.iterrows():
            if row[2] == 0:  
                temp_read_bw.append(row[1])  
            elif row[2] == 1:  
                temp_write_bw.append(row[1])  

    except FileNotFoundError:
        print(f"File {read_file} not found")
        continue

med_bw_read.append(np.median(temp_read_bw))
avg_bw_read.append(np.mean(temp_read_bw))
std_bw_read.append(np.std(temp_read_bw))
med_bw_write.append(np.median(temp_write_bw))
avg_bw_write.append(np.mean(temp_write_bw))
std_bw_write.append(np.std(temp_write_bw))

print(f"Read bandwidth (task3) median:", med_bw_read, "mean value:", avg_bw_read, "standard deviation:", std_bw_read)
print(f"Write bandwidth (task3) median:", med_bw_write, "mean value:", avg_bw_write, "standard deviation:", std_bw_write)



#task3
lat_read, clat_read, slat_read = [], [], []
lat_write, clat_write, slat_write = [], [], []

# total latency, completion latency, submission latency
for i in [1, 2, 3, 4, 5]:
    try:
        df_lat = pd.read_csv(f'data/task3_rep{i}_lat.1.log', header=None)
        temp_read_lat = df_lat[df_lat[2] == 0][1].tolist()
        temp_write_lat = df_lat[df_lat[2] == 1][1].tolist()
        lat_read.append(np.median(temp_read_lat))
        lat_write.append(np.median(temp_write_lat))
    except FileNotFoundError:
        print(f"File data/task3_rep{i}_lat.1.log not found")
        continue

    try:
        df_clat = pd.read_csv(f'data/task3_rep{i}_clat.1.log', header=None)
        temp_read_clat = df_clat[df_clat[2] == 0][1].tolist()
        temp_write_clat = df_clat[df_clat[2] == 1][1].tolist()
        clat_read.append(np.median(temp_read_clat))
        clat_write.append(np.median(temp_write_clat))
    except FileNotFoundError:
        print(f"File data/task3_rep{i}_clat.1.log not found")
        continue

    try:
        df_slat = pd.read_csv(f'data/task3_rep{i}_slat.1.log', header=None)
        temp_read_slat = df_slat[df_slat[2] == 0][1].tolist()
        temp_write_slat = df_slat[df_slat[2] == 1][1].tolist()
        slat_read.append(np.median(temp_read_slat))
        slat_write.append(np.median(temp_write_slat))
    except FileNotFoundError:
        print(f"File data/task3_rep{i}_slat.1.log not found")
        continue

avg_lat_read = np.mean(lat_read)
std_lat_read = np.std(lat_read)
avg_clat_read = np.mean(clat_read)
std_clat_read = np.std(clat_read)
avg_slat_read = np.mean(slat_read)
std_slat_read = np.std(slat_read)
avg_lat_write = np.mean(lat_write)
std_lat_write = np.std(lat_write)
avg_clat_write = np.mean(clat_write)
std_clat_write = np.std(clat_write)
avg_slat_write = np.mean(slat_write)
std_slat_write = np.std(slat_write)


latency_categories = ['Total Read Latency', 'Completion Read Latency', 'Submission Read Latency',
                      'Total Write Latency', 'Completion Write Latency', 'Submission Write Latency']
latency_values = [avg_lat_read, avg_clat_read, avg_slat_read, 
                  avg_lat_write, avg_clat_write, avg_slat_write]

colors = ['darkblue', 'blue', 'lightblue', 'darkgreen', 'green', 'lightgreen']

latency_errors = [std_lat_read, std_clat_read, std_slat_read, 
                  std_lat_write, std_clat_write, std_slat_write]

plt.figure(figsize=(10, 6))
bars = plt.bar(latency_categories, latency_values, color=colors, yerr=latency_errors, capsize=5, error_kw={'ecolor': 'red'})

plt.title('Latency Comparison')
plt.ylabel('Latency (ms)')
plt.legend(bars, latency_categories)
plt.xticks([])  

plt.savefig('task3_latency_bar.png')
plt.show()



# percentile
percentiles = [50, 90, 99]
read_percentiles = np.percentile(lat_read, percentiles)
write_percentiles = np.percentile(lat_write, percentiles)
s_r_perc = np.percentile(slat_read, percentiles)
s_w_perc = np.percentile(slat_write, percentiles)
c_r_perc = np.percentile(clat_read, percentiles)
c_w_perc = np.percentile(clat_write, percentiles)


plt.figure(figsize=(10, 6))
plt.plot(percentiles, read_percentiles, marker='o', label='Total Read Latency Percentile')
plt.xlabel('Percentile')
plt.ylabel('Latency (ms)')
plt.title('Total Latency Percentile')
plt.legend()
plt.grid(True)
plt.savefig('task3_lat_perc_r.png')
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(percentiles, write_percentiles, marker='o', label='Total Write Latency Percentile')
plt.xlabel('Percentile')
plt.ylabel('Latency (ms)')
plt.title('Total Latency Percentile')
plt.legend()
plt.grid(True)
plt.savefig('task3_lat_perc_w.png')
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(percentiles, s_r_perc, marker='o', label='Submission Read Latency Percentile')
plt.xlabel('Percentile')
plt.ylabel('Latency (ms)')
plt.title('Submission Latency Percentile')
plt.legend()
plt.grid(True)
plt.savefig('task3_slat_perc_r.png')
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(percentiles, s_w_perc, marker='o', label='Submission Write Latency Percentile')
plt.xlabel('Percentile')
plt.ylabel('Latency (ms)')
plt.title('Submission Latency Percentile')
plt.legend()
plt.grid(True)
plt.savefig('task3_slat_perc_w.png')
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(percentiles, c_r_perc, marker='o', label='Completion Read Latency Percentile')
plt.xlabel('Percentile')
plt.ylabel('Latency (ms)')
plt.title('Completion Latency Percentile')
plt.legend()
plt.grid(True)
plt.savefig('task3_clat_perc_r.png')
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(percentiles, c_w_perc, marker='o', label='Completion Write Latency Percentile')
plt.xlabel('Percentile')
plt.ylabel('Latency (ms)')
plt.title('Completion Latency Percentile')
plt.legend()
plt.grid(True)
plt.savefig('task3_clat_perc_w.png')
plt.show()



# Cumulative Distribution Function
read_lat_sorted = np.sort(lat_read)
write_lat_sorted = np.sort(lat_write)
read_clat_sorted = np.sort(clat_read)
write_clat_sorted = np.sort(clat_write)
read_slat_sorted = np.sort(slat_read)
write_slat_sorted = np.sort(slat_write)

read_cdf = np.arange(1, len(read_lat_sorted) + 1) / len(read_lat_sorted)
write_cdf = np.arange(1, len(write_lat_sorted) + 1) / len(write_lat_sorted)
read_cdf_s = np.arange(1, len(read_slat_sorted) + 1) / len(read_slat_sorted)
write_cdf_s = np.arange(1, len(write_slat_sorted) + 1) / len(write_slat_sorted)
read_cdf_c = np.arange(1, len(read_clat_sorted) + 1) / len(read_clat_sorted)
write_cdf_c = np.arange(1, len(write_clat_sorted) + 1) / len(write_clat_sorted)


plt.figure(figsize=(10, 6))
plt.plot(read_lat_sorted, read_cdf, label='Total Read Latency CDF', color='darkblue')
plt.xlabel('Latency (ms)')
plt.ylabel('Cumulative Probability')
plt.title('Cumulative Distribution Function: Total Latency')
plt.legend()
plt.grid(True)
plt.savefig('task3_lat_r_cdf.png')
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(write_lat_sorted, write_cdf, label='Total Write Latency CDF', color='darkgreen')
plt.xlabel('Latency (ms)')
plt.ylabel('Cumulative Probability')
plt.title('Cumulative Distribution Function: Total Latency')
plt.legend()
plt.grid(True)
plt.savefig('task3_lat_w_cdf.png')
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(read_clat_sorted, read_cdf_c, label='Completion Read Latency CDF', color='blue')
plt.xlabel('Latency (ms)')
plt.ylabel('Cumulative Probability')
plt.title('Cumulative Distribution Function: Completion Latency')
plt.legend()
plt.grid(True)
plt.savefig('task3_clat_r_cdf.png')
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(write_clat_sorted, write_cdf_c, label='Completion Write Latency CDF', color='green')
plt.xlabel('Latency (ms)')
plt.ylabel('Cumulative Probability')
plt.title('Cumulative Distribution Function: Completion Latency')
plt.legend()
plt.grid(True)
plt.savefig('task3_clat_w_cdf.png')
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(read_slat_sorted, read_cdf_s, label='Submission Read Latency CDF', color='lightblue')
plt.xlabel('Latency (ms)')
plt.ylabel('Cumulative Probability')
plt.title('Cumulative Distribution Function: Submission Latency')
plt.legend()
plt.grid(True)
plt.savefig('task3_slat_r_cdf.png')
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(write_slat_sorted, write_cdf_s, label='Submission Write Latency CDF', color='lightgreen')
plt.xlabel('Latency (ms)')
plt.ylabel('Cumulative Probability')
plt.title('Cumulative Distribution Function: Submission Latency')
plt.legend()
plt.grid(True)
plt.savefig('task3_slat_w_cdf.png')
plt.show()