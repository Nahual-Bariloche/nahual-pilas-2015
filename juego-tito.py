# coding: utf-8
import pilasengine

pilas = pilasengine.iniciar()
class Pepa (pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen=self.pilas.imagenes.cargar_grilla("pingu.png", 10)
        self.x=300
        self.y=205
        
    def mover_a_la_posicion_del_mouse(self, evento):
        self.x=evento.x
        self.y=evento.y
            
def comer_banana(pepa,banana):
    banana.eliminar()
    puntaje.aumentar()

def explotar_bomba(pepa,bomba):
    bomba.explotar()
    puntaje.reducir(5)
    
pilas.fondos.Tarde()  
        
pepa=Pepa(pilas)

pilas.eventos.mueve_mouse.conectar(pepa.mover_a_la_posicion_del_mouse)

banana=pilas.actores.Banana()*15

bomba=pilas.actores.Bomba()*5

pilas.colisiones.agregar(pepa,banana,comer_banana)

pilas.colisiones.agregar(pepa,bomba,explotar_bomba)

puntaje=pilas.actores.Puntaje(-250,220,color=pilas.colores.blanco)


pilas.ejecutar()
