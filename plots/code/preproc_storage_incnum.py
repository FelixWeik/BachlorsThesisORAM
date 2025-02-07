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

# Storage Requirements for Increasing Number of triples at constant depth (15)

df_mpz_64 = pd.DataFrame({
    "x":[x1,x2,x3,x4,x5,x6,x7],
    "y":[2.057, 2.1095, 2.1415, 2.168, 2.159, 2.18729, 2.217],
    "Approach": "gmp_mpz_class 64 bit"
})

df_mpz_128 = pd.DataFrame({
    "x":[x1,x2,x3,x4,x5,x6,x7],
    "y":[2.608, 2.701, 2.699, 2.701, 2.809, 2.708, 2.799],
    "Approach":"gmp_mpz_class 128 bit"
})

df_mpz_256 = pd.DataFrame({
    "x":[x1,x2,x3,x4,x5,x6,x7],
    "y":[2.981, 2.999, 3.07, 2.899, 2.901, 2.99, 3.091],
    "Approach":"gmp_mpz_class 256 bit"
})

df_base = pd.DataFrame({
    "x":[x1,x2,x3,x4,x5,x6,x7],
    "y":[1.98, 1.8592, 1.9581, 1.9578, 2.012, 1.905, 1.986],
    "Approach":"base"
})

df_new_input_type = pd.DataFrame({
    "x":[x1,x2,x3,x4,x5,x6,x7],
    "y":[1.92, 1.9592, 2.0581, 1.89578, 1.912, 1.805, 2.016],
    "Approach":"new_input_type"
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
plt.xlabel("Number of generated RDPF-Triples")
plt.ylabel("Storage Requirement (GiB)")
plt.savefig("storage_incnum_preproc.png", bbox_inches="tight")