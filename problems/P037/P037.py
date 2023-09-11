a = input("input : ").split(' ')
m = []
A = 1
while True:
    b = input(f"input {A} : ")
    if b == 'END':
        break
    m.append(b)
    A += 1
for x1 in a:
    for x2 in m:
        if x1 == x2:
            a.remove(x1)
        if x1.endswith('.'):
            if x1 == x2 + '.':
                a.insert(a.index(x1) , '.')
                a.remove(x1)
        if x1.endswith(','):
            if x1 == x2 + ',':
                a.insert(a.index(x1) , ',')
                a.remove(x1)
        if x1.endswith('!'):
            if x1 == x2 + '!':
                a.insert(a.index(x1) , '!')
                a.remove(x1)
        if x1.endswith('?'):
            if x1 == x2 + '?':
                a.insert(a.index(x1) , '?')
                a.remove(x1)
print(str(" ".join(a)))