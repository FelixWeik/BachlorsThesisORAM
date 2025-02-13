import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


x1 = 3
x2 = 5
x3 = 10
x4 = 15
x5 = 20

# Lamport Clocks

df_new_input_type = pd.DataFrame({
    "x":[x1,x2,x3,x4,x5],
    "y":[8,12,22,32,42],
    "Approach":"new_input_type (200 RDPF-Triples)"
})

df_gmp_mpz_class = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5],
    "y":[33,53,103,153,203],
    "Approach": "gmp_mpz_class"
})

df_base = pd.DataFrame({
    "x":[x1,x2,x3,x4,x5],
    "y":[8,12,22,32,42],
    "Approach":"base"
})

plt.figure(figsize=(8, 5))
sns.lineplot(data=df_new_input_type, x="x", y="y", hue="Approach", marker="o", linestyle="dashed", palette=["Blue"])
sns.lineplot(data=df_gmp_mpz_class, x="x", y="y", hue="Approach", marker="*", linestyle="dashed", palette=["Red"])
sns.lineplot(data=df_base, x="x", y="y", hue="Approach", marker=".", linestyle="dotted", palette=["Green"])

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
sns.set_style("ticks")
plt.grid(axis="y")
plt.grid(axis="x")
plt.xticks(range(3, 21, 1))
plt.xlabel("Depth")
plt.ylabel("Lamport Clock")
plt.savefig("lamport_clock_preproc.png", bbox_inches="tight")