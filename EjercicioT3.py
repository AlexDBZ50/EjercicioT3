def imprimir(mat):
    for f in mat:
        print(f)
    print()


def validar(lab, visitado, f, c):
    filas = len(lab)
    columnas = len(lab[0])

    if f < 0 or f >= filas:
        return False

    if c < 0 or c >= columnas:
        return False

    if lab[f][c] == 0:
        return False

    if visitado[f][c]:
        return False

    return True


def laberinto(lab, res, visitado, f, c, vidas, puntos):
    if validar(lab, visitado, f, c):

        vidas_raton = vidas
        puntos_raton = puntos

        if lab[f][c] == 1:
            puntos_raton += 1

        elif lab[f][c] == -1:
            vidas_raton -= 1

        elif lab[f][c] == -2:
            vidas_raton -= 2

        if vidas_raton <= 0:
            return False

        visitado[f][c] = True
        res[f][c] = 1

        print("Posicion actual:", f, c)
        print("Vidas del raton:", vidas_raton)
        print("Puntos del raton:", puntos_raton)
        imprimir(res)

        if f == 0 and c == 0:
            return True

        if laberinto(lab, res, visitado, f + 1, c, vidas_raton, puntos_raton):  # abajo
            return True

        if laberinto(lab, res, visitado, f, c + 1, vidas_raton, puntos_raton):  # derecha
            return True

        if laberinto(lab, res, visitado, f - 1, c, vidas_raton, puntos_raton):  # arriba
            return True

        if laberinto(lab, res, visitado, f, c - 1, vidas_raton, puntos_raton):  # izquierda
            return True

        visitado[f][c] = False
        res[f][c] = 0

    return False


lab = [
    [1, 1, 1, 1, 0, 1, 1, 1, 1],
    [-2, 0, 0, -1, 0, 1, 0, 1, 0],
    [1, 1, 0, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, -1, 0, 0, 0, -1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0],
    [-1, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, -1, 1, 1, 1, 0],
    [1, 0, 0, 1, 0, 1, 0, 1, 0],
    [1, 1, -1, 1, 1, 1, 0, 1, 1]
]

filas = len(lab)
columnas = len(lab[0])

res = [[0 for _ in range(columnas)] for _ in range(filas)]
visitado = [[False for _ in range(columnas)] for _ in range(filas)]

vidas_iniciales = 3
puntos_iniciales = 0

print("LABERINTO ORIGINAL:")
imprimir(lab)

print("BUSCANDO SALIDA...\n")

if laberinto(lab, res, visitado, 8, 0, vidas_iniciales, puntos_iniciales):
    print("PUDIMOS ESCAPAR!!!")
    print("CAMINO FINAL:")
    imprimir(res)
else:
    print("NO HAY SALIDA...!!!")
    