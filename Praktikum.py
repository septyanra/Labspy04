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
    nim        = input      ("NIM            : ")    
    nilaitugas = float(input("Nilai Tugas    : "))
    nilaiuts   = float(input("Nilai UTS      : "))
    nilaiuas   = float(input("Nilai UAS      : "))
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
     
        

    masukkan = input("Input Data Selanjutnya?(y/t) => ")

    namaMHS.append(nama)
    nimMHS.append(nim)
    nilaiTugas.append(nilaitugas)
    nilaiUTS.append(nilaiuts)
    nilaiUAS.append(nilaiuas)
    nilaiAkhir.append(nilaiakhir)
    keterangan.append(ket)
    
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
