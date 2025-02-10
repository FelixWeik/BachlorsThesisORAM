import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

x1 = 1
x2 = 2.5
x3 = 5
x4 = 7.5
x5 = 10
x6 = 50
x7 = 75
x8 = 100

# Wallclock time for decreasing latency (x), constant bandwidth (100mbit),
# constant depth (15), and constant number of retrieved / updated items (1)
# 50 rdpf triples have been generated before

##### READ #####

df_base = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5,x6,x7,x8],
    "y": [0.011,0.052,0.084,0.113,0.144,0.628,0.928,1.23],
    "Approach": "base"
})

df_mpz_64 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5,x6,x7,x8],
    "y": [24.986,24.403,25.698,27.053,25.244,26.918,29.150,39.475],
    "Approach": "gmp_mpz_class 64 bit"
})

df_mpz_128 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5,x6,x7,x8],
    "y": [41.912,42.058,42.002,45.125,46.921,49.51,56.105,65.765],
    "Approach": "gmp_mpz_class 128 bit"
})

df_mpz_256 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5,x6,x7,x8],
    "y": [59.59,58.96,58.892,64.716,63.716,66.671,81.725,91.12],
    "Approach": "gmp_mpz_class 256 bit"
})

df_nit_64 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5,x6,x7,x8],
    "y": [0.011,0.052,0.084,0.113,0.144,0.628,0.928,1.23],
    "Approach": "new_input_type 64 bit"
})

df_nit_128 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5,x6,x7,x8],
    "y": [0.056,0.087,0.142,0.178,0.243,0.896,1.342,1.629],
    "Approach": "new_input_type 128 bit"
})

df_nit_256 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5,x6,x7,x8],
    "y": [0.132,0.189,0.243,0.289,0.489,1.32,1.698,2.198],
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
sns.set_style("ticks")
plt.grid(axis="y")
plt.grid(axis="x")
plt.xlabel("Latency (ms)")
plt.ylabel("Wall Clock Time (s)")
plt.savefig("wct_latency_read_online.png", bbox_inches="tight")

##### UPDATE #####

df_base = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5,x6,x7,x8],
    "y": [0.027,0.062,0.095,0.129,0.161,0.601,0.901,1.201],
    "Approach": "base"
})

df_mpz_64 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5,x6,x7,x8],
    "y": [35.1,33.418,33.557,34.185,33.058,35.028,41.725,48.279],
    "Approach": "gmp_mpz_class 64 bit"
})

df_mpz_128 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5,x6,x7,x8],
    "y": [48.765,49.12,49.051,51.122,50.928,56.194,60.12,78.785],
    "Approach": "gmp_mpz_class 128 bit"
})

df_mpz_256 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5,x6,x7,x8],
    "y": [68.15,68.2,67.915,73.125,74.261,76.921,79.153,95.681],
    "Approach": "gmp_mpz_class 256 bit"
})

df_nit_64 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5,x6,x7,x8],
    "y": [0.027,0.062,0.095,0.129,0.161,0.601,0.901,1.201],
    "Approach": "new_input_type 64 bit"
})

df_nit_128 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5,x6,x7,x8],
    "y": [0.047,0.12,0.195,0.229,0.361,0.801,1.201,1.801],
    "Approach": "new_input_type 128 bit"
})

df_nit_256 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5,x6,x7,x8],
    "y": [0.147,0.21,0.245,0.349,0.541,0.911,1.801,2.601],
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
sns.set_style("ticks")
plt.grid(axis="y")
plt.grid(axis="x")
plt.xlabel("Latency (ms)")
plt.ylabel("Wall Clock Time (s)")
plt.savefig("wct_latency_update_online.png", bbox_inches="tight")