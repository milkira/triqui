def tablero(t):
    print("")
    print(t[0] if t[0] else " ", "|", t[1] if t[1] else " ", "|", t[2] if t[2] else " ")
    print("--+---+--")
    print(t[3] if t[3] else " ", "|", t[4] if t[4] else " ", "|", t[5] if t[5] else " ")
    print("--+---+--")
    print(t[6] if t[6] else " ", "|", t[7] if t[7] else " ", "|", t[8] if t[8] else " ")
    print("")

def triqui(t):
    c = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for a, b, c in c:
        if t[a] == t[b] == t[c] != "":
            return True
    return False

def jugar():
    t = [""] * 9
    turno = "X"
    for _ in range(9):
        tablero(t)
        while True:
            posicion = input(f"Turno de {turno}. Ingrese posición (0-8): ")
            if posicion.isdigit() and 0 <= int(posicion) <= 8 and t[int(posicion)] == "":
                t[int(posicion)] = turno
                break
            print("Posición inválida. Intente de nuevo.")
        if triqui(t):
            tablero(t)
            
            print(turno, "ha ganado!")
            return
        turno = "O" if turno == "X" else "X"
    tablero(t)
    print("¡Empate!")

jugar()

ojala que tegas suerte