"""
Template Method (comportamental) tem a intenção de definir
um algoritmo em um método, postergando alguns passos
para as subclasses por herança. Template method permite
que subclasses redefinam certos passos de um algoritmo
sem mudar a estrutura do mesmo.

Também é possível definir hooks para que as subclasses
utilizem caso necessário.

The Hollywood principle: "Don't Call Us, We'll Call You."
(IoC - Inversão de controle)
"""
from abc import ABC, abstractmethod


class Pizza(ABC):
    """
        Class abstrata
    """
    def prepere(self):
        """
            Template method
        """
        self.hook_before_add_igredients()
        self.add_igrentients()
        self.hook_after_add_igredients()
        self.cook()
        self.cut()
        self.serve()
    
    def hook_before_add_igredients(self): pass
    def hook_after_add_igredients(self): pass
        
    def cut(self):
        print(f"{self.__class__.__name__}: Cortando a pizza")
    
    def serve(self):
        print(f"{self.__class__.__name__}: Servindo a pizza")

    @abstractmethod
    def add_igrentients(self): pass
    
    @abstractmethod
    def cook(self): pass
    
class AModa(Pizza):   
    def add_igrentients(self):
        print(f"AModa - Adicionando igredientes: presunto, queijo, goiabada")
        
    def cook(self):
        print(f'AModa - cozinhando por 45 min no forno a lenha') 
        
class Veg(Pizza):
    def hook_before_add_igredients(self):
        print("Veg - Lavando igredientes")

    def add_igrentients(self):
        print(f"Veg - Adicionando igredientes: igredientes veganos")
        
    def cook(self):
        print(f'Veg - cozinhando por 5 min no forno comum')  
        
if __name__ == "__main__":
    a_moda = AModa()
    a_moda.prepere()
    veg = Veg()
    veg.prepere()