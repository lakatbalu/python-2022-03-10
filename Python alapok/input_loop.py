# name = input("Mi a neved?")
# count = input(f"Hányszor írjuk ki a neved {name}?")
# for i in range(int(count)):
#     print(f"{i+1}. {name}")

# months = ["január", "február", "március"]
# for month in months:
#     print(f"Az év egyik hónapja {month}")

numbers = [3,5,98,55,33,10,124]
count = 0

for i in numbers:
    #count = count+i
    count += i
print(count)
