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

# Wallclock time for decreasing bandwidth (x), constant latency (1ms), 
# constant depth (15) and constant number of generated rdpf-triples (50)

# Note that the lamport clock stays constant

df_mpz_64 = pd.DataFrame({
    "x":[x1,x2,x3,x4,x5,x6,x7],
    "y":[6.256,7.115,6.983,7.815,43.509,453.790,876.383],
    "Approach":"gmp_mpz_class 64 bit"
}) # lamport clock constant at 153

df_mpz_128 = pd.DataFrame({
    "x":[x1,x2,x3,x4,x5,x6,x7],
    "y":[8.672,7.652,8.950,9.100,56.100,532.954,943.711],
    "Approach":"gmp_mpz_class 128 bit"
})

df_mpz_256 = pd.DataFrame({
    "x":[x1,x2,x3,x4,x5,x6,x7],
    "y":[14.012,13.11,14.721,13.945,71.346,569.741,1030.927],
    "Approach":"gmp_mpz_class 256 bit"
})

df_base = pd.DataFrame({
    "x":[x1,x2,x3,x4,x5,x6,x7],
    "y":[1.1,1.012,0.973,1.39,13.897,200.539,299.148],
    "Approach":"base"
})

df_new_input_type = pd.DataFrame({
    "x":[x1,x2,x3,x4,x5,x6,x7],
    "y":[0.912,1.012,0.874,1.382,14.021,198.539,301.211],
    "Approach":"new_input_type"
})

plt.figure(figsize=(8,5))

sns.lineplot(data=df_mpz_64, x="x", y="y", hue="Approach", marker="*", linestyle="dashed", palette=["#ff6666"])
sns.lineplot(data=df_mpz_128, x="x", y="y", hue="Approach", marker="*", linestyle="dashed", palette=["#cc0000"])
sns.lineplot(data=df_mpz_256, x="x", y="y", hue="Approach", marker="*", linestyle="dashed", palette=["#800000"])

sns.lineplot(data=df_base, x="x", y="y", hue="Approach", marker=".", linestyle="dotted", palette=["Green"])

sns.lineplot(data=df_new_input_type, x="x", y="y", hue="Approach", marker="o", linestyle="dashed", palette=["#66b3ff"])

sns.set_style("ticks")
plt.grid(axis="y")
plt.grid(axis="x")
plt.xlabel("Bandwidth (kbit/s)")
plt.ylabel("Wall Clock Time (s)")
plt.savefig("time_decreasing_bandwidth_preproc.png")