# Lists: ordered, mutable, allows duplicate elements
mylist = ["banana", "cherry", "apple"]
print(mylist)

mylist2 = list() #empty List
print(mylist2)

mylist2 = [5, True, "apple", "apple"] #doppelte elemente
print(mylist2)

item = mylist[1]
print(item)

for i in mylist: #alle elemente
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

#addieren zu einem spezifischen Platz