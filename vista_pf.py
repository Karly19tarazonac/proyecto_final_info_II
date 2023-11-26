import sys
import numpy as np
from PyQt5 import QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtWidgets
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication,QMainWindow, QDialog, QMessageBox, QFileDialog, QTableWidgetItem;
from log_in import Ui_inicio_de_sesion
from PyQt5.uic import loadUi;
import os
from PyQt5.QtGui import QPixmap
import pandas as pd
import nilearn
from nilearn import plotting
import shutil

class Ventanaprincipal(QMainWindow):
    #constructor
    def __init__(self, ppal=None):
        super(Ventanaprincipal,self).__init__(ppal)
        loadUi("login.ui",self)
        self.setup()
        
    #metodo para configurar las senales-slots y otros de la interfaz
    
    def setup(self):
        #se programa la senal para el boton
        self.login.clicked.connect(self.accion_ingresar)
    
    def asignarControlador(self,c):
        self.__controlador = c

    def accion_ingresar(self):
        usuario = self.campo_usuario.text()
        password = self.campo_password.text()
        #esta informacion la debemos pasar al controlador
        resultado = self.__controlador.validar_usuario(usuario,password)
        #se crea la ventana de resultado
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Resultado")
        #se selecciona el resultado de acuerdo al resultado de la operacion
        if resultado == "medico":
            self.abrirVentanaopciones()
        if resultado == "personal":
            self.abrirVentanaopciones2()
        if resultado == False:
            msg.setText("Usuario no Valido")
        #se muestra la ventana
            msg.show()

    def recibir_imagen(self,imagen):
        self.__controlador.img_conextion(imagen)

    def recibir_imagen2(self,imagen):
        return self.__controlador.dcm_info(imagen)
    
    def recibir_imagen3d(self,imagen):
        self.__controlador.nifti_conversion(imagen)
        
    def slider_uno(self, event):
        return self.__controlador.datos_slide1(event)
        
    def slider_dos(self, event):
        self.__controlador.datos_slide2(event)
    
    def slider_tres(self, event):
        return self.__controlador.datos_slide3(event)
        
    def abrirVentanaopciones(self):
        ventana_opciones=AbrirVentana_opciones(self)
        self.hide()
        ventana_opciones.show()

    def abrirVentanaopciones2(self):
        ventana_opciones=Ventana_opciones2(self)
        self.hide()
        ventana_opciones.show()
    
class AbrirVentana_opciones(QDialog):
    def __init__(self, ppal=None):
        super().__init__(ppal)
        loadUi('opciones_ventana.ui',self)
        self.__ventanaPadre = ppal
        self.setup()
    
    def setup(self):
        self.leer_archivo_dcm.clicked.connect(self.abrirVentanaBuscarCarpeta)
        self.mirar_inventarios.clicked.connect(self.abrirVentanaInventario)
        self.Diagnosticos.clicked.connect(self.abrirVentanaDiagnosticos)
        self.pushButton.clicked.connect(self.abiriVentanaAnestesia)
        self.img3d.clicked.connect(self.abrirVentanaOpciones3d)
        self.log_out.clicked.connect(self.logout)

    def abiriVentanaAnestesia(self):
        ventana_anestesia=VentanaAnestesia(self)
        self.hide()
        ventana_anestesia.show() 

    def abrirVentanaInventario(self):
        ventana_inventario=VentanaInventario(self)
        self.hide()
        ventana_inventario.show() 

    def abrirVentanaBuscarCarpeta(self):
        ventana_browse=VentanaBuscarCarpeta(self)
        self.hide()
        ventana_browse.show()

    def recibir_imagen(self,imagen):
        self.__ventanaPadre.recibir_imagen(imagen)

    def recibir_imagen2(self,imagen):
        return self.__ventanaPadre.recibir_imagen2(imagen)
    
    def recibir_imagen3d(self,imagen):
        self.__ventanaPadre.recibir_imagen3d(imagen)

    def slider_uno(self, event):
        return self.__ventanaPadre.slider_uno(event)
        
    def slider_dos(self, event):
        self.__ventanaPadre.slider_dos(event)
     
    def slider_tres(self, event):
        return self.__ventanaPadre.slider_tres(event)
       
    def abrirVentanaDiagnosticos(self):
        ventana_diagnostico=VentanaDiagnosticos(self)
        self.hide()
        ventana_diagnostico.show()
         
    def cerrar(self):
        self.__ventanaPadre.show()
        self.hide()

    def abrirVentanaOpciones3d(self):
        ventana_opciones=VentanaOpciones3d(self)
        self.hide()
        ventana_opciones.show()

    def logout(self):
        self.__ventanaPadre.show()
        self.hide()

class VentanaOpciones3d(QDialog):
    def __init__(self, ppal=None):
        super().__init__(ppal)
        loadUi('opciones3d.ui',self)
        self.__ventanaPadre = ppal
        self.setup()
    
    def setup(self):
        self.dcm.clicked.connect(self.abrirVentanaBuscarCarpeta)
        self.nii.clicked.connect(self.abrirVentanaBuscarArchivo)
        self.buttonBox.rejected.connect(self.cerrar)
        self.log_out.clicked.connect(self.logout)

    def abrirVentanaBuscarCarpeta(self):
        ventana_browse=VentanaBuscarCarpeta2(self)
        self.hide()
        ventana_browse.show()

    def abrirVentanaBuscarArchivo(self):
        ventana_browse=VentanaBuscarArchivo(self)
        self.hide()
        ventana_browse.show()

    def recibir_imagen3d(self,imagen):
        self.__ventanaPadre.recibir_imagen3d(imagen)

    def cerrar(self):
        self.__ventanaPadre.show()
        self.hide()

    def logout(self):
        self.__ventanaPadre.logout()
        self.hide()

class VentanaBuscarCarpeta2(QDialog):
    def __init__(self, ppal=None):
        super().__init__(ppal)
        loadUi('dialog_filesearch.ui',self)
        self.__ventanaPadre = ppal
        self.file=""
        self.setup()

    def setup(self):
        self.browse.clicked.connect(self.browsefiles)
        self.buttonBox.accepted.connect(self.abrirVentanaVisualizacion3d)
        self.buttonBox.rejected.connect(self.cerrar)
        self.log_out.clicked.connect(self.logout)

    def browsefiles(self):
        carpeta=QFileDialog.getExistingDirectory(self,"Open File")
        self.filepath.setText(carpeta)
        self.__ventanaPadre.recibir_imagen3d(carpeta)
        x = os.listdir("Nifti")
        file= x[0]
        self.file = "Nifti/"+file

    def cerrar(self):
        self.__ventanaPadre.show()

    def abrirVentanaVisualizacion3d(self):
        ventana_visualizacion=VentanaVisualizacion3d(self)
        self.hide()
        ventana_visualizacion.show()

    def recibir_imagen3d(self,imagen):
        self.__ventanaPadre.recibir_imagen3d(imagen)
    
    def logout(self):
        self.__ventanaPadre.logout()
        self.hide()

class VentanaBuscarArchivo(QDialog):
    def __init__(self, ppal=None):
        super().__init__(ppal)
        loadUi('filesearch.ui',self)
        self.__ventanaPadre = ppal
        self.file=""
        self.setup()

    def setup(self):
        self.browse.clicked.connect(self.browsefiles)
        self.buttonBox.accepted.connect(self.abrirVentanaVisualizacion3d)
        self.buttonBox.rejected.connect(self.cerrar)
        self.log_out.clicked.connect(self.logout)

    def browsefiles(self):
        archivo=QFileDialog.getOpenFileName(self,"Open File")[0]
        self.filepath.setText(archivo)
        self.file=archivo

    def cerrar(self):
        self.__ventanaPadre.show()

    def abrirVentanaVisualizacion3d(self):
        ventana_visualizacion=VentanaVisualizacion3d(self)
        self.hide()
        ventana_visualizacion.show()
    
    def logout(self):
        self.__ventanaPadre.logout()
        self.hide()

class VentanaVisualizacion3d(QDialog):
    def __init__(self, ppal=None):
        super().__init__(ppal)
        loadUi('visualizacion3d.ui',self)
        self.__ventanaPadre = ppal
        self.eje="ortho"
        self.setup()

    def setup(self):
        self.cargar()
        self.buttonBox.rejected.connect(self.cerrar)
        self.log_out.clicked.connect(self.logout)
        # self.cb.activated.connect(self.cambiarEje)

    def cargar(self):
        file=self.__ventanaPadre.file
        nilearn.plotting.plot_anat(file,display_mode=self.eje,output_file="temp_image")
        pixmap = QPixmap("temp_image.png")
        self.img.setPixmap(pixmap)
        os.remove('temp_image.png')
        shutil.rmtree("Nifti",ignore_errors=True)

    # def cambiarEje(self):
    #     if self.cb.currentText() == "Ortho":
    #         self.eje="ortho"
    #     elif self.cb.currentText() == "Axial":
    #         self.eje="z"
    #     elif self.cb.currentText() == "Sagital":
    #         self.eje="x"
    #     elif self.cb.currentText() == "Coronal":
    #         self.eje="y"
    #     self.cargar()

    def cerrar(self):
        self.__ventanaPadre.show()
        self.hide()

    def logout(self):
        self.__ventanaPadre.logout()
        self.hide()

class Ventana_opciones2(QDialog):
    def __init__(self, ppal=None):
        super().__init__(ppal)
        loadUi('opciones_ventana2.ui',self)
        self.__ventanaPadre = ppal
        self.setup()
    
    def setup(self):
        # self.leer_archivo_dcm.clicked.connect(self.abrirVentanaBuscarCarpeta)
        self.mirar_inventarios.clicked.connect(self.abrirVentanaInventario)
        # self.Diagnosticos.clicked.connect(self.abrirVentanaDiagnosticos)
        # self.pushButton.clicked.connect(self.abiriVentanaAnestesia)
        self.salir.clicked.connect(self.cerrar)
        self.log_out.clicked.connect(self.logout)

    def abrirVentanaInventario(self):
        ventana_inventario=VentanaInventario(self)
        self.hide()
        ventana_inventario.show() 

    def cerrar(self):
        self.__ventanaPadre.show()
        self.hide()

    def logout(self):
        self.__ventanaPadre.logout()
        self.hide()

class VentanaDiagnosticos(QDialog):
    def __init__(self, ppal=None):
        super().__init__(ppal)
        loadUi('pantalla.ui',self)
        self.__ventanaPadre = ppal
        self.setWindowTitle("apertura de diagnosticos")
        self.setup()

    def setup(self):
        self.open_file.clicked.connect(self.abrir_dialogo)
        self.salir_boton.clicked.connect(self.cerrar)
        self.log_out.clicked.connect(self.logout)
    
    def cerrar(self):
        self.__ventanaPadre.show()
        self.hide()

    def abrir_dialogo(self):
        filename= QFileDialog.getOpenFileName(self,"Open File")[0]
        self.file_path.setText(filename)
        text = open(filename,"r")
        self.display.setText(text.read())

    def logout(self):
        self.__ventanaPadre.logout()
        self.hide()

class VentanaAnestesia(QDialog):
    def __init__(self, ppal=None):
        super().__init__(ppal)
        loadUi('anestesia.ui',self)
        self.__ventanaPadre = ppal
        self.setup()
    
    def setup(self):
        #se programa la senal para el boton
        self.grafica=Canvas_grafica()
        self.verticalLayout.addWidget(self.grafica)
        self.oxigeno.valueChanged.connect(self.slider_uno)
        # self.anest.valueChanged.connect(self.slider_dos)
        self.presion.valueChanged.connect(self.slider_tres)
        self.boton_salir.clicked.connect(lambda:self.close())
        self.log_out.clicked.connect(self.logout)


    def slider_uno(self, event):
        valor1 = self.__ventanaPadre.slider_uno(event)
        self.grafica.datos1(valor1)

    def slider_dos(self, event):
        valor2 = self.__ventanaPadre.slider_dos(event)
        self.grafica.datos2(valor2) 
    
    def slider_tres(self, event):
        valor3 = self.__ventanaPadre.slider_tres(event)
        self.grafica.datos3(valor3)

    def logout(self):
        self.__ventanaPadre.logout()
        self.hide()

class Canvas_grafica(FigureCanvas):
    def __init__(self, parent=None):     
        self.fig , self.ax = plt.subplots(facecolor='gray')
        super().__init__(self.fig) 
        self.ax.grid()
        self.ax.margins(x=0)
        self.nivel1 = 10
        self.nivel2 = 1
        self.nivel3 = 1
        self.grafica_datos()

    def datos1(self, valor1):
        self.nivel1 = valor1

    def datos2(self, valor2):
        self.nivel2 = valor2

    def datos3(self, valor3):
        self.nivel3 = valor3
        
    def grafica_datos(self):
        plt.title("Administracion de anestesia")
        x = np.arange(-np.pi, 10*np.pi, 0.01) 
        line, = self.ax.plot(x, self.nivel1*np.sin(self.nivel3*x), color='r',linewidth=2)
        line2, = self.ax.plot(x, self.nivel1*np.sin(self.nivel2*x), color='blue',linewidth=2)
        self.draw()     
        line.set_ydata(np.sin(x)+24)
        line2.set_ydata(np.sin(x)+24)
        QtCore.QTimer.singleShot(10, self.grafica_datos)
    
class VentanaBuscarCarpeta(QDialog):
    def __init__(self, ppal=None):
        super().__init__(ppal)
        loadUi('dialog_filesearch.ui',self)
        self.__ventanaPadre = ppal
        self.folder=""
        self.setup()

    def setup(self):
        self.browse.clicked.connect(self.browsefiles)
        self.buttonBox.accepted.connect(self.abrirVentanaVisualizacion)
        self.buttonBox.rejected.connect(self.cerrar)
        self.log_out.clicked.connect(self.logout)

    def browsefiles(self):
        carpeta=QFileDialog.getExistingDirectory(self,"Open File")
        self.filepath.setText(carpeta)
        self.folder=carpeta

    def cerrar(self):
        self.__ventanaPadre.show()

    def abrirVentanaVisualizacion(self):
        ventana_visualizacion=VentanaVisualizacion(self)
        self.hide()
        ventana_visualizacion.show()

    def recibir_imagen(self,imagen):
        self.__ventanaPadre.recibir_imagen(imagen)

    def recibir_imagen2(self,imagen):
        return self.__ventanaPadre.recibir_imagen2(imagen)
    
    def logout(self):
        self.__ventanaPadre.logout()
        self.hide()

class VentanaVisualizacion(QDialog):
    def __init__(self, ppal=None):
        super().__init__(ppal)
        loadUi('visualization.ui',self)
        self.__ventanaPadre = ppal
        self.file_number=0
        self.setup()

    def setup(self):
        self.cargar()
        self.buttonBox.rejected.connect(self.cerrar)
        self.hslider.valueChanged.connect(self.slider)
        self.log_out.clicked.connect(self.logout)

    def slider(self,value):
        self.file_number=value
        self.cargar()

    def cargar(self):
        folder=self.__ventanaPadre.folder
        try:
            archivos = os.listdir(folder)
        except:
            self.label.setText("ERROR: Escoge Otra Carpeta")
            return
        slider_max= len(archivos)-1
        self.hslider.setMaximum(slider_max)
        filename = archivos[self.file_number]
        imagen = f"{folder}/{filename}"
        self.__ventanaPadre.recibir_imagen(imagen)
        pixmap = QPixmap("temp_image.png")
        self.img.setPixmap(pixmap)
        os.remove('temp_image.png')
        dcm_info = self.__ventanaPadre.recibir_imagen2(imagen)
        self.label.setText(f"{filename}\n\n{dcm_info}")

    def cerrar(self):
        self.__ventanaPadre.show()

    def logout(self):
        self.__ventanaPadre.logout()
        self.hide()

class VentanaInventario(QDialog):
    def __init__(self, ppal=None):
        super().__init__(ppal)
        loadUi('inventario.ui',self)
        self.__ventanaPadre = ppal
        self.setup()

    def setup(self):
        self.boton_abrir.clicked.connect(self.abrir_archivo)
        self.pushButton.clicked.connect(self.crear_tabla)
        self.boton_salir.clicked.connect(self.salir_archivo)
        self.log_out.clicked.connect(self.logout)

    def abrir_archivo(self):
        #nos da una tupla que es la direccion y un nombre 
        file= QFileDialog.getOpenFileName(self, "abrir archivo Excel","","Excel Files (*.xlsx) ;; All Files (*)" )
        self.direccion = file [0]
    
    def crear_tabla(self):
        try:
            df= pd.read_excel(self.direccion) #leemos el archivo
            columnas = list(df.columns) # crea una lista del encabezado
            df_fila= df.to_numpy().tolist() # crea una lista de listas de todas las filas
            x=len(columnas)
            y=len(df_fila)

#excepciones para formato incorrecto o no hallado

        except ValueError:
            QMessageBox.about(self,"informacion","formato incorrecto")
            return None
        
        except FileNotFoundError:
             QMessageBox.about(self,"informacion","el archivo esta \n malogrado")
             return None
        
        self.tableWidget.setRowCount(y)
        self.tableWidget.setColumnCount(x)

#ciclos para asignar valores en columnas
        for j in range(x):
            encabezado= QtWidgets.QTableWidgetItem(columnas[j])
            self.tableWidget.setHorizontalHeaderItem(j,encabezado )
#ciclo para asignar valores a filas
            for i in range(y):
                dato=str(df_fila[i][j])
#cambia valores nan a vacios
                if dato=="nan":
                    dato=""
#asigna los datos a la columna y fila correspondiente
                self.tableWidget.setItem(i,j,QTableWidgetItem(dato))
        
    def salir_archivo(self):
        self.__ventanaPadre.show()
        self.hide()

    def logout(self):
        self.__ventanaPadre.logout()
        self.hide()
