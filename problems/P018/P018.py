a = int(input())
def ispreme (a):
    ispreme = True
    for d in range(2 , a):
        if a % d == 0:
            ispreme = False
            break
    return ispreme
for c in range(2 , a):
    if ispreme(c) and ispreme(c + 2):
        print(c , c + 2)