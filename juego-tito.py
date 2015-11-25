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
    pausado=False
    
    
    def comer_banana(self,pepa,banana):
        banana.eliminar()
        self.pepa.imagen.definir_cuadro(4)
        pilas.tareas.agregar(2,self.pepa.imagen.definir_cuadro,0)
        self.puntaje.aumentar(20)
        if (int(self.puntaje.texto)>450):
            texto=pilas.actores.Texto("You Win")
            texto.color = pilas.colores.Color(250, 250, 250)
            pilas.fondos.Espacio()
            pepa.eliminar()
            pilas.tareas.agregar(5,pilas.escenas.PantallaBienvenida)
    
    def explotar_bomba(self,pepa,bomba):
        bomba.explotar()
        pilas.camara.vibrar(5,2)
        
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
        self.pepa=Pepa(pilas)
        pilas.eventos.mueve_mouse.conectar(self.pepa.mover_a_la_posicion_del_mouse,id="mover")
        banana=pilas.actores.Banana()*30
        self.bomba=pilas.actores.Bomba()*3
        pilas.colisiones.agregar(self.pepa,banana,self.comer_banana)
        pilas.colisiones.agregar(self.pepa,self.bomba,self.explotar_bomba)
        self.boton=pilas.actores.Boton(245,215)
        self.boton.conectar_presionado(self.boton_pausa)
        pilas.eventos.pulsa_tecla_escape.conectar(self.ir_inicio)
        
    def boton_pausa(self):
        if(self.pausado):
            self.pausado=False
            self.boton.pintar_normal()
            self.texto.eliminar()
            pilas.eventos.mueve_mouse.conectar(self.pepa.mover_a_la_posicion_del_mouse,id="mover")
            self.agrega()
        else:
            self.boton.pintar_presionado()
            self.texto=pilas.actores.Texto("Pausado")
            self.texto.x=245
            self.texto.y=215
            self.pausado=True
            pilas.eventos.mueve_mouse.desconectar_por_id("mover") 
            self.tarea.terminar()
            self.tarea2.terminar()
        
    def ir_inicio(self):
        pilas.escenas.PantallaBienvenida()     
        
    def agregar_bombas(self):
        
        nueva_bomba=pilas.actores.Bomba()
        nueva_bomba.hacer(pilas.comportamientos.Orbitar,pilas.azar(-300,280),pilas.azar(-240,220),pilas.azar(1,100),10)          
        self.bomba.agregar(nueva_bomba)
        
    def agregar_bombas_lineales(self):
        bomba=pilas.actores.Bomba()
        bomba.x =  [-200,pilas.azar(-300,280)]
        bomba.y =[-150,pilas.azar(-240,220)]   
        self.bomba.agregar(bomba)
    def agrega(self):
        self.tarea=pilas.tareas.siempre(2,self.agregar_bombas)
        self.tarea2=pilas.tareas.siempre(3,self.agregar_bombas_lineales)
    

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