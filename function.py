'''
#mendefinisikan
def fungsi():
    print('ini adalah fungsi')
fungsi()
'''

#membuat fungsi sederhana

def suaraayam():
    print('Kukuruyuk')
def hargaayam():
    suaraayam()
    print('Harga ayam per 1 Kg Rp.20.000')
#hargaayam()

#membuat fungsi dengan input argument
def hargatotalayam(Kg):
    suaraayam()
    harga = 20000
    hargatotal = Kg * harga
    print('Harga',Kg,'Kg Ayam adalah ',hargatotal)
hargaayam()
hargatotalayam(3)
