def P037(number):
    for x1 in number:
        for x2 in m:
            if x1 == x2:
                number.remove(x1)
            if x1.endswith('.'):
                if x1 == x2 + '.':
                    number.insert(number.index(x1) , '.')
                    number.remove(x1)
            if x1.endswith(','):
                if x1 == x2 + ',':
                    number.insert(number.index(x1) , ',')
                    number.remove(x1)
            if x1.endswith('!'):
                if x1 == x2 + '!':
                    number.insert(number.index(x1) , '!')
                    number.remove(x1)
            if x1.endswith('?'):
                if x1 == x2 + '?':
                    number.insert(number.index(x1) , '?')
                    number.remove(x1)
    return str(" ".join(number))
if __name__ == "__main__":
    a = input("input : ").split(' ')
    m = []
    A = 1
    while True:
        b = input(f"input {A} : ")
        if b == 'END':
            break
        m.append(b)
        A += 1
    answer = P037(a)
    print(answer)