asp = prom = prom1 = ing = genero1 = genero2 = 0
edad = []
gen = ip = tac = " "
genero = []
tacones = []
promtac = promtac2 = 0
x = 0
i = 0
s = 0
w = 0

print("Indique el genero del aspirante con M o F")
print("Indique si posee tacones o iPhone con S o N")
print("------------------------")
for x in range(0,20):
    asp = int(input("Edad del aspirante: "))
    i += 1
    gen =(input("Genero del aspirante: "))
    tac = input("Posee iPhone: ")
    ip = input("Posee Tacones: ")
    print("------------------------")
    genero.append(gen)
    edad.append(asp)
    if tac == "S":
        tacones.append(asp)
        w += 1
    if ip == "S":
        s += 1
prom = sum(edad)
prom1 = prom / 20
genero1 = genero.count("M")
genero2 = genero.count("F")
promtac = sum(tacones)
promtac2 = promtac/w


print("Promedio de edad: ",prom1)
print("Cantidad de damas: ", genero2)
print("Cantidad de caballeros: ", genero1)
print("Cantidad de personas con iPhone: ", s)
print("Promedio de personas que usan tacones: ",promtac2)
