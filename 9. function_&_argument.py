#Fungsi dengan menggunakan argument sederhana

'''
def siswa(nama):
    print('Siswa ini bernama',nama)
siswa('Joko')
'''

#Fungsi dengan menggunakan keyword dan argument

'''
def guru(nama,pelajaran):
    print('Guru ini adalah',nama)
    print('Mengajar',pelajaran)
guru(nama='mulyono',pelajaran='Penjaskes')
guru(pelajaran='Bahasa Inggris',nama='kusnadi')
guru('Bahasa Jawa', 'Jarwo')
'''

#Fungsi dengan menggunakan default argument

def penjagasekolah(nama,shift='siang',sifat='ramah'):
    print('penjaga sekolah ini bernama',nama)
    print('Shiftnya',shift)
    print('Sifatnya',sifat)

penjagasekolah('kabul')
penjagasekolah('maman',shift='malam',sifat='Galak')
penjagasekolah(nama='parjo',shift='Pagi',sifat='pemarah')
