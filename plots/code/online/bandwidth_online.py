import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

x1 = 1500
x2 = 1250
x3 = 1000
x4 = 750
x5 = 100
x6 = 10
x7 = 5

# Wallclock Time for decreasing bandwidth, constant latency (1ms),
# constant depth (15) and constant number of retreived itemas (1)

##### READ ####

df_base = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5,x6,x7],
    "y": [0.038,0.038,0.039,0.038,0.073,1.044,1.459],
    "Approach": "base"
})

df_mpz_64 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5,x6,x7],
    "y": [24.986,25.177,26.484,23.902,24.834,30.064,38.071],
    "Approach": "gmp_mpz_class 64 bit"
})

df_mpz_128 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5,x6,x7],
    "y": [41.912,43.108,42.244,41.792,43.805,51.91,56.108],
    "Approach": "gmp_mpz_class 128 bit"
})

df_mpz_256 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5,x6,x7],
    "y": [59.59,57.731,58.9,61.623,59.709,69.796,71.715],
    "Approach": "gmp_mpz_class 256 bit"
})

df_nit_64 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5,x6,x7],
    "y": [0.038,0.038,0.039,0.038,0.834,38.064,48.071],
    "Approach": "new_input_type 64 bit"
})

df_nit_128 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5,x6,x7],
    "y": [0.071,0.068,0.074,0.069,0.805,56.91,65.108],
    "Approach": "new_input_type 128 bit"
})

df_nit_256 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5,x6,x7],
    "y": [0.152,0.144,0.149,0.15,0.709,79.796,84.715],
    "Approach": "new_input_type 256 bit"
})

plt.figure(figsize=(8,5))

sns.lineplot(data=df_mpz_64, x="x", y="y", hue="Approach", marker="*", linestyle="dashed", palette=["#ff6666"])
sns.lineplot(data=df_mpz_128, x="x", y="y", hue="Approach", marker="*", linestyle="dashed", palette=["#cc0000"])
sns.lineplot(data=df_mpz_256, x="x", y="y", hue="Approach", marker="*", linestyle="dashed", palette=["#800000"])

sns.lineplot(data=df_base, x="x", y="y", hue="Approach", marker=".", linestyle="dotted", palette=["Green"])

sns.lineplot(data=df_nit_64, x="x", y="y", hue="Approach", marker="o", linestyle="dashed", palette=["#66b3ff"])
sns.lineplot(data=df_nit_128, x="x", y="y", hue="Approach", marker="o", linestyle="dashed", palette=["#3b8acc"])
sns.lineplot(data=df_nit_256, x="x", y="y", hue="Approach", marker="o", linestyle="dashed", palette=["#3380cc"])

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(axis="y")
plt.grid(axis="x")
plt.xlabel("Bandwidth (kbit/s)")
plt.ylabel("Wall Clock Time (s)")
plt.savefig("wct_bandwidth_read_online.png", bbox_inches="tight")

##### UPDATE #####

df_base = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5,x6,x7],
    "y": [0.041,0.041,0.044,0.041,0.092,1.138,2.651],
    "Approach": "base"
})

df_mpz_64 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5,x6,x7],
    "y": [35.1,34.502,36.466,31.758,33.409,39.201,42.166],
    "Approach": "gmp_mpz_class 64 bit"
})

df_mpz_128 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5,x6,x7],
    "y": [48.765,49.123,48.855,49.871,53.7,62.163,69.129],
    "Approach": "gmp_mpz_class 128 bit"
})

df_mpz_256 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5,x6,x7],
    "y": [68.150,67.629,67.726,68.325,79.12,85.368,91.441],
    "Approach": "gmp_mpz_class 256 bit"
})

df_nit_64 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5,x6,x7],
    "y": [0.039,0.041,0.042,0.046,0.409,41.201,47.166],
    "Approach": "new_input_type 64 bit"
})

df_nit_128 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5,x6,x7],
    "y": [0.052,0.049,0.052,0.049,0.7,67.163,76.129],
    "Approach": "new_input_type 128 bit"
})

df_nit_256 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5,x6,x7],
    "y": [0.091,0.086,0.093,0.091,0.12,89.368,98.441],
    "Approach": "new_input_type 256 bit"
})

plt.figure(figsize=(8,5))

sns.lineplot(data=df_mpz_64, x="x", y="y", hue="Approach", marker="*", linestyle="dashed", palette=["#ff6666"])
sns.lineplot(data=df_mpz_128, x="x", y="y", hue="Approach", marker="*", linestyle="dashed", palette=["#cc0000"])
sns.lineplot(data=df_mpz_256, x="x", y="y", hue="Approach", marker="*", linestyle="dashed", palette=["#800000"])

sns.lineplot(data=df_base, x="x", y="y", hue="Approach", marker=".", linestyle="dotted", palette=["Green"])

sns.lineplot(data=df_nit_64, x="x", y="y", hue="Approach", marker="o", linestyle="dashed", palette=["#66b3ff"])
sns.lineplot(data=df_nit_128, x="x", y="y", hue="Approach", marker="o", linestyle="dashed", palette=["#3b8acc"])
sns.lineplot(data=df_nit_256, x="x", y="y", hue="Approach", marker="o", linestyle="dashed", palette=["#3380cc"])

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(axis="y")
plt.grid(axis="x")
plt.xlabel("Bandwidth (kbit/s)")
plt.ylabel("Wall Clock Time (s)")
plt.savefig("wct_bandwidth_update_online.png", bbox_inches="tight")