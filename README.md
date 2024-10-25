# set the max performance:
```bash
sudo cpufreq-set -r -g performance
```

# run tests:
```bash
chmod +x run_all_tasks.sh
./run_all_tasks.sh
```

# validate test values:
- use `ANOVA`to compare results among different tests (in the same comdition): `F-value` should be small (close to 1), `P-value` should be greater than `0.05`.
```bash
python3 same_cond.py
```

# once test values valid, compare results in different conditions:
- `ANOVA` again, but if the considered condition does have influence on our results, the `F-value`should be great and the `P-value`should be less than `0.05`
```bash
# combine test1 to test5 in the same line
python3 compare.py
# compare each test separately
python3 compare_s.py
```

# calculate mean value and standard deviation, find median value, and apply the linear regression, then plot
```bash
python3 plot.py
```




