#son = float(input("Juft son kiriting !"))
#if son%2 :
#    print("Bu juft son emas !")
#else:
#   print("Raxmat")
#yosh = int(input("Yoshingiz nechida ! "))
#if yosh<4 or yosh>60 :
#    narx = 0
#elif yosh < 18:
#    narx = 10000
#lif yosh>18 :
#    narx = 20000
#print(f"Sizga chipta narxi {narx} so`m ! ")
#son = float(input("Birinchi sonni kiriting !"))
#son1 = float(input("Ikinchi sonni kiriting !"))
#if son < son1:
#    print (f"{son}<{son1}")
#elif son == son1 :
#    print(f"{son}={son1}")
#else : 
#    print(f"{son}>{son1}")
#mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz','kartoshka', 'olma', 'banan', 'uzum', 'qovun']
#savat = []
#for n in range(5):
#    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
#for mahsulot in savat:
#    if mahsulot in mahsulotlar:
#        print(f"Do'konimizda {mahsulot} bor")
#    else:
#        print(f"Do'konimizda {mahsulot} yo'q")
mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz', 'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)
if mavjud_emas:
 print(f"Do'konimizda quyidagi mahsulotlar yo'q:")
for mahsulot in mavjud_emas:
    print(mahsulot)
else:
  print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
#foydalanuvchilar = ['Jamshidharker9363', 'Eminien', 'jek_ma', 'Editor', 'Close_Coder']
# = input("Yangi user kiriting !")
#if # in foydalanuvchilar :
#    print("Bu user bant iltimos yangi user kiriting !")
#lse:
#   print("Muofiqiyatli ro`yhatdan o`tdingiz ! " , f"Hush kelibsiz {#}")