import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

x1 = 3
x2 = 5
x3 = 10
x4 = 15
x5 = 20


df_base = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5],
    "y": [2100,9300,306900,9830100,314572500],
    "Approach": "base"
})

df_mpz_64 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5],
    "y": [4800,19200,614400,19361400,628147500],
    "Approach": "gmp_mpz_class 64 bit"
})

df_mpz_128 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5],
    "y": [5400,19800,615000,19661400,629146200],
    "Approach": "gmp_mpz_class 128 bit"
})

df_mpz_256 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5],
    "y": [6900,21300,616500,1962900,629257700],
    "Approach": "gmp_mpz_class 256 bit"
})

df_nit = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5],
    "y": [2100,9300,306900,9830100,314572500],
    "Approach": "new_input_type"
})

sns.lineplot(data=df_mpz_64, x="x", y="y", hue="Approach", marker="*", linestyle="dashed", palette=["#ff6666"])
sns.lineplot(data=df_mpz_128, x="x", y="y", hue="Approach", marker="*", linestyle="dashed", palette=["#cc0000"])
sns.lineplot(data=df_mpz_256, x="x", y="y", hue="Approach", marker="*", linestyle="dashed", palette=["#800000"])

sns.lineplot(data=df_base, x="x", y="y", hue="Approach", marker=".", linestyle="dotted", palette=["Green"])

sns.lineplot(data=df_nit, x="x", y="y", hue="Approach", marker="o", linestyle="dashed", palette=["#66b3ff"])

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
sns.set_style("ticks")
plt.xticks(range(3,21))
plt.grid(axis="y")
plt.grid(axis="x")
plt.xlabel("Depth")
plt.ylabel("Number of AES-Operations")
plt.savefig("aes_ops_preproc.png", bbox_inches="tight")