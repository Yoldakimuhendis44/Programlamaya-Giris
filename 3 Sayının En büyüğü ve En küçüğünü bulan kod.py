enb=0
enk=0
sayi1=int(input("1. sayıyı giriniz:"))
sayi2=int(input("2. sayıyı giriniz:"))
sayi3=int(input("3. sayıyı giriniz:"))

if sayi1 > sayi2 and sayi3 > sayi2 and sayi1 > sayi3:
    print(" enb=", sayi1)
    print(" enk=", sayi2)
if sayi2 > sayi1 and sayi1 > sayi3:
    print(" enb=", sayi2)
    print(" enk=", sayi3)
if sayi1 > sayi2 and sayi2 > sayi3:
    print(" enb=", sayi1)
    print(" enk=", sayi3)
if sayi2 > sayi1 and sayi3 > sayi1 and sayi2 > sayi3:
    print(" enb=", sayi2)
    print(" enk=", sayi1)
if sayi3>sayi1 and sayi1>sayi2:
    print(" enb=", sayi3)
    print(" enk=", sayi2)
if sayi3 > sayi1 and sayi2 > sayi1 and sayi3 > sayi2:
    print(" enb=", sayi3)
    print(" enk=", sayi1)
