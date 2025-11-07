# Function dimension
# Inputs: matriz, matriz de lista de listas, por referencia
# Outputs: filas, columnas, dimensión de la matriz.
def dimension (matriz):
    filas = len(matriz)
    if filas > 0:
        columnas = len(matriz[0])
    else:
        columnas = 0
    return filas, columnas

# Function imprimir
# Inputs: A, matriz de lista de listas, por referencia
# Outputs: la matriz impresa en pantalla.
def imprimir (A):
    f, c = dimension (A)
    for i in range(0, f):
        print ("| ", end = "") # end = "" es para no imprimir un salto de línea al final del print
        for j in range(0, c):
            print("{:>5} |".format(str(A[i][j])), end = "")
        print("") #Imprime un salto de línea


def Mensaje(mensaje):
    ascii = [ord(c) for c in mensaje]
    bloques = []
    while ascii:
        bloque = ascii[:16]
        ascii= ascii[16:]

        while len(bloque) < 16:
            bloque.append(0)

        matriz = []
        for i in range(0, 16, 4):
            matriz.append(bloque[i:i+4])
        bloques.append(matriz)
    return bloques



def suma_matrices(m1, m2):
    n = len(m1)
    m = len(m1[0])
    c = []
    for i in range(n):
        fila = []
        for j in range(m):
            r = m1[i][j] + m2[i][j]
            fila.append(r)
        c.append(fila)
    return c


def cifrar_mensaje(mensaje, a):
    nueva = Mensaje(mensaje)
    resultado = []

    for matriz in nueva:
        c = suma_matrices(matriz, a)
        resultado.append(c)

    return resultado


A = [
    [2, 3, 1, 1],
    [1, 2, 3, 1],
    [1, 1, 2, 3],
    [3, 1, 1, 2]
]

texto = "yvATYGSHDVB LDFKAJ NBXLÑ"
resultado = cifrar_mensaje(texto, A)
matrimensaje=Mensaje
imprimir(resultado[1])