print("""********************
Hesap Makinesi Programı

İşlemler;

1. Toplama İşlemi

2. Çıkarma İşlemi

3. Çarpma İşlemi

4. Bölme İşlemi
********************
""")
while True:

    sayi1 = int(input("İlk sayıyı giriniz: "))
    sayi2 = int(input("İkinci sayıyı giriniz: "))

    işlem = input("İşlemi giriniz: ")

    if (işlem == "1"):
        print("{} + {} = {}".format(sayi1,sayi2,sayi1+sayi2))

    elif(işlem == "2"):
        print("{} - {} = {}".format(sayi1,sayi2,sayi1-sayi2))

    elif(işlem == "3"):
        print("{} * {} = {}".format(sayi1,sayi2,sayi1*sayi2))

    elif(işlem == "4"):
        print("{} / {} = {}".format(sayi1,sayi2,sayi1/sayi2))

    else:
        print("Geçersiz İşlem")

    cevap = input("Çıkmak için 'q' ya basın. Devam etmek için 'w' ya basın: ")

    if ((cevap == "q") or (cevap == "Q")):
        break
    elif ((cevap == "w") or (cevap == "W")):
        continue
