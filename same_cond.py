import scipy.stats as stats
import pandas as pd

reps = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# task1 read-write
for k in [0, 12, 25, 38, 50, 63, 75, 88, 100]:
    read_bw = []  
    write_bw = []

    for i in reps:
        read_file = f'data/task1_rw_pct{k}_rep{i}_bw.1.log'
        write_file = f'valid/task1_rw_pct{k}.txt'

        try:
            df = pd.read_csv(read_file, header=None)

            temp_read_bw = []
            temp_write_bw = []

            for index, row in df.iterrows():
                if row[2] == 0:  
                    temp_read_bw.append(row[1])  
                elif row[2] == 1:  
                    temp_write_bw.append(row[1])  

            read_bw.append(temp_read_bw)
            write_bw.append(temp_write_bw)
            # print(f"Read bandwidth (task1, rep {i}):", read_bw[-1])
            # print(f"Write bandwidth (task1, rep {i}):", write_bw[-1])

        except FileNotFoundError:
            print(f"File {read_file} not found")
            continue


    if len(read_bw) >= 2 and len(write_bw) >= 2:
        try:
            f_statistic_r, p_value_r = stats.f_oneway(*read_bw)
            f_statistic_w, p_value_w = stats.f_oneway(*write_bw)
            with open(write_file, 'w') as f:
                print(f"F-statistic for read bandwidth (task1): {f_statistic_r}", file=f)
                print(f"P-value for read bandwidth (task1): {p_value_r}", file=f)
                print(f"F-statistic for write bandwidth (task1): {f_statistic_w}", file=f)
                print(f"P-value for read bandwidth (task1): {p_value_w}", file=f)
        except ValueError as e:
            print(f"Error in ANOVA: {e}")
    else:
        print(f"Not enough data for ANOVA (task1 r-w) ")


# task1 random read-write
for k in [0, 12, 25, 38, 50, 63, 75, 88, 100]:
    read_bw = []  
    write_bw = []

    for i in reps:
        read_file = f'data/task1_randrw_pct{k}_rep{i}_bw.1.log'
        write_file = f'valid/task1_randrw_pct{k}.txt'

        try:
            df = pd.read_csv(read_file, header=None)

            temp_read_bw = []
            temp_write_bw = []

            for index, row in df.iterrows():
                if row[2] == 0:  
                    temp_read_bw.append(row[1])  
                elif row[2] == 1:  
                    temp_write_bw.append(row[1])  

            read_bw.append(temp_read_bw)
            write_bw.append(temp_write_bw)
            # print(f"Read bandwidth (task1, rep {i}):", read_bw[-1])
            # print(f"Write bandwidth (task1, rep {i}):", write_bw[-1])

        except FileNotFoundError:
            print(f"File {read_file} not found")
            continue


    if len(read_bw) >= 2 and len(write_bw) >= 2:
        try:
            f_statistic_r, p_value_r = stats.f_oneway(*read_bw)
            f_statistic_w, p_value_w = stats.f_oneway(*write_bw)
            with open(write_file, 'w') as f:
                print(f"F-statistic for read bandwidth (task1): {f_statistic_r}", file=f)
                print(f"P-value for read bandwidth (task1): {p_value_r}", file=f)
                print(f"F-statistic for write bandwidth (task1): {f_statistic_w}", file=f)
                print(f"P-value for read bandwidth (task1): {p_value_w}", file=f)
        except ValueError as e:
            print(f"Error in ANOVA: {e}")
    else:
        print(f"Not enough data for ANOVA (task1 random r-w)")

        
# task2
for k in [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]:
    read_bw = []  
    write_bw = []

    for i in reps:
        read_file = f'data/task2_bs{k}k_rep{i}_bw.1.log'
        write_file = f'valid/task2_{k}k.txt'

        try:
            df = pd.read_csv(read_file, header=None)

            temp_read_bw = []
            temp_write_bw = []

            for index, row in df.iterrows():
                if row[2] == 0:  
                    temp_read_bw.append(row[1])  
                elif row[2] == 1:  
                    temp_write_bw.append(row[1])  

            read_bw.append(temp_read_bw)
            write_bw.append(temp_write_bw)
            # print(f"Read bandwidth (task2, rep {i}):", read_bw[-1])
            # print(f"Write bandwidth (task2, rep {i}):", write_bw[-1])

        except FileNotFoundError:
            print(f"File {read_file} not found")
            continue


    if len(read_bw) >= 2 and len(write_bw) >=2:
        try:
            f_statistic_r, p_value_r = stats.f_oneway(*read_bw)
            f_statistic_w, p_value_w = stats.f_oneway(*write_bw)
            with open(write_file, 'w') as f:
                print(f"F-statistic for read bandwidth (task2): {f_statistic_r}", file=f)
                print(f"P-value for read bandwidth (task2): {p_value_r}", file=f)
                print(f"F-statistic for write bandwidth (task2): {f_statistic_w}", file=f)
                print(f"P-value for read bandwidth (task2): {p_value_w}", file=f)
        except ValueError as e:
            print(f"Error in ANOVA: {e}")
    else:
        print(f"Not enough data for ANOVA (task2)")
         
         

# task4
for k in [1, 2, 4, 6, 8]:
    read_bw = []  
    write_bw = []
    
    for i in reps:
        read_file = f'data/task4_numjobs{k}_rep{i}_bw.1.log'
        write_file = f'valid/task4_numjobs{k}.txt'

        try:
            df = pd.read_csv(read_file, header=None)

            temp_read_bw = []
            temp_write_bw = []

            for index, row in df.iterrows():
                if row[2] == 0:  
                    temp_read_bw.append(row[1])  
                elif row[2] == 1:  
                    temp_write_bw.append(row[1])  

            read_bw.append(temp_read_bw)
            write_bw.append(temp_write_bw)
            # print(f"Read bandwidth (task4, rep {i}):", read_bw[-1])
            # print(f"Write bandwidth (task4, rep {i}):", write_bw[-1])

        except FileNotFoundError:
            print(f"File {read_file} not found")
            continue


    if len(read_bw) >= 2 and len(write_bw) >= 2:
        try:
            f_statistic_r, p_value_r = stats.f_oneway(*read_bw)
            f_statistic_w, p_value_w = stats.f_oneway(*write_bw)
            with open(write_file, 'w') as f:
                print(f"F-statistic for read bandwidth (task4): {f_statistic_r}", file=f)
                print(f"P-value for read bandwidth (task4): {p_value_r}", file=f)
                print(f"F-statistic for write bandwidth (task4): {f_statistic_w}", file=f)
                print(f"P-value for read bandwidth (task4): {p_value_w}", file=f)
        except ValueError as e:
            print(f"Error in ANOVA: {e}")
            
    else:
        print(f"Not enough data for ANOVA (task4 parallel)")
          
          
  
# task3 bandwidth       
read_bw = []  
write_bw = []

for i in reps:
    read_file = f'data/task3_rep{i}_bw.1.log'
    write_file = f'valid/task3_bw.txt'

    try:
        df = pd.read_csv(read_file, header=None)

        temp_read_bw = []
        temp_write_bw = []

        for index, row in df.iterrows():
            if row[2] == 0:  
                temp_read_bw.append(row[1])  
            elif row[2] == 1:  
                temp_write_bw.append(row[1])  

        read_bw.append(temp_read_bw)
        write_bw.append(temp_write_bw)
        # print(f"Read bandwidth (task3, rep {i}):", read_bw[-1])
        # print(f"Write bandwidth (task3, rep {i}):", write_bw[-1])

    except FileNotFoundError:
        print(f"File {read_file} not found")
        continue


if len(read_bw) >= 2 and len(write_bw) >= 2:
    try:
        f_statistic_r, p_value_r = stats.f_oneway(*read_bw)
        f_statistic_w, p_value_w = stats.f_oneway(*write_bw)
        with open(write_file, 'w') as f:
            print(f"F-statistic for read bandwidth (task3): {f_statistic_r}", file=f)
            print(f"P-value for read bandwidth (task3): {p_value_r}", file=f)
            print(f"F-statistic for write bandwidth (task3): {f_statistic_w}", file=f)
            print(f"P-value for read bandwidth (task3): {p_value_w}", file=f)
    except ValueError as e:
        print(f"Error in ANOVA: {e}")
else:
    print(f"Not enough data for ANOVA (task3 bandwidth)")         
 



# task3 total latency
read_lat = []
write_lat = []

for i in reps:
    read_file = f'data/task3_rep{i}_lat.1.log'
    write_file = f'valid/task3_lat.txt'

    try:
        df = pd.read_csv(read_file, header=None)

        temp_read_lat = []
        temp_write_lat = []

        for index, row in df.iterrows():
            if row[2] == 0:  
                temp_read_lat.append(row[1])  
            elif row[2] == 1:  
                temp_write_lat.append(row[1])  

        read_lat.append(temp_read_lat)
        write_lat.append(temp_write_lat)
        # print(f"Read latency (task3, rep {i}):", read_lat[-1])
        # print(f"Write latency (task3, rep {i}):", write_lat[-1])

    except FileNotFoundError:
        print(f"File {read_file} not found")
        continue

if len(read_bw) >= 2 and len(write_bw) >= 2:
    try:
        f_statistic_read, p_value_read = stats.f_oneway(*read_lat)
        f_statistic_write, p_value_write = stats.f_oneway(*write_lat)

        with open(write_file, 'w') as f:
            print(f"F-statistic for read total latency (task3): {f_statistic_read}", file=f)
            print(f"P-value for read total latency (task3): {p_value_read}", file=f)
            print(f"F-statistic for write total latency (task3): {f_statistic_write}", file=f)
            print(f"P-value for write total latency (task3): {p_value_write}", file=f)

    except ValueError as e:
        print(f"Error in ANOVA: {e}")
else:
    print(f"Not enough data for ANOVA (task3 total latency)")


# task3 completion latency
read_lat = []
write_lat = []

for i in reps:
    read_file = f'data/task3_rep{i}_clat.1.log'
    write_file = f'valid/task3_clat.txt'

    try:
        df = pd.read_csv(read_file, header=None)

        temp_read_lat = []
        temp_write_lat = []

        for index, row in df.iterrows():
            if row[2] == 0:  
                temp_read_lat.append(row[1])  
            elif row[2] == 1:  
                temp_write_lat.append(row[1])  

        read_lat.append(temp_read_lat)
        write_lat.append(temp_write_lat)
        # print(f"Read completion latency (task3, rep {i}):", read_lat[-1])
        # print(f"Write completion latency (task3, rep {i}):", write_lat[-1])

    except FileNotFoundError:
        print(f"File {read_file} not found")
        continue

if len(read_lat) >= 2 and len(write_lat) >= 2:
    try:
        f_statistic_read, p_value_read = stats.f_oneway(*read_lat)
        f_statistic_write, p_value_write = stats.f_oneway(*write_lat)

        with open(write_file, 'w') as f:
            print(f"F-statistic for read completion latency (task3): {f_statistic_read}", file=f)
            print(f"P-value for read completion latency (task3): {p_value_read}", file=f)
            print(f"F-statistic for write comletion latency (task3): {f_statistic_write}", file=f)
            print(f"P-value for write completion latency (task3): {p_value_write}", file=f)

    except ValueError as e:
        print(f"Error in ANOVA: {e}")
else:
    print(f"Not enough data for ANOVA (task3 completion latency)")



# task3 submission latency
read_lat = []
write_lat = []

for i in reps:
    read_file = f'data/task3_rep{i}_slat.1.log'
    write_file = f'valid/task3_slat.txt'

    try:
        df = pd.read_csv(read_file, header=None)

        temp_read_lat = []
        temp_write_lat = []

        for index, row in df.iterrows():
            if row[2] == 0:  
                temp_read_lat.append(row[1])  
            elif row[2] == 1:  
                temp_write_lat.append(row[1])  

        read_lat.append(temp_read_lat)
        write_lat.append(temp_write_lat)
        # print(f"Read submission latency (task3, rep {i}):", read_lat[-1])
        # print(f"Write submission latency (task3, rep {i}):", write_lat[-1])

    except FileNotFoundError:
        print(f"File {read_file} not found")
        continue

if len(read_lat) >= 2 and len(write_lat) >= 2:
    try:
        f_statistic_read, p_value_read = stats.f_oneway(*read_lat)
        f_statistic_write, p_value_write = stats.f_oneway(*write_lat)

        with open(write_file, 'w') as f:
            print(f"F-statistic for read submission latency (task3): {f_statistic_read}", file=f)
            print(f"P-value for read submission latency (task3): {p_value_read}", file=f)
            print(f"F-statistic for write submission latency (task3): {f_statistic_write}", file=f)
            print(f"P-value for write submission latency (task3): {p_value_write}", file=f)

    except ValueError as e:
        print(f"Error in ANOVA: {e}")
else:
    print(f"Not enough data for ANOVA (task3 submission latency)")
        