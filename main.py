a = b = 2566
a = 2566
b=a
print(id(a), id(b))
print(a)
print(type(a))
print(type("tekst"))
print(type(False))

import math

a,b,c,d,e = 1.5,2.5,3.5,4.5,5.5
print(a+b+c+d+e)
print(round(a))
print(round(a),round(b),round(c),round(d),round(e))
print(round(a)+round(b)+round(c)+round(d)+round(e))
print(int(a)+int(b)+int(c)+int(d)+int(e))
print(math.ceil(a)+math.ceil(b)+math.ceil(c)+math.ceil(d)+math.ceil(e))

a = 21
if a > 20:
    print("a wieksze od 20")
else:
    print("a mniejsze od 20")

a = 20
if a > 20:
    print("a wieksze od 20")
elif a < 20:
    print("a mniejsze od 20")
else:
    print("a rowne 20")

tekst = 'to jest tekst'
tekst2 = 'to jest drugi tekst'
tekst3 = 'to jest \ntrzeci tekst'
print(tekst+tekst2)
print(tekst3)

a=20.547

b= 45

print(f"to jest pierwsza liczba {a},\n to jest druga liczba {b}")
#zamienia na duze litery
print(tekst.upper())
#zamienia na male litery
print(tekst.lower())
#zamienia pierwsze litery slowa na duze, reszte na male
print(tekst.title())