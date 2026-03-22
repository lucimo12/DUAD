#Duplique el proyecto Sistema de Control de Estudiantes y modifíquelo para usar objetos para guardar la información de los estudiantes (creando una clase de Student).
#1.Hay que cambiar los estudiantes de diccionarios a objetos.
#2.Hay que convertir la data del csv (que viene por defecto en formato de diccionario) a objetos al importarla.
#3.Hay que convertir los objetos a diccionarios para poder exportarlos a csv.
#4.Hay que modificar el acceso a los keys para accesar a atributos.

class Student():
    def __init__(self, name, section, spanish, english, social, science):
        self.name = name 
        self.section = section
        self.spanish = spanish
        self.english = english
        self.social = social
        self.science = science
    
    def to_dict(self):
        return {
            "name": self.name,
            "section": self.section,
            "spanish": self.spanish,
            "english": self.english,
            "social": self.social,
            "science": self.science
        }
        

        