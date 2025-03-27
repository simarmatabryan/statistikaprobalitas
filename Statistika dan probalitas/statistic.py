import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import math

while True:
    print("\n=== PROGRAM STATISTIK DESKRIPTIF ===")

    # ===== INPUT DATA =====
    print("Masukkan data numerik (pisahkan dengan spasi):")
    data = list(map(int, input().split()))

    # ===== a. Mean, Median, Mode =====
    mean = round(np.mean(data), 2)
    median = round(np.median(data), 2)
    mode = round(stats.mode(data, keepdims=True).mode[0], 2)

    print(f"\n[Statistik Dasar]")
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")

    # ===== b. Range, Variance, Standard Deviation =====
    range_val = round(np.max(data) - np.min(data), 2)
    variance = round(np.var(data, ddof=1), 2)
    std_dev = round(np.std(data, ddof=1), 2)

    print(f"\n[Sebaran Data]")
    print(f"Range: {range_val}")
    print(f"Variance: {variance}")
    print(f"Standard Deviation: {std_dev}")

    # ===== c. Frequency Distribution Table =====
    k = int(round(1 + 3.322 * math.log10(len(data))))
    min_val, max_val = min(data), max(data)
    range_class = (max_val - min_val) / k
    bins = [min_val + i * range_class for i in range(k + 1)]
    labels = [f"{round(bins[i], 2)} - {round(bins[i+1], 2)}" for i in range(len(bins) - 1)]
    freq, _ = np.histogram(data, bins=bins)
    freq_dist = pd.DataFrame({"Class Range": labels, "Frequency": freq})

    # ===== d. Relative Frequency dan Persentase =====
    freq_dist["Relative Frequency"] = (freq_dist["Frequency"] / len(data)).round(2)
    freq_dist["Percentage"] = (freq_dist["Relative Frequency"] * 100).map(lambda x: f"{x:.2f}%")

    print("\n[Distribusi Frekuensi]")
    print(freq_dist.to_string(index=False))

    # ===== e. Histogram =====
    plt.figure(figsize=(8, 4))
    plt.bar(freq_dist["Class Range"], [float(p.strip('%')) for p in freq_dist["Percentage"]])
    plt.xticks(rotation=45)
    plt.title("Histogram of Percentage Distribution")
    plt.ylabel("Percentage")
    plt.xlabel("Class Range")
    plt.tight_layout()
    plt.show()

    # ===== f. Dot Plot =====
    plt.figure(figsize=(10, 2))
    sns.stripplot(x=data, size=10)
    plt.title("Dot Plot")
    plt.xlabel("Value")
    plt.tight_layout()
    plt.show()

    # ===== g. Box Plot =====
    plt.figure(figsize=(6, 4))
    sns.boxplot(data=data)
    plt.title("Box Plot")
    plt.xlabel("Value")
    plt.tight_layout()
    plt.show()

    # ===== h. Skewness =====
    skewness = round(stats.skew(data), 2)
    if skewness > 0:
        skew_desc = "Positively skewed (Right-skewed): ekor data lebih panjang di kanan."
    elif skewness < 0:
        skew_desc = "Negatively skewed (Left-skewed): ekor data lebih panjang di kiri."
    else:
        skew_desc = "Data simetris (tidak miring)."

    print(f"\n[Skewness]")
    print(f"Nilai Skewness: {skewness}")
    print(f"Interpretasi: {skew_desc}")

    # ===== Looping =====
    ulang = input("\nIngin mengulang program? (y/n): ").strip().lower()
    if ulang != 'y':
        print("Program selesai. Terima kasih!")
        break