# Lists: ordered, mutable, allows duplicate elements
mylist = ["banana", "cherry", "apple"]
print(mylist)

mylist2 = list()   # empty List
print(mylist2)

mylist2 = [5, True, "apple", "apple"]  # doppelte elemente
print(mylist2)

item = mylist[1]
print(item)

for i in mylist:   # alle elemente
    print(i)

# checking ob gibts ein besonderen Element
if "banana" in mylist:
    print("yes")
else:
    print("no")

# wie lange ist meine Liste
print(len(mylist))

# addidtion von Elementen
mylist.append("lemon")
print(mylist)

# addieren zu einem spezifischen Platz
mylist.insert(1, "blueberry")
print(mylist)

# letzten item löschen
item = mylist.pop()
print(item)
print(mylist)

# spezifische Element löschen
item = mylist.remove("cherry")
print(mylist)

# reverse the list
item = mylist.reverse()
print(mylist)

# elemente sortieren
mylist3 = [4, 2, 9, 53]
print(mylist3)
item = mylist3.sort()
print(mylist3)

# neue organisierte Liste erzeugen
new_list = sorted(mylist3)
print(new_list)

# concat Liste
new_list2 = new_list + mylist
print(new_list2)

# alle elemente löschen
item = mylist.clear()
print(mylist)

# slicing Method
dieliste = [1, 2, 3, 4, 5]
dieliste2 = dieliste[1:5]  # falls [:5] -> fängt von Anfang an, falls [1:] geht zu ende
print(dieliste2)

dieliste = [1, 2, 3, 4, 5]
dieliste2 = dieliste[::2] # jeden zweiten Element wird ausgegeben
dieliste2 = dieliste[::-1] # die Liste umkehren
print(dieliste2)

# Liste kopieren und in die kopierte etwas addieren (originale bleibt wie sie ist)
list_org = ["banana", "cherry", "apple"]
# list_cpy = list_org.copy() # erste Option
# list_cpy = list(list_org) # zweite Option
list_cpy = list_org[:] # dritte Option
list_cpy.append("lemon")
print(list_cpy)
print(list_org)

# list comprehension - create list out of list
a = [1, 2, 3]
b = [i*i for i in a]
print(a)
print(b)
