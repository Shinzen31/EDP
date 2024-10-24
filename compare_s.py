import scipy.stats as stats
import pandas as pd


# task1 read-write
for i in [1, 2, 3, 4, 5]:
    read_bw = []  
    write_bw = []

    for k in [0, 12, 25, 38, 50, 63, 75, 88, 100]:
        read_file = f'data/task1_rw_pct{k}_rep{i}_bw.1.log'
        write_file = f'compare/task1_rw_{i}.txt'

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
for i in [1, 2, 3, 4, 5]:
    read_bw = []  
    write_bw = []

    for k in [0, 12, 25, 38, 50, 63, 75, 88, 100]:
        read_file = f'data/task1_randrw_pct{k}_rep{i}_bw.1.log'
        write_file = f'compare/task1_randrw_{i}.txt'

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
for i in [1, 2, 3, 4, 5]: 
    read_bw = []  
    write_bw = []

    for k in [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]:
        read_file = f'data/task2_bs{k}k_rep{i}_bw.1.log'
        write_file = f'compare/task2_{i}.txt'

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
for i in [1, 2, 3, 4, 5]:
    read_bw = []  
    write_bw = []
    
    for k in [1, 2, 4, 6, 8]:
        read_file = f'data/task4_numjobs{k}_rep{i}_bw.1.log'
        write_file = f'compare/task4_{i}.txt'

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
for i in [1, 2, 3, 4, 5]: 
    read_bw = []  
    write_bw = []

    for k in [4, 16, 64]:
        read_file1 = f'data/task2_bs{k}k_rep{i}_bw.1.log'
        read_file2 = f'data/task3_rep{i}_bw.1.log'
        write_file = f'compare/task3_bw_{i}.txt'

        try:
            df1 = pd.read_csv(read_file1, header=None)
            df2 = pd.read_csv(read_file2, header=None)

            temp_read_bw = []
            temp_write_bw = []

            for index, row in df1.iterrows():
                if row[2] == 0:  
                    temp_read_bw.append(row[1])  
                elif row[2] == 1:  
                    temp_write_bw.append(row[1])  
            for index, row in df2.iterrows():
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



    

 


