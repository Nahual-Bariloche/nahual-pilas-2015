# coding: utf-8
import pilasengine

pilas = pilasengine.iniciar()
pilas.fondos.Volley()
puntaje = pilas.actores.Puntaje(-280, 200, color=pilas.colores.violeta)
class Rzck(pilasengine.actores.Actor):
    def iniciar(self):
     
        self.imagen= self.pilas.imagenes.cargar_grilla("pingu.png",10)
        self.x= 0
        self.y= -150
        
rzck = Rzck(pilas)

rzck.aprender("arrastrable")



bomba= pilas.actores.Bomba() *100

def cuando_colisiona(rzck, bomba):
    
    bomba.explotar()
    puntaje.aumentar (10)
pilas.colisiones.agregar(rzck, bomba, cuando_colisiona)


pilas.ejecutar()