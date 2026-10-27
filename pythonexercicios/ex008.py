v = float(input("Digite um valor em metros: "))
print("O valor em metros e {}m, em decimetros e {}dc, em centimetros e {:.0f}mm, e em milimetros e {:.0f}mm".format(v, (v * 10), (v * 100), (v * 1000)))
print("O valor em metros e {}m, em kilometros e {}km, em hectometros e {}hm, e em decametros {}dm".format(v, (v * 0.001), (v * 0.01), (v * 0.1 )))