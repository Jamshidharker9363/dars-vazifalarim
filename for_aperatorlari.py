#ismlar = ["Komila" , "Nusratillo" , "Otabek" , "Mahliyo" , "Mohinur"]
#for ismlar1 in ismlar :
#    print (f"Jim o`tiriylar please {ismlar1}")
#    print ("Farosatni ishlatiylar")
#    print("Kod" ,len(ismlar1) , " marta takrorlandi")
#sonlar = list(range(11,100,2))
#for son in sonlar:
#     print(son*son*son)
#kinolar = []
#print("Yoqtirgan kinolaringgizni kiriting ")
#for kino in range(5):
#    kinolar.append(input(f"{kino+1} - kinoo :"))
#    print(kinolar)
odamchalar = int(input("Bugun necha kishi bilan suhbat qildinggiz ?"))
odamlar = []
print("Bugun gaplashgan odamlaringgizni ismini kiriting ")
for odam in range(odamchalar):
    odamlar.append(input(f"{odam+1}- suhbat qilgan odamaingiz kim edi :"))
print(odamlar)