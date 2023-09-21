def P019(number_1):
    ouput = []
    a = [1]
    b = [1 , 1]
    if len(a) <= number_1:
        ouput.append(a)
    if len(b) <= number_1:
        ouput.append(b)
    while len(a) <= number_1 and len(b) <= number_1:
        a = [1]
        if len(b) <= number_1:
            x = 0
            y = 1
            while y < len(b):
                a.append(b[x] + b[y])
                x += 1 
                y += 1
            a.append(1)
            if len(a) <= number_1 :
                ouput.append(a)
        if len(a) <= number_1:
            b = [1]
            x = 0
            y = 1
            while y < len(a):
                b.append(a[x] + a[y])
                x += 1
                y += 1
            b.append(1)
            if len(b) <= number_1:
                ouput.append(b)
    return ouput
if __name__ == "__main__":
    INPUT = int(input('int : '))
    answer = P019(INPUT)
    for IXI in answer:
        print(IXI)