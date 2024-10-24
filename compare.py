import scipy.stats as stats
import pandas as pd


# task1 read-write
read_bw = []  
write_bw = []
write_file = f'compare/task1_rw.txt'

for k in [0, 12, 25, 38, 50, 63, 75, 88, 100]:
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

    read_bw.append(temp_read_bw)
    write_bw.append(temp_write_bw)

print(f"Read bandwidth (task1):", read_bw)
print(f"Write bandwidth (task1):", write_bw)

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
read_bw = []  
write_bw = []
write_file = f'compare/task1_randrw.txt'

for k in [0, 12, 25, 38, 50, 63, 75, 88, 100]:
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
        
        read_bw.append(temp_read_bw)
        write_bw.append(temp_write_bw)
        
print(f"Read bandwidth (task1 random):", read_bw)
print(f"Write bandwidth (task1 random):", write_bw)

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
read_bw = []  
write_bw = []
write_file = f'compare/task2.txt'

for k in [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]:
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
        
        read_bw.append(temp_read_bw)
        write_bw.append(temp_write_bw)

print(f"Read bandwidth (task2):", read_bw)
print(f"Write bandwidth (task2):", write_bw)

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
read_bw = []  
write_bw = []
write_file = f'compare/task4.txt'

for k in [1, 2, 4, 6, 8]:
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
        
        read_bw.append(temp_read_bw)
        write_bw.append(temp_write_bw)
        
print(f"Read bandwidth (task4):", read_bw)
print(f"Write bandwidth (task4):", write_bw)

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


# task3
read_bw = []  
write_bw = []
write_file = f'compare/task3.txt'

for k in [4, 16, 64]:
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
        
        read_bw.append(temp_read_bw)
        write_bw.append(temp_write_bw)

    for i in [1, 2, 3, 4, 5]:
        read_file = f'data/task3_rep{i}_bw.1.log'

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
        
        read_bw.append(temp_read_bw)
        write_bw.append(temp_write_bw)

print(f"Read bandwidth (task3):", read_bw)
print(f"Write bandwidth (task3):", write_bw)

if len(read_bw) >= 2 and len(write_bw) >=2:
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
    print(f"Not enough data for ANOVA (task3)")