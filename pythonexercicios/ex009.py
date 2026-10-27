n = int(input("Digite um numero para aparecer sua tabuada:"))
print("=" * 12)
for i in range (0,11):
    res = i*n
    print("{} X {:2} = {}".format(n, i, res))
print("=" * 12)
    