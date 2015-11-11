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
        pilas.tareas.siempre(5, self.agregar_aceituna,aceitunas)
        pilas.tareas.siempre(10,self.agregar_aceituna_orbitales,aceitunas)
        
    def agregar_aceituna(self, aceitunas):
        aceituna=pilas.actores.Aceituna()
        aceituna.x=[-200,pilas.azar(0,200)]
        aceituna.y=pilas.azar(-200,200)
        aceitunas.agregar(aceituna)
        
    def agregar_aceituna_orbitales(self,aceitunas):
         aceituna=pilas.actores.Aceituna()
         aceituna.hacer(pilas.comportamientos.Orbitar,pilas.azar(-200,200),pilas.azar(-300,300),pilas.azar(10,20),pilas.azar(20,30))  
         aceitunas.agregar(aceituna)
        
        
        
        
           
    
    def cuando_colisiona(self, rzck, bomba):
        bomba.explotar()
        self.puntaje.aumentar (10)
        if(int(self.puntaje.texto)>90):
            texto = pilas.actores.Texto ("aguantaaaaa")
            pilas.tareas.agregar(5,pilas.escenas.PantallaBienvenida)
        
    def cuando_colisiona1(self, rzck, banana):
        banana.eliminar()
        self.puntaje.reducir(10)
        if(int(self.puntaje.texto)<0):
            pilas.tareas.agregar(5,pilas.escenas.PantallaBienvenida)
            rzck.eliminar()
            texto = pilas.actores.Texto ("juego terminado")
            pilas.fondos.Noche()                                                                                  


pilas.escenas.vincular(PantallaBienvenida)
pilas.escenas.PantallaBienvenida()
pilas.escenas.vincular(PantallaJuego)
pilas.definir_pantalla_completa(True)


pilas.ejecutar()