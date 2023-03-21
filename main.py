#Zestaw 2
#Zad 1

python1 = ' Python 2023'
python2 = ' Python 2023'
python3 = ' Python 2023'

print("------------------")
print(python1 == python2)
print(python2 == python3)

print(type(python1), hex(id(python1)))
print(type(python2), hex(id(python2)))
print(type(python3), hex(id(python3)))

python3 = 'Java 11'

print("------------------")
print(python1 == python2)
print(python2 == python3)

print(type(python1), hex(id(python1)))
print(type(python2), hex(id(python2)))
print(type(python3), hex(id(python3)))

#Zad 2

liczba1 = float(input("Pierwsza liczba: "))
operator = input("Wpisz operator np. +, -, *, / : ")
liczba2 = float(input("Druga liczba: "))

if operator == "+":
    print(liczba1 + liczba2)
elif operator == "-":
    print(liczba1 - liczba2)
elif operator == "*":
    print(liczba1 * liczba2)
elif operator == "/":
    if liczba2 == 0:
        print("Nie dziel przez 0")
    else:
        print(liczba1 / liczba2)
else:
    print("Podany zły operator")

#Zad3

answer = []

question = [
    "1. Jak masz na imię?",
    "2. Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie:\n"
    "A. czytanie książek/czasopism\n"
    "B. słuchanie muzyki\n"
    "C. spotkania z rodziną/przyjaciółmi",
    "3. W jakich okolicznościach czytasz książki najczęściej?\n"
    "A. w czasie wolnym (po pracy, na urlopie)\n"
    "B. w ogóle nie czytam\n"
    "C. podczas podróży",
    "4. Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?\n"
    "A. czytanie mnie relaksuje/odpręża\n"
    "B. czytanie to moje hobby\n"
    "C. chęć poszerzenia wiedzy",
    "5. Po książki w jakiej formie sięgasz najczęściej?\n"
    "A. papierowej (tradycyjnej)\n"
    "B. e-booki (książki elektroniczne) na komputerze\n"
    "C. e-booki na tablecie/telefonie",
    "6. Ile książek czytasz średnio w ciągu roku?\n"
    "A. 0\n"
    "B. 1-2\n"
    "C. 3+",
    "7. Jak często średnio czytasz książki?\n"
    "A. wcale\n"
    "B. kilka razy w miesiacu\n"
    "C. codziennie"
]



# pytanie 1
name = input(question[0] + " ")
answer.append(name)

# pytanie 2
answer2 = ""
while answer2 not in ["A", "B", "C"]:
    answer2 = input(question[1] + "\nWybierz literę: ")
    if answer2 == "A":
        finalAnswer = "czytanie książek/czasopism"
    elif answer2 == "B":
        finalAnswer = "słuchanie muzyki"
    elif answer2 == "C":
        finalAnswer = "spotkania z rodziną/przyjaciółmi"
answer.append(answer2 + " : " + finalAnswer)

# pytanie 3
answer3 = ""
while answer3 not in ["A", "B", "C"]:
    answer3 = input(question[2] + "\nWybierz literę: ")
    if answer3 == "A":
        finalAnswer = "w czasie wolnym (po pracy, na urlopie)"
    elif answer3 == "B":
        finalAnswer = "w ogóle nie czytam"
    elif answer3 == "C":
        finalAnswer = "podczas podróży"
answer.append(answer3 + " : " + finalAnswer)

#pytanie 4
answer4 = ""
while answer4 not in ["A", "B", "C"]:
    answer4 = input(question[3] + "\nWybierz literę: ")
    if answer4 == "A":
        finalAnswer = "czytanie mnie relaksuje/odpręża"
    elif answer4 == "B":
        finalAnswer = "czytanie to moje hobby"
    elif answer4 == "C":
        finalAnswer = "chęć poszerzenia wiedzy"
answer.append(answer4 + " : " + finalAnswer)

#pytanie 5
answer5 = ""
while answer5 not in ["A", "B", "C"]:
    answer5 = input(question[4] + "\nWybierz literę: ")
    if answer5 == "A":
        finalAnswer = "papierowej (tradycyjnej)"
    elif answer5 == "B":
        finalAnswer = "e-booki (książki elektroniczne) na komputerze"
    elif answer5 == "C":
        finalAnswer = "e-booki na tablecie/telefonie"
answer.append(answer5 + " : " + finalAnswer)

#pytanie 6
answer6 = ""
while answer6 not in ["A", "B", "C"]:
    answer6 = input(question[5] + "\nWybierz literę: ")
    if answer6 == "A":
        finalAnswer = "0"
    elif answer6 == "B":
        finalAnswer = "1-2"
    elif answer6 == "C":
        finalAnswer = "3+"
answer.append(answer6 + " : " + finalAnswer)

#pytanie 7
answer7 = ""
while answer7 not in ["A", "B", "C"]:
    answer7 = input(question[6] + "\nWybierz literę: ")
    if answer7 == "A":
        finalAnswer = "wcale"
    elif answer7 == "B":
        finalAnswer = "kilka razy w miesiacu"
    elif answer7 == "C":
        finalAnswer = "codziennie"
answer.append(answer7 + " : " + finalAnswer)

# drukowanie wyników
print("\nPomyślnie wykonano ankietę :)")
print("Twoje odpowiedzi to:")
print(question[0]+"\n", name)
print(question[1]+"\n", answer[1])
print(question[2]+"\n", answer[2])
print(question[3]+"\n", answer[3])
print(question[4]+"\n", answer[4])
print(question[5]+"\n", answer[5])
print(question[6]+"\n", answer[6])