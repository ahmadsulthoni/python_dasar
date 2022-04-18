# scope variable local

'''
namakucing = 'Casandra'

def rubahnamakucing (namabaru):
    namakucing = namabaru
    print('saya rubah nama kucing menjadi',namakucing)

rubahnamakucing('ketie')
print('nama kucing saya menjadi',namakucing)
'''

# scope variable global
namakucing = 'Casandra'


def rubahnamakucing(namabaru):
    global namakucing
    namakucing = namabaru
    print('saya rubah nama kucing menjadi', namakucing)


rubahnamakucing('ketie')
print('nama kucing saya menjadi', namakucing)
