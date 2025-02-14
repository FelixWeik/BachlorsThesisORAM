import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

x1 = 1
x2 = 5
x3 = 10
x4 = 25
x5 = 50
x6 = 75
x7 = 100

# Wall Clock Time for Increasing Number of of RDPF-Triples

df_mpz_64 = pd.DataFrame({
    "x":[x1,x2,x3,x4,x5,x6,x7],
    "y":[2.1,3.4,6.7,13.07,26.3,39.72,54.83],
    "Approach": "gmp_mpz_class 64 bit"
})

df_mpz_128 = pd.DataFrame({
    "x":[x1,x2,x3,x4,x5,x6,x7],
    "y":[4.1,5.2,8.5,19.2,36.2,43.12,69.1],
    "Approach":"gmp_mpz_class 128 bit"
})

df_mpz_256 = pd.DataFrame({
    "x":[x1,x2,x3,x4,x5,x6,x7],
    "y":[8.1,9.2,12.13,22.3,37.3,53.2,86.2],
    "Approach":"gmp_mpz_class 256 bit"
})

df_base = pd.DataFrame({
    "x":[x1,x2,x3,x4,x5,x6,x7],
    "y":[0.044,0.05,0.062,0.06,0.15,0.26,0.23],
    "Approach":"base"
})


plt.figure(figsize=(8,5))

sns.lineplot(data=df_mpz_64, x="x", y="y", hue="Approach", marker="*", linestyle="dashed", palette=["#ff6666"])
sns.lineplot(data=df_mpz_128, x="x", y="y", hue="Approach", marker="*", linestyle="dashed", palette=["#cc0000"])
sns.lineplot(data=df_mpz_256, x="x", y="y", hue="Approach", marker="*", linestyle="dashed", palette=["#800000"])

sns.lineplot(data=df_base, x="x", y="y", hue="Approach", marker=".", linestyle="dotted", palette=["Green"])

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
sns.set_style("ticks")
plt.grid(axis="y")
plt.grid(axis="x")
plt.xlabel("Number of generated RDPF-Triples")
plt.ylabel("Wall Clock Time (s)")
plt.savefig("wall_clock_incnum_preproc.png", bbox_inches="tight")