import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Preproc Storage Requirements

x1 = 3
x2 = 5
x3 = 10
x4 = 15
x5 = 20

y1 = 1.579
y2 = 1.6966
y3 = 1.7308
y4 = 1.8307
y5 = 3.58326


df0 = pd.DataFrame({
    "x":[x1,x2,x3,x4, x5],
    "y":[y1,y2,y3,y4, y5],
    "Approach": "new_input_type"
})

df_base = pd.DataFrame({
    "x":[x1,x2,x3,x4, x5],
    "y":[y1,y2,y3,y4, y5],
    "Approach": "base"
})

y1 = 1.5568
y2 = 1.5957
y3 = 1.6233
y4 = 2.1463
y5 = 4.0214

df3 = pd.DataFrame({
    "x":[x1,x2,x3,x4, x5],
    "y":[y1,y2,y3,y4, y5],
    "Approach": "gmp_mpz_class 64 bit"
})

y1 = 1.9621
y2 = 1.98335
y3 = 2.33319
y4 = 2.495239
y5 = 4.96041

df4 = pd.DataFrame({
    "x":[x1,x2,x3,x4, x5],
    "y":[y1,y2,y3,y4, y5],
    "Approach": "gmp_mpz_class 128 bit"
})

y1 = 2.4118
y2 = 2.4395
y3 = 2.675159
y4 = 2.833388
y5 = 5.321

df5 = pd.DataFrame({
    "x":[x1,x2,x3,x4, x5],
    "y":[y1,y2,y3,y4, y5],
    "Approach": "gmp_mpz_class 256 bit"
})

plt.figure(figsize=(8,5))
sns.lineplot(data=df0, x="x", y="y", hue="Approach", marker="o", linestyle="dashed", palette=["#66b3ff"])

sns.lineplot(data=df3, x="x", y="y", hue="Approach", marker="*", linestyle="dashed", palette=["#ff6666"])
sns.lineplot(data=df4, x="x", y="y", hue="Approach", marker="*", linestyle="dashed", palette=["#cc0000"])
sns.lineplot(data=df5, x="x", y="y", hue="Approach", marker="*", linestyle="dashed", palette=["#800000"])

sns.lineplot(data=df_base, x="x", y="y", hue="Approach", marker=".", linestyle="dotted", palette=["Green"])

sns.set_style("ticks")
plt.grid(axis="y")
plt.grid(axis="x")
plt.xticks(range(3, 21, 1))
plt.xlabel("Depth")
plt.ylabel("Storage Requirement (GiB)")
plt.savefig("storage_requirements_preproc.png")