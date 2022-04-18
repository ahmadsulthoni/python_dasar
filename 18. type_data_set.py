'''
set/himpunan = tidak punya urutan,jika ada 2 nama yang sama di anggapnya hanya 1 data
cara menggunakan himpunan memakai {}
'''
# contoh
superhero = {'Saras 008', 'Wiro Sableng', 'Gundala'}

# menambah himpunan
superhero.add('Gatot Kaca')  # <-- Urutanya akan acak
print(superhero)
superhero.add('Gundala')  # <-- Tidak akan ada data tambahan
print(superhero)
# dengan menggunakan set

superhero = set()
superhero.add('Wiro Sableng')
superhero.add('Gundala')
superhero.add('Saras 008')
print(superhero)

'''
himpunan bisa di beri string dan angka di 1 tempat
set tidak support index
'''
# mencari gabungan dan irisan di himpunan
ganjil = {1, 3, 5, 7, 9}
genap = {2, 4, 6, 8, 10}
prima = {2, 3, 5, 7}

# mencari gabungan
print(ganjil.union(genap))
print(ganjil.intersection(prima))
