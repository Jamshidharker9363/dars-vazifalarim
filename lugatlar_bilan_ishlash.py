"""
otam = {'ismi':'Shukrullo', 'tugulgan_yili' : '1977', 'tugulgan_joyi' : 'Andijon viloyati'}
tyil = otam ['tugulgan_yili']
tjoy = otam['tugulgan_joyi']
print(f"Otamning ismi {otam['ismi'].title()},{tyil} - yilda, {tjoy.title()}da tug`ulgan .")

onam = {'ismi' : 'Muhoira', 'tugulgan_yili' : '1981', 'tugulgan_joyi' : 'Andijon viloyati'}
tyil =  onam['tugulgan_yili']
tjoy = onam['tugulgan_joyi']
print(f"Onamning ismi {onam['ismi'].title()},{tyil} - yilda, {tjoy.title()}da tug`ulgan .")

akam = {'ismi' : 'Abdulloh', 'tugulgan_yili' : '1999', 'tugulgan_joyi' : 'Andijon viloyati'}
tyil = akam ['tugulgan_yili']
tjoy = akam ['tugulgan_joyi']
print(f"Akamning ismi {akam['ismi'].title()},{tyil} - yilda, {tjoy.title()}da tug`ulgan .")

ukam = {'ismi':'Adurahmon', 'tugulgan_yili' : '2005', 'tugulgan_joyi' : 'Andijon viloyati'}
tyil = ukam ['tugulgan_yili']
tjoy = ukam ['tugulgan_joyi']
print(f"Ukamning ismi {ukam['ismi'].title()},{tyil} - yilda, {tjoy.title()}da tug`ulgan .")
"""
"""
taomlar = {'Akam':'Chuchvara','Ukam':'manti','Singlim':'osh','Opam':'Mastava','Jiyanim':'dimlama'}
taom = taomlar['Akam']
print(f"Akamning sevimli tamomi {taom}")

taom = taomlar['Ukam']
print(f"Ukamning sevimli tamomi {taom}")

taom = taomlar['Opam']
print(f"Opamning sevimli tamomi {taom}")

python_izohli_lugati = {
    'integer':"Butun son",
    'float':"O'nlik son",
    'string':"Matn",
    'list':"Ro'yxat",
    'tuple':"O'zgarmas ro'yxat",
    'Dictionary':"Lug`at"}


#kalit = input("Kalit so'z kiriting:").lower()
#print(python_izohli_lugati.get(kalit,"Bunday so'z mavjud emas"))

kalit = input("Kalit so'z kiriting:").lower()
tarjima = python_izohli_lugati.get(kalit)
if tarjima==None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")


davlatlar = {
    "o'zbekiston":'toshkent',
    'aqsh':'washington d.c.',
    'rossiya':'moskva',
    'tojikiston':'dushanbe',
    "qirg'iziston":'bishkek',
    'qozog\'iston':'nursulton',
    'malayziya':'kuala-lumpur',
    'singapur':'sungapur',
    'italiya':'rim'}
print("Dunyo davlatlari :")
for davlat in sorted(davlatlar):
    print(davlat.upper())


print('\nDavlatlarning poytaxtlari:')
for poytaxt in sorted(davlatlar.values()):
    print(poytaxt.title())


county = input("Qaysi davlatni poytaxtini bilishni istaysiz :").lower()
capital = davlatlar.get(county)
if county == None :
    print("Bizda bunday malumot yo'q !")
else:
    print(f"{county.upper()} davlatining poytaxti {capital.title()} shahri !")
"""
menu = {
        'osh':20000,
        "lag'mon":22000,
        'non':4000,
        'choy':5000,
        'shashlik':12000,
        'somsa':6000,
        'tabaka':15000
        }
print('3 ta taom buyurtma qiling ')
buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f"{n+1}- taom :").lower())

for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtma.title()} {menu[buyurtma]} so`m")
    else:
        print(f"Kechirasiz , bizda {buyurtma} yo`q .")