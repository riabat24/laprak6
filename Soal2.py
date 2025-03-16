def Ganjil(a,b):
    if b > a:
        while b != a:
            if b % 2 == 1:
                print(b, end=" ")
            b = b - 1
    else:
        while b != a:
            b = b + 1
            if b % 2 == 1:
                print(b, end=" ")
bawah = int(input("Masukan nilai bawah: "))
atas = int(input("Masukan nilai atas: "))
Ganjil(atas,bawah)
