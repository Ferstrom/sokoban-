class Sokoban:
    """
        Definimos los componentes
    
        0 - Cajas
        1 - Paredes 
        2 - Muñeco
        3 - Camino
        4 - Metas
        5 - Muñeco-meta
        6 - Caja-meta
    """

    """ 
    Reglas validas para moverse (Arriba, Derecha, Abajo, Izquierda)
    
    00 - Muñeco, camino -> [2,3] -> [3,2]
    01 - Muñeco, espacio
    02 - Muñeco, caja, espacio
    03 - Muñeco, caja, meta
    04 - Muñeco, caja_meta, espacio
    05 - Muñeco, caja_meta, meta
    06 - Muñeco_meta, camino
    07 - Muñeco_meta, espacio
    08 - Muñeco_meta, caja, espacio
    09 - Muñeco_meta, caja, meta
    10 - Muñeco_meta, caja_meta, espacio
    11 - Muñeco_meta, caja_meta, meta

    Derecha -> muneco_columna + 1 
    Izquierda -> muneco_columna - 1
    Abajo -> muneco_fila + 1
    Arriba -> muneco_fila - 1

    """ 

    mapa = [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,3,3,1,3,3,3,3,3,3,3,3,3,3,1],
        [1,3,3,1,3,2,3,3,3,3,3,3,3,3,1],
        [1,3,3,1,3,3,3,0,3,3,3,3,3,4,1],
        [1,3,3,3,3,3,3,0,3,3,3,3,3,4,1],
        [1,3,3,3,3,3,3,0,4,4,3,3,3,4,1],
        [1,3,3,3,3,3,3,4,0,4,4,4,3,3,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    ]

    muneco_fila = 2
    muneco_columna = 5

    def imprimirMapa(self):
        for fila in self.mapa:
            print(fila)

    def jugar(self):
        self.imprimirMapa()

    def moverDerecha(self):
        print("mover Derecha")
        #00 - Muñeco, camino -> [2,3] -> [3,2]
        if self.mapa[self.muneco_fila][self.muneco_columna] == 2 and self.mapa[self.muneco_fila][self.muneco_columna + 1] == 3:
            self.mapa[self.muneco_fila][self.muneco_columna] = 3
            self.mapa[self.muneco_fila][self.muneco_columna + 1] = 2
            self.muneco_columna += 1
        #Muñeco,meta
        elif self.mapa[self.muneco_fila][self.muneco_columna] == 2 and self.mapa[self.muneco_fila][self.muneco_columna + 1] == 4:
            self.mapa[self.muneco_fila][self.muneco_columna] = 3
            self.mapa[self.muneco_fila][self.muneco_columna + 1] = 5
            self.muneco_columna += 1
        #Muñeco,caja,espacio
        elif self.mapa[self.muneco_fila][self.muneco_columna] == 2 and self.mapa[self.muneco_fila][self.muneco_columna + 1] == 0 and self.mapa[self.muneco_fila][self.muneco_columna + 2] == 3:
            self.mapa[self.muneco_fila][self.muneco_columna] = 3
            self.mapa[self.muneco_fila][self.muneco_columna + 1] = 2
            self.mapa[self.muneco_fila][self.muneco_columna + 2] = 0
            self.muneco_columna += 1
        #Muñeco,caja,meta
        elif self.mapa[self.muneco_fila][self.muneco_columna] == 2 and self.mapa[self.muneco_fila][self.muneco_columna + 1] == 0 and self.mapa[self.muneco_fila][self.muneco_columna + 2] == 4:
            self.mapa[self.muneco_fila][self.muneco_columna] = 3
            self.mapa[self.muneco_fila][self.muneco_columna + 1] = 2
            self.mapa[self.muneco_fila][self.muneco_columna + 2] = 6
            self.muneco_columna += 1
        #Muñeco,caja_meta,espacio
        elif self.mapa[self.muneco_fila][self.muneco_columna] == 2 and self.mapa[self.muneco_fila][self.muneco_columna + 1] == 6 and self.mapa[self.muneco_fila][self.muneco_columna + 2] == 3:
            self.mapa[self.muneco_fila][self.muneco_columna] = 3
            self.mapa[self.muneco_fila][self.muneco_columna + 1] = 5
            self.mapa[self.muneco_fila][self.muneco_columna + 2] = 0
            self.muneco_columna += 1
        #Muñeco,caja_meta,meta
        elif self.mapa[self.muneco_fila][self.muneco_columna] == 2 and self.mapa[self.muneco_fila][self.muneco_columna + 1] == 6 and self.mapa[self.muneco_fila][self.muneco_columna + 2] == 4:
            self.mapa[self.muneco_fila][self.muneco_columna] = 3
            self.mapa[self.muneco_fila][self.muneco_columna + 1] = 5
            self.mapa[self.muneco_fila][self.muneco_columna + 2] = 6
            self.muneco_columna += 1
        #Muñeco_meta,espacio
        elif self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila][self.muneco_columna + 1] == 3:
            self.mapa[self.muneco_fila][self.muneco_columna] = 4
            self.mapa[self.muneco_fila][self.muneco_columna + 1] = 2
            self.muneco_columna += 1
        
        #Muñeco,caja_meta,meta
        elif self.mapa[self.muneco_fila][self.muneco_columna] == 2 and self.mapa[self.muneco_fila][self.muneco_columna + 1] == 0 and self.mapa[self.muneco_fila][self.muneco_columna + 2] == 4:
            self.mapa[self.muneco_fila][self.muneco_columna] = 3
            self.mapa[self.muneco_fila][self.muneco_columna + 1] = 2
            self.mapa[self.muneco_fila][self.muneco_columna + 2] = 6
            self.muneco_columna += 1
        #Muñeco_meta,meta
        elif self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila][self.muneco_columna + 1] == 4:
            self.mapa[self.muneco_fila][self.muneco_columna] = 4
            self.mapa[self.muneco_fila][self.muneco_columna + 1] = 5
            self.muneco_columna += 1
        #Muñeco_meta,caja,espacio
        elif self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila][self.muneco_columna + 1] == 0 and self.mapa[self.muneco_fila][self.muneco_columna + 2] == 3:
            self.mapa[self.muneco_fila][self.muneco_columna] = 4
            self.mapa[self.muneco_fila][self.muneco_columna + 1] = 2
            self.mapa[self.muneco_fila][self.muneco_columna + 2] = 0
            self.muneco_columna += 1
        #Muñeco_meta,caja,meta
        elif self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila][self.muneco_columna + 1] == 0 and self.mapa[self.muneco_fila][self.muneco_columna + 2] == 4:
            self.mapa[self.muneco_fila][self.muneco_columna] = 4
            self.mapa[self.muneco_fila][self.muneco_columna + 1] = 2
            self.mapa[self.muneco_fila][self.muneco_columna + 2] = 6
            self.muneco_columna += 1
        #Muñeco_meta,caja_meta,espacio
        elif self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila][self.muneco_columna + 1] == 6 and self.mapa[self.muneco_fila][self.muneco_columna + 2] == 3:
            self.mapa[self.muneco_fila][self.muneco_columna] = 4
            self.mapa[self.muneco_fila][self.muneco_columna + 1] = 5
            self.mapa[self.muneco_fila][self.muneco_columna + 2] = 0
            self.muneco_columna += 1
        #Muñeco_meta,caja_meta,meta
        elif self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila][self.muneco_columna + 1] == 6 and self.mapa[self.muneco_fila][self.muneco_columna + 2] == 4:
            self.mapa[self.muneco_fila][self.muneco_columna] = 4
            self.mapa[self.muneco_fila][self.muneco_columna + 1] = 5
            self.mapa[self.muneco_fila][self.muneco_columna + 2] = 6
            self.muneco_columna += 1

    def moverIzquierda(self):
        print("mover izquierda")
        if self.mapa[self.muneco_fila][self.muneco_columna] == 2 and self.mapa[self.muneco_fila][self.muneco_columna - 1] == 3:
            self.mapa[self.muneco_fila][self.muneco_columna] = 3
            self.mapa[self.muneco_fila][self.muneco_columna - 1] = 2
            self.muneco_columna -= 1
         #Muñeco,meta
        elif self.mapa[self.muneco_fila][self.muneco_columna] == 2 and self.mapa[self.muneco_fila][self.muneco_columna - 1] == 4:
            self.mapa[self.muneco_fila][self.muneco_columna] = 3
            self.mapa[self.muneco_fila][self.muneco_columna - 1] = 5
            self.muneco_columna -= 1
        #Muñeco,caja,espacio
        elif self.mapa[self.muneco_fila][self.muneco_columna] == 2 and self.mapa[self.muneco_fila][self.muneco_columna - 1] == 0 and self.mapa[self.muneco_fila][self.muneco_columna - 2] == 3:
            self.mapa[self.muneco_fila][self.muneco_columna] = 3
            self.mapa[self.muneco_fila][self.muneco_columna - 1] = 2
            self.mapa[self.muneco_fila][self.muneco_columna - 2] = 0
            self.muneco_columna -= 1
        #Muñeco,caja,meta
        elif self.mapa[self.muneco_fila][self.muneco_columna] == 2 and self.mapa[self.muneco_fila][self.muneco_columna - 1] == 0 and self.mapa[self.muneco_fila][self.muneco_columna - 2] == 4:
            self.mapa[self.muneco_fila][self.muneco_columna] = 3
            self.mapa[self.muneco_fila][self.muneco_columna - 1] = 2
            self.mapa[self.muneco_fila][self.muneco_columna - 2] = 6
            self.muneco_columna -= 1
        #Muñeco,caja_meta,espacio
        elif self.mapa[self.muneco_fila][self.muneco_columna] == 2 and self.mapa[self.muneco_fila][self.muneco_columna - 1] == 6 and self.mapa[self.muneco_fila][self.muneco_columna - 2] == 3:
            self.mapa[self.muneco_fila][self.muneco_columna] = 3
            self.mapa[self.muneco_fila][self.muneco_columna - 1] = 5
            self.mapa[self.muneco_fila][self.muneco_columna - 2] = 0
            self.muneco_columna -= 1
    
        
    def moverAbajo(self):
        print("mover Abajo")
        if self.mapa[self.muneco_fila][self.muneco_columna] == 2 and self.mapa[self.muneco_fila + 1][self.muneco_columna] == 3:
            self.mapa[self.muneco_fila][self.muneco_columna] = 3
            self.mapa[self.muneco_fila + 1][self.muneco_columna] = 2
            self.muneco_fila += 1

        elif self.mapa[self.muneco_fila][self.muneco_columna] == 2 and self.mapa[self.muneco_fila + 1][self.muneco_columna] == 4:
            self.mapa[self.muneco_fila][self.muneco_columna] = 3
            self.mapa[self.muneco_fila + 1][self.muneco_columna] = 5
            self.muneco_fila += 1

        elif self.mapa[self.muneco_fila][self.muneco_columna] == 2 and self.mapa[self.muneco_fila + 1][self.muneco_columna] == 4:
            self.mapa[self.muneco_fila][self.muneco_columna] = 3
            self.mapa[self.muneco_fila + 1][self.muneco_columna] = 5
            self.muneco_fila += 1

        elif self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila + 1][self.muneco_columna] == 4:
            self.mapa[self.muneco_fila][self.muneco_columna] = 4
            self.mapa[self.muneco_fila + 1][self.muneco_columna] = 5
            self.muneco_fila += 1

        elif self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila + 1][self.muneco_columna] == 3:
            self.mapa[self.muneco_fila][self.muneco_columna] = 4
            self.mapa[self.muneco_fila + 1][self.muneco_columna] = 2
            self.muneco_fila += 1

    def moverArriba(self):
        print("mover Arriba")
        if self.mapa[self.muneco_fila][self.muneco_columna] == 2 and self.mapa[self.muneco_fila - 1][self.muneco_columna] == 3:
            self.mapa[self.muneco_fila][self.muneco_columna] = 3
            self.mapa[self.muneco_fila - 1][self.muneco_columna] = 2
            self.muneco_fila -= 1

        elif self.mapa[self.muneco_fila][self.muneco_columna] == 2 and self.mapa[self.muneco_fila - 1][self.muneco_columna] == 4:
            self.mapa[self.muneco_fila][self.muneco_columna] = 3
            self.mapa[self.muneco_fila - 1][self.muneco_columna] = 5
            self.muneco_fila -= 1

        elif self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila - 1][self.muneco_columna] == 4:
            self.mapa[self.muneco_fila][self.muneco_columna] = 4
            self.mapa[self.muneco_fila - 1][self.muneco_columna] = 5
            self.muneco_fila -= 1

        elif self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila - 1][self.muneco_columna] == 3:
            self.mapa[self.muneco_fila][self.muneco_columna] = 4
            self.mapa[self.muneco_fila - 1][self.muneco_columna] = 2
            self.muneco_fila -= 1

        elif self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila - 1][self.muneco_columna] == 3:
            self.mapa[self.muneco_fila][self.muneco_columna] = 6
            self.mapa[self.muneco_fila - 1][self.muneco_columna] = 5
            self.muneco_fila -= 1
            
    def jugar(self):
        while True:
            self.imprimirMapa()
            opciones = "d-derecha"
            print(opciones)
            movimiento = input("Moverse a: ")
            if movimiento == "d":
                self.moverDerecha()
            elif movimiento == "s":
                self.moverAbajo()
            elif movimiento == "a":
                self.moverIzquierda()
            elif movimiento == "w":
                self.moverArriba()
            

juego = Sokoban()
juego.jugar()