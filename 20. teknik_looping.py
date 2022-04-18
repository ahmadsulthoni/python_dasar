# contoh looping biasa

nama_band = ['Payung Teduh', 'Four Twenty', 'Dialog dini hari', 'Mr.Sonjaya', 'Parah Yena', ]
kumpulan_lagu = ['akad', 'zona nyaman', 'Rumahku', 'sang filsuf', 'Sindoro']

iterasi = 0;
for band in nama_band:
    print('No', iterasi, 'Nama Band', band)
    iterasi += 1

# enumerate
for i, band in enumerate(nama_band):
    print(i, ':', band)

# zip
for band, lagu in zip(nama_band, kumpulan_lagu):
    print(band, 'Menyanyikan lagu berjudul', lagu)

# set
playlist = {'Jaran Goyang', 'Mandul', 'Suara', 'Manja'}
for lagu in sorted(playlist):
    print(lagu)

# dictionary
playlist2 = {'Payung Teduh': 'Akad', 'Four Twenty': 'Zona Nyaman', 'Dialog Dini Hari': 'Rumahku'}

# mengambil data keys (band)
for i in playlist2.keys():
    print(i)

# mengambil data value (Judul)
for i in playlist2.values():
    print(i)

# mengambil semua data (band & judul) dua bagian data
for i in playlist2.items():
    print(i)

# mengambil semua data (band & judul) dua bagian data
for i, v in playlist2.items():
    print(i, 'lagunya:', v)
