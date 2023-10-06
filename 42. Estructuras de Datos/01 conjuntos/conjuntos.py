a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
b = {90, 67,  0}
c = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}

# Unión
union = a | b
print(f"Union a u b = {union}")

# Intersección
interseccion = a & b
print(f"Inrersección de 'a' n 'b' = {interseccion}")

# Diferencia
diferencia_a = a - b
print(f"Direncia de a - b = {diferencia_a}")

# Diferencia
diferencia_b = b - a
print(f"Diferencia de b - a = {diferencia_b}")

# Diferencia símetrica
simetrica = a ^ b
print(f"Diferencía simétrica {simetrica}") # valores de a que no se repiten de b y valores de b que no se repiten en a

# Si a es un subconjunto de b
subconjunto_a = a.issubset(b)
print(f"¿A es subconjunto de B? = {subconjunto_a}")

# Si a es un superconjunto de b
super_conjunto_a = a.issuperset(b)
print(f"¿A es super conjunto de B? = {super_conjunto_a}")

# Es un subset a b subsetjoin
subsetjoin = a.isdisjoint(b)
print(f"¿A es un disjoint de B? = {subsetjoin}") # que no se repitan ningun número de conjuntos de a y b


