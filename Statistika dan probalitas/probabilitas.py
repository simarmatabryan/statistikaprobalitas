import math

while True:
    # ===== a. Input data =====
    print("\n=== PROGRAM PROBABILITY ===")
    print("Masukkan elemen semesta (universal set):")
    U = set(input("U (pisahkan dengan spasi): ").split())

    print("\nMasukkan himpunan A:")
    A = set(input("A (pisahkan dengan spasi): ").split())

    print("\nMasukkan himpunan B:")
    B = set(input("B (pisahkan dengan spasi): ").split())

    # ===== b. Probabilitas =====
    p_A = len(A) / len(U)
    p_B = len(B) / len(U)
    p_A_union_B = len(A.union(B)) / len(U)
    p_A_intersect_B = len(A.intersection(B)) / len(U)
    p_A_complement = 1 - p_A

    print("\n[Probabilitas]")
    print(f"P(A): {p_A:.2f}")
    print(f"P(B): {p_B:.2f}")
    print(f"P(A ∪ B): {p_A_union_B:.2f}")
    print(f"P(A ∩ B): {p_A_intersect_B:.2f}")
    print(f"P(A') (komplemen A): {p_A_complement:.2f}")

    # ===== c. Permutasi dan Kombinasi =====
    print("\n[Permutasi dan Kombinasi]")
    try:
        n = int(input("Masukkan nilai n: "))
        r = int(input("Masukkan nilai r: "))

        if r > n:
            print("❌ r tidak boleh lebih besar dari n.")
        else:
            permutasi = math.perm(n, r)
            kombinasi = math.comb(n, r)

            print(f"Permutasi P({n},{r}): {permutasi}")
            print(f"Kombinasi C({n},{r}): {kombinasi}")
    except ValueError:
        print("❌ Masukkan angka bulat untuk n dan r!")

    # ===== d. Operasi Himpunan =====
    print("\n[Operasi Himpunan]")
    print(f"A ∪ B (Union): {A.union(B)}")
    print(f"A ∩ B (Intersection): {A.intersection(B)}")
    print(f"A' (Komplemen terhadap U): {U.difference(A)}")

    # ===== Looping ke awal? =====
    ulang = input("\nIngin mengulang? (y/n): ").strip().lower()
    if ulang != 'y':
        print("Program selesai.")
        break