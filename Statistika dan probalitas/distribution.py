from scipy.stats import binom, poisson

while True:
    print("\n=== DISTRIBUTION CALCULATOR ===")
    print("1. Binomial Distribution")
    print("2. Poisson Distribution")
    pilihan = input("Pilih distribusi (1/2): ").strip()

    if pilihan == '1':
        print("\n--- BINOMIAL DISTRIBUTION ---")
        n = int(input("Masukkan jumlah percobaan (n): "))
        p = float(input("Masukkan peluang sukses (p): "))
        x = int(input("Masukkan nilai x (jumlah sukses yang dicari): "))

        prob = binom.pmf(x, n, p)
        print(f"P(X = {x}) = {prob:.4f}")

    elif pilihan == '2':
        print("\n--- POISSON DISTRIBUTION ---")
        λ = float(input("Masukkan nilai lambda (λ = rata-rata kejadian): "))
        x = int(input("Masukkan nilai x (jumlah kejadian yang dicari): "))

        prob = poisson.pmf(x, λ)
        print(f"P(X = {x}) = {prob:.4f}")

    else:
        print("Pilihan tidak valid.")

    ulang = input("\nIngin menghitung lagi? (y/n): ").strip().lower()
    if ulang != 'y':
        print("Program selesai.")
        break