def maksimal(a, b):
    if a > b:
        return a
    else:
        return b

def minimal(a, b):
    if a < b:
        return a
    else:
        return b

if __name__ == "__main__":
    bilangan = int(input())
    
    nilai_list = list(map(int, input().split()))
    
    batas = 0
    maks = -100000
    minim = 100000
    
    while batas < bilangan:
        nilai = nilai_list[batas]
        maks = maksimal(maks, nilai)
        minim = minimal(minim, nilai)
        batas += 1
        
    print(f"{maks} {minim}")