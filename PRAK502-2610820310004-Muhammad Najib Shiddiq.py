def mutlak(angka):
    if angka < 0:
        return -angka
    return angka

def hitung(nilai1, nilai2):
    return mutlak(nilai1 - nilai2)

if __name__ == "__main__":
    a, c, b, d = map(int, input().split())
    
    Hasil = hitung(a, b) + hitung(c, d)
    print(mutlak(Hasil))