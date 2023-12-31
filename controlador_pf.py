from vista_pf import Ventanaprincipal
import sys
from PyQt5.QtWidgets import QApplication
from modelo_pf import Servicio

class Coordinador(object):
    #como el coordindor enlaza el modelo con la vista debe
    #tener acceso a objetos de ambas clases
    def __init__(self, vista, sistema):
        self.__mi_vista = vista
        self.__mi_sistema = sistema
    def validar_usuario(self, u, p):
        return self.__mi_sistema.verificarUsuario(u,p)
    def img_conextion(self, imagen):
        self.__mi_sistema.pictureMaker(imagen)
    def dcm_info(self,imagen):
        return self.__mi_sistema.leerDicom(imagen)
    
    def nifti_conversion(self, imagen):
        self.__mi_sistema.nifti_conversion(imagen)

    def datos_slide1(self, valor1):
        return self.__mi_sistema.ampliarSenal(valor1)
    
    def datos_slide2(self, valor2):
        return self.__mi_sistema.anestesia_admin(valor2)
    
    def datos_slide3(self, valor3):
        return self.__mi_sistema.frecuenciaSenal(valor3)
        
    def datos_slide2(self, valor2):
        return self.__mi_sistema.anestesia_admin(valor2)
    
#esta clase no cambia ya que en esta simplemente se hacen las conexiones que siempre van
class Principal(object):
    def __init__(self):
        self.__app = QApplication(sys.argv)
        self.__mi_vista = Ventanaprincipal()
        self.__mi_sistema = Servicio()
        #hacemos enlaces entre las partes
        self.__mi_coordinador = Coordinador(self.__mi_vista, self.__mi_sistema)
        self.__mi_vista.asignarControlador(self.__mi_coordinador)
        
    def main(self):
        self.__mi_vista.show()
        sys.exit(self.__app.exec_())   

#se crean los objetos para la ejecucion    
p = Principal()
p.main()   
