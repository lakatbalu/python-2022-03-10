i=0
while i<=10:
    print(i)
    i += 1


#min = 1
#max = 10
#e = input("gondolj egy számra 1 és 10 között")
#while guess != int(e):
#    guess = (min + max)/2
#    if guess == int(e):
#        print("Nyertél")
#    elif guess > int(e):
#        print("Kisebbre gondoltam")
#        max = guess
#    else:
#        print("Nagyobbra gondoltam")
#        min = guess


print("Gondolj egy számra")

min = 1
max = 10
answer = "x"
prev_guess = -1
while answer != "e":
    if guess == prev_guess:
        print("Ne szórakozz!")
        answer = "e"
    guess = (min + max) // 2
    print(f"""A szám amire gondoltam: {guess}
    Válassz kérlek!
    
    e - egyenlő
    k - kisebb
    n - nagyobb""")
    answer = input("Mi a válaszod?")

    if answer == "k":
        max = guess
    elif answer == "n":
        min = guess
    elif answer == "e":
        print("Kitaláltad")
    else:
        print("nem jó válasz")



