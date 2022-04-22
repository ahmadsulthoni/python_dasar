'''
nilai = 80
if nilai == 75:
    print('Nilai anda =',nilai)

if nilai == 80:
    print('Nilai anda =',nilai)
'''

#nexting if/if di dalam if

'''
nilai1 = 60
nilai2 = 90

if nilai1 >= 50:
    print('nilai anda =',nilai1)
    print('Step 1')
    if nilai2 <= 80:
        print('Nilai anda =', nilai2)
        print('step 2')
'''
nilai = 30

if 80 <= nilai <= 100:
    print('nilai anda adalah A')
elif 70 <= nilai <= 80:
    print('nilai anda adalah B')
elif 60 <= nilai <= 70:
    print('nilai anda adalah C')
elif 50 <= nilai <= 60:
    print('nilai anda D, Lakukan perbaikan')
else:
    print('maaf anda tidak lulus')

#operator logika untuk list string

gorengan = ['bakwan','cireng','tahu','pukis', 'combro','bandros']
beli = 'bandros'

if beli in gorengan:
    print('mamang bilang,"ya, saya jual ',beli,'"')

if not beli in gorengan:
    print('"saya gak jual',beli,'"')

