#tipe data dictionary adalah sebuah struktur data assosiatif/maping
'''
Rumus
member1 = {key:value,key:value}
'''

#contoh
member1 = {'id':101,
           'nama':'Ahmad Sulthoni',
           'Pekerjaan':'Swasta',
           'Status Member':'Gold'
            }

print(member1['Pekerjaan'])
print(member1.keys())
print(member1.values())
print(member1.items())

member2 = {'id':102,
           'nama':'Karyo Papan',
           'Pekerjaan':'Jual Papan',
           'Status Member':'Berlian'
           }
memberlist = {101:member1,102:member2}

print(memberlist[102])

