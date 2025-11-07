def MultiplicarMatrices(a, b):
    c = []
    n = len(a)
    m = len(a[0])
    z = len(b[0])

    for i in range(n):
        fila = []
        for j in range(z):
            fila.append(0)
        c.append(fila)

    for k in range(n):
        for l in range(z):
            for d in range(m):
                c[k][l] += a[k][d] * b[d][l]

    return c


Multiplicacion = MultiplicarMatrices(resultado[0], A)
print("\nResultado de la multiplicación de matrices:")
imprimir(Multiplicacion)
