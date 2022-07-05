import pandas as pd

ogrenci_sayisi=int(input("Kaç öğrenci kaydedeceksiniz?:"))
namelist=[]
familyNamelist=[]
SchoolNamelist=[]
ortalamalist=[]





for i in range(ogrenci_sayisi):
    name=input("İsim Giriniz:")
    familyName=input("Soyad giriniz:")
    SchoolName=input("Okul No giriniz:")
    vizeNotu=int(input("Vize notu giriniz:"))
    if vizeNotu>=100:
        print("100'den büyük sayı giremezsiniz.")
        vizeNotu=int(input("Vize notu giriniz:"))
    finalNotu=int(input("Final notu giriniz:"))
    if finalNotu>=100:
        print("100'den büyük sayı giremezsiniz.")
        finalNotu=int(input("Final notu giriniz:"))
    ortalama=(vizeNotu*0.4)+(finalNotu*0.6)
    namelist.append(name)
    familyNamelist.append(familyName)
    SchoolNamelist.append(SchoolName)
    ortalamalist.append(ortalama)


    
   



seri1=pd.DataFrame({"Ad":namelist,"Soyad":familyNamelist,"School_Name":SchoolNamelist,"Ortalama":ortalamalist})
seri1.loc[seri1['Ortalama'] <= 40, 'Durum'] = 'Kaldı' 
seri1.loc[seri1['Ortalama'] > 40, 'Durum'] = 'Geçti'

if ortalama>90:
    print("AA ")
elif ortalama>80 and ortalama<90:
    print("BA ")
elif ortalama>70 and ortalama<80:
    print("BB ")
elif ortalama>60 and ortalama<70:
    print("CB ")
elif ortalama>50 and ortalama<60:
    print("CC ")
elif ortalama>40 and ortalama<50:
    print("DC ")
else:
    print("FF ")

print(seri1)
dosya=seri1.to_excel("C:/Users/Sefa/Desktop/Bilgiler.xlsx",sheet_name="Sınav_Sonuçları" )
