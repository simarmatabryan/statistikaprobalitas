import math
from scipy.special import comb, factorial

# ===== Fungsi menghitung Binomial PMF =====
def binomial_pmf(n, p, k):
    """Menghitung probabilitas distribusi binomial"""
    q = 1 - p
    pmf = comb(n, k) * (p ** k) * (q ** (n - k))
    return pmf

# ===== Fungsi menghitung Poisson PMF =====
def poisson_pmf(mu, k):
    """Menghitung probabilitas distribusi Poisson"""
    pmf = (mu ** k * math.exp(-mu)) / factorial(k)
    return pmf

# ===== Menu Pilihan Pengguna =====
while True:
    print("\n=== DISTRIBUTION CALCULATOR ===")
    print("1. Binomial Distribution")
    print("2. Poisson Distribution")
    print("3. Keluar")

    pilihan = input("Pilih distribusi (1/2/3): ").strip()

    # ===== Perhitungan Binomial =====
    if pilihan == '1':
        try:
            print("\n--- BINOMIAL DISTRIBUTION ---")
            n = int(input("Masukkan jumlah percobaan (n): "))
            p = float(input("Masukkan peluang sukses per percobaan (p): "))
            k = int(input("Masukkan jumlah keberhasilan yang diinginkan (k): "))

            # Validasi input
            if n <= 0:
                print("❌ n harus bilangan bulat positif!")
                continue
            if k < 0 or k > n:
                print("❌ k harus antara 0 hingga n!")
                continue
            if p < 0 or p > 1:
                print("❌ p harus berada di antara 0 dan 1!")
                continue

            # ===== Menghitung Nilai Binomial PMF =====
            prob_binom = binomial_pmf(n, p, k)

            # ===== Menampilkan Hasil Binomial =====
            print(f"\n=== Hasil Perhitungan Distribusi Binomial ===")
            print(f"P(X = {k}) = {prob_binom:.4f}")
            print(f"n = {n}, p = {p}, q = {1 - p:.2f}, k = {k}")

        except ValueError:
            print("❌ Masukkan nilai yang valid untuk n, p, dan k!")

    # ===== Perhitungan Poisson =====
    elif pilihan == '2':
        try:
            print("\n--- POISSON DISTRIBUTION ---")
            mu = float(input("Masukkan rata-rata kejadian per periode (μ): "))
            k = int(input("Masukkan jumlah kejadian yang diinginkan (k): "))

            # Validasi input
            if mu < 0:
                print("❌ μ harus bilangan positif atau nol!")
                continue
            if k < 0:
                print("❌ k harus bilangan bulat positif atau nol!")
                continue

            # ===== Menghitung Nilai Poisson PMF =====
            prob_poisson = poisson_pmf(mu, k)

            # ===== Menampilkan Hasil Poisson =====
            print(f"\n=== Hasil Perhitungan Distribusi Poisson ===")
            print(f"P(X = {k}) = {prob_poisson:.4f}")

        except ValueError:
            print("❌ Masukkan nilai yang valid untuk μ dan k!")

    # ===== Keluar dari Program =====
    elif pilihan == '3':
        print("Program selesai. Terima kasih!")
        break

    # ===== Jika Pilihan Tidak Valid =====
    else:
        print("❌ Pilihan tidak valid! Silakan pilih 1, 2, atau 3.")
