"""
===================   TASK 2   ====================
* Name: Product Of Digits
*
* Write a script that will take an input from user
* as integer number and display product of digits
* for a given number. Consider that user will always
* provide integer number.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
===================================================
"""
broj = ("Unesite cijeli broj: ")  # eval procjenjuje sta je korisnik unio

if not isinstance(broj,int): # ispitujemo da li je unijet cijeli broj
    print("Pogresan unos!")
    quit()

proizvod = 1
for i in str(abs(broj)): # prolazi kroz cifre datog broja(ali apsolutnog,zbog minusa)

    proizvod *= int(i)   # mnozi sve cifre datog broja

if broj < 0 : # ako je broj negativan proizvod cifara ce takodje biti negativan,pa zato dobijeni proiz mnozimo sa -1

    print("Proizvod cifara datog broja je: ", (-1) * proizvod)

else:
    print("Proizvod cifara datog broja je: ", proizvod)







