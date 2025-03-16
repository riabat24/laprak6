print("Program penghitung IPS Mahasiswa") 
t = int(input("Berapa jumlah mata kuliah? "))

skor = 0 

for i in range (0,t): 
    matkul = input("Nilai MK %d: "%(i+1)) 
    if matkul == "A": 
        nilai = 4 
    elif matkul == "B": 
        nilai = 3 
    elif matkul == "C": 
        nilai = 2 
    elif matkul == "D": 
        nilai = 1 
    skor += nilai 

ipk = skor / t 

print("Nilai IPS Anda adalah: %0.2f" %ipk)