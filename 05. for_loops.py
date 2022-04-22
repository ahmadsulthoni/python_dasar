#list sebagai iterable

gorengan = ['bakwan','cireng','tahu isi','tempe goreng','ubi goreng']

for g in gorengan:
    print(g)
    print(len(g))

#string sebagai iterable
bakwan = 'bakwan'

for i in bakwan:
    print(i)

#for dalam for
buah = ['semangka','jeruk','apel','anggur']
sayur = ['kangkung','wortel','tomat','kentang']
daftar_belanja = [gorengan,buah,sayur]

for subDaftarBelanja in daftar_belanja:
    print(subDaftarBelanja)

for komponen in subDaftarBelanja:
    print(komponen)

#for loop,else,break,range

number = 43

for i in range(0,40): #lakukan perulangan 0 sampai 40
    print(i)
    if i is number:
        print('angka di temukan',i)
        break
else:
    print('angka',number,'tidak di temukan')
print('proses berakhir')
