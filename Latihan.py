print ("````````````Latihan````````````")
print ('===============================\n')
print("List:")
print("A = [1,5,10,15,20]")
print('\n')
print ("Mengakses List")
A = [1,5,10,15,20]
print(A[2])            #Menampilkan elemen ke-3
print(A[1:4])          #Menampilkan elemen ke-2 sampai ke-4
print(A[-1])           #Menampilkan elemen terakhir

print("Mengubah Elemen List")
print("A =", A)
A[3] = 75              #Mengubah elemen ke-4 dengan nilai lain
print(A)
A[3:5] = [100,90]      #Mengubah elemen ke-4 sampai elemen terakhir
print(A)

print("Menambahkan Elemen List")
print("A  =", A)
B = A[:2]              #Mengambil 2 bagian dari list pertama
print("B  =" , B)
B.append("September")  #Menambah list B dengan nilai string
print("B  =", B)
B.extend([23,19,99])   #Menambah list B dengan 3 nilai
print("B  =", B)
AB = A+B               #Menggabungkan list A dengan list B
print("AB =", AB)




