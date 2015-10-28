# coding: utf-8
import pilasengine

pilas = pilasengine.iniciar()



def iniciar_juego():
    pilas.escenas.PantallaJuego()
def salir_del_juego():
    pilas.terminar()
    

class Rzck(pilasengine.actores.Actor):
    def iniciar(self):
     
        self.imagen= self.pilas.imagenes.cargar_grilla("pingu.png",10)
        self.x= 0
        self.y= -150
class PantallaBienvenida(pilasengine.escenas.Escena):

    def iniciar(self):
        pilas.fondos.Pasto()
        
        pilas.actores.Menu(
        [
            ('iniciar juego', iniciar_juego),
            ('salir', salir_del_juego),
        ])


class PantallaJuego(pilasengine.escenas.Escena):
    def iniciar(self):
         juego=Juego()
         juego.iniciar()
                  
class Juego():
    puntaje = pilas.actores.Puntaje(-280, 200, color=pilas.colores.violeta)    

    def iniciar(self):
        
        pilas.fondos.Volley()
        self.puntaje = pilas.actores.Puntaje(-280, 200, color=pilas.colores.violeta)
        rzck = Rzck(pilas)
        rzck.aprender("arrastrable")
        bomba= pilas.actores.Bomba() *10
        pilas.colisiones.agregar(rzck, bomba,self.cuando_colisiona)
        aceitunas=pilas.actores.Aceituna()*10
        pilas.colisiones.agregar(rzck, aceitunas,self.cuando_colisiona1)
        una_tarea = pilas.tareas.siempre(5, self.agregar_aceituna,aceitunas)
        
    def agregar_aceituna(self, aceitunas):
        aceituna=pilas.actores.Aceituna()*2
        aceitunas.agregar(aceituna)
    
    def cuando_colisiona(self, rzck, bomba):
        bomba.explotar()
        self.puntaje.aumentar (10)
        
    def cuando_colisiona1(self, rzck, banana):
        banana.eliminar()
        self.puntaje.reducir(10)
        if (self.puntaje.texto=="-10"):
            pilas.escenas.PantallaBienvenida()
            #rzck.eliminar()
            #texto = pilas.actores.Texto ("juego terminado")
            #pilas.fondos.Noche()                                                                                  



pilas.escenas.vincular(PantallaBienvenida)
pilas.escenas.PantallaBienvenida()
pilas.escenas.vincular(PantallaJuego)
pilas.ejecutar()