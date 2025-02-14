import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

x1 = 1
x2 = 2
x3 = 3
x4 = 4
x5 = 5

# Number of messages sent for increasing number of retrieved / updated items,
# bandwidth (100mbit) and latency (1ms) are constant;
# 50 RDPF-Triples have been generated before 

##### READ #####

df_base = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5],
    "y": [4,6,8,10,12],
    "Approach": "base"
})

df_mpz_64 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5],
    "y": [12,18,22,26,30],
    "Approach": "gmp_mpz_class 64 bit"
})

df_mpz_128 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5],
    "y": [26,30,34,38,42],
    "Approach": "gmp_mpz_class 128 bit"
})

df_mpz_256 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5],
    "y": [54,58,62,66,70],
    "Approach": "gmp_mpz_class 256 bit"
})

df_nit_64 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5],
    "y": [4,6,8,10,12],
    "Approach": "new_input_type 64 bit"
})

df_nit_128 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5],
    "y": [8,10,12,14,16],
    "Approach": "new_input_type 128 bit"
})

df_nit_256 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5],
    "y": [16,18,20,22,24],
    "Approach": "new_input_type 256 bit"
})

plt.figure(figsize=(8,5))

sns.lineplot(data=df_mpz_64, x="x", y="y", hue="Approach", marker="*", linestyle="dashed", palette=["#ff6666"])
sns.lineplot(data=df_mpz_128, x="x", y="y", hue="Approach", marker="*", linestyle="dashed", palette=["#cc0000"])
sns.lineplot(data=df_mpz_256, x="x", y="y", hue="Approach", marker="*", linestyle="dashed", palette=["#800000"])

sns.lineplot(data=df_base, x="x", y="y", hue="Approach", marker=".", linestyle="dotted", palette=["Green"])

sns.lineplot(data=df_nit_64, x="x", y="y", hue="Approach", marker="o", linestyle="dashed", palette=["#66b3ff"])
sns.lineplot(data=df_nit_128, x="x", y="y", hue="Approach", marker="o", linestyle="dashed", palette=["#4d9ae6"])
sns.lineplot(data=df_nit_256, x="x", y="y", hue="Approach", marker="o", linestyle="dashed", palette=["#3380cc"])

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
sns.set_style("ticks")
plt.grid(axis="y")
plt.grid(axis="x")
plt.xticks([x1, x2, x3, x4, x5])
plt.xlabel("Number of retrieved Items")
plt.ylabel("Number of sent Messages")
plt.savefig("message_num_read_online.png", bbox_inches="tight")

##### UPDATE #####

df_base = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5],
    "y": [4,6,8,10,12],
    "Approach": "base"
})

df_mpz_64 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5],
    "y": [12,16,20,24,28],
    "Approach": "gmp_mpz_class 64 bit"
})

df_mpz_128 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5],
    "y": [20, 24, 28, 32, 36],
    "Approach" : "gmp_mpz_class 128 bit"
})

df_mpz_256 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5],
    "y": [38,42,46,50,54],
    "Approach": "gmp_mpz_class 256 bit"
})

df_nit_64 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5],
    "y": [4,6,8,10,12],
    "Approach": "new_input_type 64 bit"
})

df_nit_128 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5],
    "y": [8,10,12,14,16],
    "Approach": "new_input_type 128 bit"
})

df_nit_256 = pd.DataFrame({
    "x": [x1,x2,x3,x4,x5],
    "y": [16,18,20,22,24],
    "Approach": "new_input_type 256 bit"
})

plt.figure(figsize=(8,5))

sns.lineplot(data=df_mpz_64, x="x", y="y", hue="Approach", marker="*", linestyle="dashed", palette=["#ff6666"])
sns.lineplot(data=df_mpz_128, x="x", y="y", hue="Approach", marker="*", linestyle="dashed", palette=["#cc0000"])
sns.lineplot(data=df_mpz_256, x="x", y="y", hue="Approach", marker="*", linestyle="dashed", palette=["#800000"])

sns.lineplot(data=df_base, x="x", y="y", hue="Approach", marker=".", linestyle="dotted", palette=["Green"])

sns.lineplot(data=df_nit_64, x="x", y="y", hue="Approach", marker="o", linestyle="dashed", palette=["#66b3ff"])
sns.lineplot(data=df_nit_128, x="x", y="y", hue="Approach", marker="o", linestyle="dashed", palette=["#4d9ae6"])
sns.lineplot(data=df_nit_256, x="x", y="y", hue="Approach", marker="o", linestyle="dashed", palette=["#3380cc"])

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
sns.set_style("ticks")
plt.grid(axis="y")
plt.grid(axis="x")
plt.xticks([x1, x2, x3, x4, x5])
plt.xlabel("Number of updated Items")
plt.ylabel("Number of sent Messages")
plt.savefig("message_num_update_online.png", bbox_inches="tight")