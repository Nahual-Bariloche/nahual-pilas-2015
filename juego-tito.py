# coding: utf-8
import pilasengine

pilas = pilasengine.iniciar()

pilas.definir_pantalla_completa(True)

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
        self.puntaje.aumentar(20)
        if (int(self.puntaje.texto)>500):
            texto=pilas.actores.Texto("Lalalalala")
            texto.color = pilas.colores.Color(250, 250, 250)
            pilas.fondos.Espacio()
            pepa.eliminar()
            pilas.tareas.agregar(5,pilas.escenas.PantallaBienvenida)
            
    
    def explotar_bomba(self,pepa,bomba):
        bomba.explotar()
        self.puntaje.reducir(10)
        if (int(self.puntaje.texto)<0):
            texto=pilas.actores.Texto("Try Again")
            texto.color = pilas.colores.Color(0, 0, 0)
            pilas.fondos.Blanco()
            pepa.eliminar()
            pilas.tareas.agregar(5,pilas.escenas.PantallaBienvenida)

    def iniciar(self):
        pilas.fondos.Tarde()
        self.puntaje=pilas.actores.Puntaje(-250,220,color=pilas.colores.blanco)  
        pepa=Pepa(pilas)
        pilas.eventos.mueve_mouse.conectar(pepa.mover_a_la_posicion_del_mouse)
        banana=pilas.actores.Banana()*30
        self.bomba=pilas.actores.Bomba()*5
        pilas.colisiones.agregar(pepa,banana,self.comer_banana)
        pilas.colisiones.agregar(pepa,self.bomba,self.explotar_bomba)


    def agregar_bombas(self):
        
        nueva_bomba=pilas.actores.Bomba() 
        nueva_bomba.x =  [-200,pilas.azar(-300,280)]
        nueva_bomba.y =[-150,pilas.azar(-240,220)]           
        self.bomba.agregar(nueva_bomba)

    def agrega(self):
        pilas.tareas.siempre(2,self.agregar_bombas)
    


class PantallaBienvenida(pilasengine.escenas.Escena):

    def iniciar(self):
        self.fondo = self.pilas.fondos.Volley()

        pilas.actores.Menu(
        [
            ('iniciar juego', iniciar_juego),
            ('salir', salir_del_juego),
        ])
    def ejecutar(self):
        pass
        


class PantallaJuego(pilasengine.escenas.Escena):
    def iniciar(self):
        juego = Juego()
        juego.iniciar()
        juego.agrega()
        
pilas.escenas.vincular(PantallaBienvenida)


pilas.escenas.vincular(PantallaJuego)




pilas.ejecutar()