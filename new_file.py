# 5!    1*2*3*4*5

n = 5
num = 1
for x in range(2, n+1):
    num *= x

for idx, char in enumerate("text"):
    if char != 'e':
        print(f'{idx} {char}')
print(f'num = {num}')

num2 = 1
x = 2
while x <= n:
    num2 *= x
    x += 1

print(f'num2 = {num2}')


def factorial(n):
    num = 1
    for x in range(2, n+1):
        num *= x
    return num

print(f'fun1 {factorial(5)}')


def factorial2(n):
    if n > 1:
        return n * factorial2(n-1)
    elif n == 1:
        return 1



print(f'fun2 {factorial2(5)}')


list_elems = ['1jfjj23', '14', '1l', 'werw4t', 'hrty4']
min = list_elems[0]
for x in list_elems:
    if len(x) <= len(min):
        min = x
print(min)

print([1,2,4,5,63,535,35,235,23,4,124,323,5,235,2])
print(list(set([1,2,4,5,63,535,35,235,23,4,124,323,5,235,2])))
print(['a',2,'f',4,5])
print(set(['a',2,'f',4,5]))

v = {'id': 12342, 'name': "Лёша", 'sity': 'Воронеж'}
print(v)

list_elems = ['Алёша', 'Степашка', 'Ёжина', 'Банан', 'Кифирчик']
len_text = dict()
for idx, x in enumerate(list_elems):
    len_text[f'obj_{idx}'] = {
        'name': x,
        'len_name': len(x),
        'num': idx+1
    }

list_elems = ['Алёша', 'Степашка', 'Ёжина', 'Банан', 'Кифирчик', 'Бананa']
svin = dict()
minel = list_elems[0]
maxel = ""
for idx, x in enumerate(list_elems):
    if len(x) <= len(minel):
        minel = x
    if len(x) >= len(maxel):
        maxel = x
svin[minel]={
    'len': len(minel),
    'num': idx
}
svin[maxel]={
    'len': len(maxel),
    'num': idx
}
print(svin)