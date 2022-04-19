'''
w = write mode/mode menulis dan menghapus file lama, jika file tidak ada maka akan di buat file baru
r = read mode only/ hanya bisa baca
a = appending mode/ menambahkan data di akhir baris
r+ = write and read mode
'''
#membuat file text
file = open('data.txt','w')
file.write('ini adalah data text yang di buat menggunakan python')
file.write('\nini baris kedua')
file.write('\nini baris ke tiga')
file.write('\nini baris ke empat')
file.close()

#membaca file text
file2 = open('data.txt','r')
print(file2.read())
print(file2.readline())
file2.close()

#appending mode
file3 = open('data.txt','a')
file3.write('\nbaris ini di buat dengan menggunakan append')
file3.close()

