f = open('test.txt', 'r')
x = f.read()
print(x)
f.close()

f = open('test.txt', 'r')
x = f.readline()
print(x)
f.close()

f = open('test.txt', 'r')

for a in range(0, 10):
    x = f.read()
    print(x)

f.close()