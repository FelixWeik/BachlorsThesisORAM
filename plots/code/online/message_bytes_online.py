import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

x1 = 1
x2 = 2
x3 = 3
x4 = 4
x5 = 5 

# Number of message bytes sent for increasing number of retrieved / updated items
# bandwidth (100mbit) and latency (1ms) are constant;
# 50 RDPF-Triples have been generated

##### READ #####

df_base = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5],
    "y": [8, 12, 16, 20, 24],
    "Approach": "base"
})

df_mpz_64 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5],
    "y": [4,8,12,16,20],
    "Approach": "gmp_mpz_class 64 bit"
})

df_mpz_128 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5],
    "y": [8,16,24,32,40],
    "Approach": "gmp_mpz_class 128 bit"
})

df_mpz_256 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5],
    "y": [16,32,48,64,80],
    "Approach": "gmp_mpz_class 256 bit"
})

df_nit_64 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5],
    "y": [8, 12, 16, 20, 24],
    "Approach": "new_input_type 64 bit"
})

df_nit_128 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5],
    "y": [16,24,32,40,48],
    "Approach": "new_input_type 128 bit"
})

df_nit_256 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5],
    "y": [32,48,64,80,96],
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
plt.xticks([x1, x2, x3, x4, x5])
plt.xlabel("Number of retrieved Items")
plt.ylabel("Number of sent Message Bytes")
plt.savefig("message_bytes_read_online.png", bbox_inches="tight")

##### UPDATE #####

df_base = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5],
    "y": [4,6,8,10,12],
    "Approach": "base"
})

df_mpz_64 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5],
    "y": [12,24,36,48,60],
    "Approach": "gmp_mpz_class 64 bit"
})

df_mpz_128 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5],
    "y": [24,48,72,96,120],
    "Approach": "gmp_mpz_class 128 bit"
})

df_mpz_256 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5],
    "y": [48,96,142,192,240],
    "Approach": "gmp_mpz_class 256 bit"
})

df_nit_64 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5],
    "y": [4,6,8,10,12],
    "Approach": "new_input_type 64 bit"
})

df_nit_128 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5],
    "y": [8,12,16,20,24],
    "Approach": "new_input_type 128 bit"
})

df_nit_256 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5],
    "y": [16,24,32,40,48],
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
plt.xticks([x1, x2, x3, x4, x5])
plt.xlabel("Number of updated Items")
plt.ylabel("Number of sent Message Bytes")
plt.savefig("message_bytes_update_online.png", bbox_inches="tight")