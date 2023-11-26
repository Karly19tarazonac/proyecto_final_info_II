import pydicom
import matplotlib.pyplot as plt
import dicom2nifti
import os

class Servicio(object):
    def __init__(self):
        self.nivel1=10
        self.nivel2=1
        self.nivel3=1
        self.__usuarios = {}
        #se crea un usuario inicial para arrancar el sistema
        self.__usuarios["medico"] = 'medico'
        self.__usuarios['personal'] = "personal"
    
    def verificarUsuario(self, u, c):
        try:
            #Si existe la clave se verifica que sea el usuario
            if self.__usuarios[c] == u:
                if u == "medico":
                    # u_doctor = True
                    return "medico"
                if u == "personal":
                    # u_enfermero = True
                    return "personal"
            else:
                return False
        except: #si la clave no existe se genera KeyError
            return False
        
    def leerDicom(self,imagen):
        ds = pydicom.dcmread(imagen)
        slice = str(ds["SliceLocation"])
        image_type = str(ds["ImageType"])
        study_description = str(ds["StudyDescription"])
        series_decription = str(ds["SeriesDescription"])
        modality = str(ds["Modality"])
        dcm_info = f"{image_type}\n{study_description}\n{series_decription}\n{modality}\n{slice}"
        return dcm_info
        
    def pictureMaker(self,imagen):
        dcm_data = pydicom.dcmread(imagen)
        im = dcm_data.pixel_array
        if (len(im.shape))==3:
            slice_index = im.shape[0] // 2
            selected_slice = im[slice_index, :, :]
            plt.imshow(selected_slice, cmap=plt.cm.bone)
        else:
            plt.imshow(im, cmap = plt.cm.bone)
        plt.axis('off')
        plt.savefig("temp_image.png")

    def nifti_conversion(self,imagen):
        os.mkdir("Nifti")
        dicom2nifti.convert_directory(imagen,"Nifti")

    def ampliarSenal(self,valor1):
        self.nivel1 = valor1*0.1
        return self.nivel1

    def frecuenciaSenal(self, valor3):
        self.nivel3 = valor3*0.05
        return self.nivel3
    
    def anestesia_admin(self, valor2):
        self.nivel2 =valor2*0.05
        return self.nivel2
