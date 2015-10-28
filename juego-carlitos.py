# coding: utf-8
import pilasengine

pilas = pilasengine.iniciar()

pilas.fondos.Selva()

def iniciar_juego():
     pilas.escenas.PantallaJuego()
    
  
def salir_del_juego():
    pilas.terminar()

menu=pilas.actores.Menu(
        [
            ('iniciar juego', iniciar_juego),
            ('salir', salir_del_juego),
        ])

class Pepa (pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen=self.pilas.imagenes.cargar_grilla("pingu.png", 10)
        self.x=300
        self.y=205
        
    def mover_a_la_posicion_del_mouse(self, evento):
        self.x=evento.x
        self.y=evento.y
        
class Juego():
    
    puntaje=pilas.actores.Puntaje(-250,220,color=pilas.colores.blanco)
    
    def comer_banana(self,pepa,banana):
        banana.eliminar()
        self.puntaje.aumentar(1)
    
    def explotar_bomba(self,pepa,bomba):
        bomba.explotar()
        self.puntaje.reducir(10)
         if (self.puntaje.texto == "-10"):
             texto=pilas.actores.Texto("fin")
             pilas.fondos.Blanco()
             pepa.eliminar()
             pilas.escenas.PantallaBienvenida()
    
    def iniciar(self):
        pilas.fondos.Tarde()
        self.puntaje=pilas.actores.Puntaje(-250,220,color=pilas.colores.blanco)  
        pepa=Pepa(pilas)
        pilas.eventos.mueve_mouse.conectar(pepa.mover_a_la_posicion_del_mouse)
        banana=pilas.actores.Banana()*30
        bomba=pilas.actores.Bomba()*5
        pilas.colisiones.agregar(pepa,banana,self.comer_banana)
        pilas.colisiones.agregar(pepa,bomba,self.explotar_bomba)


    def agregar_bombas(self):
        bomba.agregar(pilas.actores.Bomba(x=50,y=60))
    def agrega(self):
        pilas.tareas.siempre(2,agregar_bombas)
    
class PantallaBienvenida(pilasengine.escenas.Escena):

    def iniciar(self):
        self.fondo = self.pilas.fondos.Selva()
  
        pilas.actores.Menu(
        [
            ('iniciar juego', iniciar_juego),
            ('salir', salir_del_juego),
        ])
        

    def ejecutar(self):
        pass
        
class PantallaJuego(pilasengine.escenas.Escena):
    def iniciar(self):
         
         juego=Juego()
         juego.iniciar()
         menu.eliminar()
         juego.agrega()
    
pilas.escenas.vincular(PantallaBienvenida)              
pilas.escenas.vincular(PantallaJuego)
pilas.escenas.PantallaBienvenida()
pilas.ejecutar()