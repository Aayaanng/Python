tuple = (1,2,3,4,5,6,7,8,9,10,"one","two","three","four","five","six","seven","eight","nine","ten")
print(tuple)
print(tuple[3:9])
print(tuple[2:10])
print(tuple[9::-1])
print(tuple[12])

Aayaann = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"} 
print(Aayaann)
print(len(Aayaann))
print(Aayaann.keys())
print(Aayaann.values())
a = Aayaann.pop(10)
print(a)
print(Aayaann)
b = Aayaann.pop(5)
print(b)
print(Aayaann)   
for i in Aayaann.values():
    print(i)
for i in Aayaann.keys():
    print(i)
for i in Aayaann:
    print(Aayaann)
Aayaann[10] = a
print(Aayaann)

set = {1,2,3,4,5,6,7,8,9,10}
print(set)
set.add(11)
print(set)
set.remove(6)
print(set)
set.add(3)
print(set)
print("i")
for i in set:
    print(set)
for i in Aayaann:
    print(Aayaann)
for d_key, d_value in Aayaann.items():
    print(d_key,' ', d_value)
#hw do this l\with list tuple and set
for i in set:
    print(i)
