i = 0
while i<3: #True, False
    print('HELLO')
    print('Hello '+str(i))
    i += 1
    print('Hello '+str(i))
print('after while')

print('---------------------------')
j = 0
while j < 10:
    print('print("Hello World X '+(j*12).__str__()+ ' ")')
    j = j + 1
print(j*12)

print('---------------------------')
k = 0
a = 0
while k < 10:
    if k%2 == 0:
        a = a + 1
    print('print("Hello World X '+(k*12).__str__()+ ' ")')
    k = k + 1
print('after while')
print(a)
