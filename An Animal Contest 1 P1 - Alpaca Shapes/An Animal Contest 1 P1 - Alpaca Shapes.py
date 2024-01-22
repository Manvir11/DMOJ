S, R = map(int, input().split())
Square = S*S
Circle = 3.14*(R*R)
if Square>Circle:
    print("SQUARE")
else:
    print("CIRCLE")
