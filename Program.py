#Program Menghitung Nilai Akhir

namaMHS    = []
nimMHS     = []
nilaiTugas = []
nilaiUTS   = []
nilaiUAS   = []
nilaiAkhir = []
keterangan = []


masukkan = "y"
while masukkan == "y":  
    nama       = input      ("Nama Mahasiswa : ")
    namaMHS.append(nama)
    nim        = input      ("NIM            : ")
    nimMHS.append(nim)
    nilaitugas = float(input("Nilai Tugas    : "))
    nilaiTugas.append(nilaitugas) 
    nilaiuts   = float(input("Nilai UTS      : "))
    nilaiUTS.append(nilaiuts)
    nilaiuas   = float(input("Nilai UAS      : "))
    nilaiUAS.append(nilaiuas)
    nilaiakhir = float((nilaitugas)*30/100 + (nilaiuts)*35/100 + (nilaiuas)*35/100) 
                   
    if nilaiakhir < 55:
        ket = "E"     
    elif 55 <= nilaiakhir and nilaiakhir < 65:
        ket = "D"
    elif 65 <= nilaiakhir and nilaiakhir < 75:
        ket = "C"
    elif 75 <= nilaiakhir and nilaiakhir < 90:
        ket = "B"
    else:
        ket = "A"
    nilaiAkhir.append(nilaiakhir)
    keterangan.append(ket) 
        

    masukkan = input("Input Data Selanjutnya?(y/t) => ")
        

print()
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
print("                          Data Nilai Mahasiswa                              ")
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
print()
print("============================================================================")
print("|","No.","|","   Nama   ","|", "   NIM   ","|"," Tugas ","|"," UTS ","|"," UAS ","|"," Akhir ","|"," Ket ","|")
print("============================================================================")

for n in range(len(namaMHS)):     
      print("| ",  n+1  ," |  ", namaMHS[n] ,"  |", nimMHS[n] ,"|  ", nilaiTugas[n] ," | ", nilaiUTS[n] ,"| ", nilaiUAS[n] ,
            "| ", nilaiAkhir[n] ," |  ", keterangan[n] ,"  |")
print("============================================================================")
print()
print()
