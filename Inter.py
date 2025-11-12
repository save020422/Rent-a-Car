import Abtsration as ab
import flet 
lista_de_usuarios =[]
lsita_de_autos = []
lsita_de_contratos = [ ]


def add_users(name_,passaport_,country_):
            
            lista_de_usuarios.append(ab.Tourist(name=name_ , 
                                         passport_number= passaport_ , 
                                         country= country_))
            print("ok")
  