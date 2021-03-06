# coding: utf-8
import pilasengine

pilas = pilasengine.iniciar()



def iniciar_juego():
    pilas.escenas.PantallaJuego()
def salir_del_juego():
    pilas.terminar()
    

class Rzck(pilasengine.actores.Actor):
    def iniciar(self):
     
        self.imagen= self.pilas.imagenes.cargar_grilla("pacman.png",4,4)
        self.escala=4
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
    pausado=False
    def iniciar(self):
        
        pilas.fondos.Volley()
        self.puntaje = pilas.actores.Puntaje(-280, 200, color=pilas.colores.violeta)
        rzck = Rzck(pilas)
        rzck.aprender("arrastrable")
        bomba= pilas.actores.Bomba() *10
        pilas.colisiones.agregar(rzck, bomba,self.cuando_colisiona)
        self.aceitunas=pilas.actores.Aceituna()*10
        pilas.colisiones.agregar(rzck,self.aceitunas,self.cuando_colisiona1)
        self.aceitunas_x=pilas.tareas.siempre(5, self.agregar_aceituna,self.aceitunas)
        self.aceitunas_y=pilas.tareas.siempre(10,self.agregar_aceituna_orbitales,self.aceitunas)
        self.boton_pausa=pilas.actores.Boton(230,215)
        
        self.boton_pausa.conectar_presionado(self.pausar)
        

        
        
       
        
        
    def pausar(self):
        if(self.pausado==True):
            self.pausado=False
            self.boton_pausa.pintar_normal()
            self.texto.eliminar()
            self.aceitunas_x=pilas.tareas.siempre(5, self.agregar_aceituna,self.aceitunas)
            self.aceitunas_y=pilas.tareas.siempre(10,self.agregar_aceituna_orbitales,self.aceitunas)
        
            


            
        else:
            self.texto=pilas.actores.Texto ("Exit to pause")
            self.texto.x=230
            self.texto.y=215
            self.boton_pausa.pintar_presionado()
            self.pausado=True
            self.aceitunas_x.terminar()
            self.aceitunas_y.terminar()
      
            
        
        
           
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
        pilas.tareas.agregar(1,rzck.imagen.definir_cuadro,0)
        
        
        rzck.imagen.definir_cuadro(2)
        
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
            pilas.camara.vibrar(intensidad=7, tiempo=3)                                                                                


pilas.escenas.vincular(PantallaBienvenida)
pilas.escenas.PantallaBienvenida()
pilas.escenas.vincular(PantallaJuego)
pilas.definir_pantalla_completa(True)


pilas.ejecutar()