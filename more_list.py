#membuat list
barang = ['kunci','ember','jaket','ban','mobil']
print (barang)

#Menambah data di list
barang.append('sepeda')
print(barang)

#menambah data di list dengan pemisahan karakter huruf
barang.extend('dompet')
print(barang)

#menyisipkan data sesuai dengan nomor list
barang.insert(0,'sepeda')
print(barang)

#menghitung karakter di data
jumlahsepeda = barang.count('sepeda')
print('Jumlah Sepeda adalah',jumlahsepeda)

#meremove data
barang.remove('sepeda')
print(barang)

#untuk membalik data di list
barang.reverse()
print(barang)

#mencopy data supaya data tidak sama dan data awal tetap terjaga

stuff = barang.copy()
stuff.append('gelas')
print(stuff)
print(barang)