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
# constant depth (15) and constant number of generated rdpf-triples (50)

df_mpz_64 = pd.DataFrame({
    "x":[x1,x2,x3,x4,x5, x6, x7, x8],
    "y":[19.7,19.821,21.06,22.81,22.15,47.16,90.57,152.73],
    "Approach":"gmp_mpz_class 64 bit"
})

df_mpz_128 = pd.DataFrame({
    "x":[x1,x2,x3,x4,x5, x6, x7, x8],
    "y":[19.9,20.66,24.07,24.7,27.125,53.160,120.610,174.94],
    "Approach":"gmp_mpz_class 128 bit"
})

df_mpz_256 = pd.DataFrame({
    "x":[x1,x2,x3,x4,x5, x6, x7, x8],
    "y":[24.02,25.01,27.12,28.472,34.802,71.819,147.734,205.735],
    "Approach":"gmp_mpz_class 256 bit"
})

df_base = pd.DataFrame({
    "x":[x1,x2,x3,x4,x5, x6, x7, x8],
    "y":[0.07,0.162,0.260,0.374,0.504,4.923,6.265,7.522],
    "Approach":"base"
})

df_new_input_type = pd.DataFrame({
    "x":[x1,x2,x3,x4,x5, x6, x7, x8],
    "y":[8.594,8.625,8.638,8.646,8.680,9.953,11.101,12.491],
    "Approach":"new_input_type (200 RDPF-Triples)"
})

plt.figure(figsize=(8,5))

sns.lineplot(data=df_mpz_64, x="x", y="y", hue="Approach", marker="*", linestyle="dashed", palette=["#ff6666"])
sns.lineplot(data=df_mpz_128, x="x", y="y", hue="Approach", marker="*", linestyle="dashed", palette=["#cc0000"])
sns.lineplot(data=df_mpz_256, x="x", y="y", hue="Approach", marker="*", linestyle="dashed", palette=["#800000"])

sns.lineplot(data=df_base, x="x", y="y", hue="Approach", marker=".", linestyle="dotted", palette=["Green"])

sns.lineplot(data=df_new_input_type, x="x", y="y", hue="Approach", marker="o", linestyle="dashed", palette=["#66b3ff"])

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
sns.set_style("ticks")
plt.grid(axis="y")
plt.grid(axis="x")
plt.xlabel("Latency (ms)")
plt.ylabel("Wall Clock Time (s)")
plt.savefig("time_decreasing_latency_preproc.png", bbox_inches="tight")