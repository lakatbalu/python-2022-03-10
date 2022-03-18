fruit = "cseresznye"
print(fruit[3])

#szeletelés - slicing

print(fruit[2:7])
print(fruit[2:7:2])
print(fruit[2:])
print(fruit[:5])
print(fruit[::-1])
print(fruit[:-3])

print(fruit.upper())

print(len(fruit))

#hasznos string függvények
print("eresz" in fruit)
print(fruit.endswith("nye"))
print(fruit.startswith("cser"))
print("1223434".isdecimal())
print("    sdfs  d   ".strip())   #megszabadítja a felesleges space-ktől balról és jobbról, középről nem
print(fruit.index("re"))          #hanyadik indexen van a megadott karakter
print(fruit.index("e", 3))        #a 3. karaktertől keresi az e betűt
print(",".join(["a", "b", "c"]))

paragraph = "alma körte barack meggy"
fruits = paragraph.split()
print(fruits)
paragraph = "alma,körte,barack,meggy"
fruits = paragraph.split(",")
print(fruits)





