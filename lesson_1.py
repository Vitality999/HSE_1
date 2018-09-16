import math
#lesson_1
a = 2 + 2 * 2
print(a)

#lesson_2
a = float(input('Введите длину квадрата\n'))
p = a*4
s = a*a
d = a**2 + a **2
c = math.sqrt(d)
m = (p, s, c)
print(m)

#lesson_3

a = int(input('введите a\n'))
b = int(input('введите b\n'))

if a == 5 and b == 6:
    b = 3
    a = 1

print(' a =', a, '\n', 'b =', b)

x = 324
x1 = x % 10
x2 = x % 100 // 10
x3 = x // 100
c = (x1 + x2 + x3)
print('Значение:', c)

#---------------------------------------------------
print(True > False)
print(False > True)
print('True больше')

#my_class == None
#type(None)
#is None
#is not None

xor = bool(a) ^ bool(b)

year = 2000
if year % 4 == 0 or year % 100 != 0 and year % 400 == 0:
    print('Високосный')
else:
    print('Не високосный')


st = []
sr = [True, None, 42]
st.extend(sr)
print(st)

f = [1, 2, 3, 4]
v = f[0]*f[2]*f[3]
print(v)

i = ['abz'
,'aabz'
,'Abz'
,'0.123'
,'00.123'
,'-0.123'
,'0123']
i.sort()
print(i)

ye = int(input('введите кол-во лет'))
pr = int(input('сумма'))
n = 1
while n <= ye:
    m = pr * 0.1
    n += 1
print(m)
