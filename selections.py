number = 200
if number < 100:
    print("A szám kisebb mint 100")
print("end")

number = 5
if number <0:
    print("negatív")
elif number == 0:
    print("Nulla")
else:
    print("Pozitív")


number = input("Adj meg egy tetszőleges számit és leírom, hogy páros-e vagy páratlan")
if int(number) % 2 == 0:
    print("páros")
else:
    print("páratlan")

count = 0
for number in [5,6,-7,15,-30,13]:
    if number >= 0:
        count += number 

print(count)



