def MaxBilangan(a, b, c, d):
    return max(a, b, c, d)

input_data = input().split()
a, b, c, d = map(int, input_data)

hasil = MaxBilangan(a, b, c, d)
print(hasil)
