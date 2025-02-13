import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

x1 = 3
x2 = 5
x3 = 10
x4 = 15
x5 = 20

# Wall Clock Time Preproc

df_new_input_type = pd.DataFrame({
    "x":[x1,x2,x3,x4, x5],
    "y":[15,17,20,25,32],
    "Approach": "new_input_type (200 RDPF-Triples)"
})

df_base = pd.DataFrame({
    "x":[x1,x2,x3,x4, x5],
    "y":[5,7,10,12,15],
    "Approach": "base"
})

df_mpz_class_64 = pd.DataFrame({
    "x":[x1,x2,x3,x4, x5],
    "y":[60,67,82,91,103],
    "Approach": "gmp_mpz_class 64 bit"
})

df_mpz_class_128 = pd.DataFrame({
    "x":[x1,x2,x3,x4, x5],
    "y":[83,97,113,135,158],
    "Approach": "gmp_mpz_class 128 bit"
})

df_mpz_class_256 = pd.DataFrame({
    "x":[x1,x2,x3,x4, x5],
    "y":[97,109,138,158,178],
    "Approach": "gmp_mpz_class 256 bit"
})

plt.figure(figsize=(8, 5))

sns.lineplot(data=df_new_input_type, x="x", y="y", hue="Approach", marker="o", linestyle="dashed", palette=["#66b3ff"])

sns.lineplot(data=df_mpz_class_64, x="x", y="y", hue="Approach", marker="*", linestyle="dashed", palette=["#ff6666"])
sns.lineplot(data=df_mpz_class_128, x="x", y="y", hue="Approach", marker="*", linestyle="dashed", palette=["#cc0000"])
sns.lineplot(data=df_mpz_class_256, x="x", y="y", hue="Approach", marker="*", linestyle="dashed", palette=["#800000"])

sns.lineplot(data=df_base, x="x", y="y", hue="Approach", marker=".", linestyle="dotted", palette=["Green"])

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
sns.set_style("ticks")
plt.grid(axis="y")
plt.grid(axis="x")
plt.xticks(range(3, 21, 1))
plt.xlabel("Depth")
plt.ylabel("Number of sent Messages")
plt.savefig("sent_messages_preproc.png", bbox_inches="tight")