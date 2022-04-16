#tuples adalah nilai yang tidak di rubah atau di tambah

#list
ganjil = [1,3,4,7,9]

#tuple
genap = (2,4,6,8,10)
print(type(ganjil))
print(type(genap))

#menambah data
ganjil.append(2)
genap = 'genap.append(2)<<-- akan Eror'
print(ganjil)
print(genap)
genap = (2,4,6,8,10)
#cara lihat apa saja yang bisa di lakukan di type data tuple
print(dir(ganjil))
print(dir(genap))

import sys
data_list = [1,2,3,4,5,"Pisang goreng",False,3.14]
data_tuple = (1,2,3,4,5,"Pisang goreng",False,3.14)

besar_datalist = sys.getsizeof(data_list)
besar_datatuple = sys.getsizeof(data_tuple)
'''
hasil data tuple lebih kecil dari list data karna tidak banyak perintah 
yang bisa di lakukan di tuple jadi, untuk penggunaan tuple lwbih baik untuk data yang tidak di ubah
'''
#cara mengecheck waktu python mengopile tuple/list

import timeit
data_list = timeit.timeit(stmt="[1,2,3,4,5]", number=1000000)
data_tuple = timeit.timeit(stmt="(1,2,3,4,5)",number=1000000)
print("Waktu yang di butuhkan untuk memproses list adalah",data_list)
print("Waktu yang di butuhkan untuk memproses tuple adalah",data_tuple)
