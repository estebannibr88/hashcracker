import hashlib

class HashGenerator:
    def __init__(self):
        pass
    
    def crear_hash(self, texto):
        # Se utiliza el algoritmo SHA256 para generar el hash
        hash_obj = hashlib.sha256()
        hash_obj.update(texto.encode())
        return hash_obj.hexdigest()

#ahora el hashcracker 

class HashCracker:
    
    
 def comparar (self,hash_file, dic_file):
    hash_calculado = HashGenerator()
    #tengo un error sobre que no me quiere leer la ruta y abrirla como archivo de lectura
    with open (dic_file, 'r') as file:
    
        diccionario = [line.strip() for line in file]#enlista las palabras del .txt eliminando espacios
    
    for password in diccionario:
        
        
        if hash_calculado.crear_hash(password) == hash_file:
            
            self.correcto = password
            
            return True
        else:
            return False
        
        
    
             
    
if __name__ == "__main__":
    generador = HashGenerator()
    cracker = HashCracker()
    
    while True:
        print("¿Qué desea hacer?")
        print("1. Crear hash")
        print("2. Crackear hash")
        opcion = input("Ingrese la opción (1/2): ")
        
        if opcion == "1":
            texto = input("Ingrese el texto a convertir en hash: ")
            hash_resultado = generador.crear_hash(texto)
            print("El hash resultante es:", hash_resultado)
        elif opcion == "2":
            
            hash_file = input("Ingrese el hash a crackear")
            dic_file = input("Ingrese la ruta del diccionario")
            resultado=cracker.comparar(hash_file, dic_file)
            if resultado:
                print("La contraseña es "+ cracker.correcto)
            else:
                print("La contraseña no se encuentra en el diccionario")
            
            
            
            
            
        else:
            print("Opción no válida. Por favor, ingrese 1 o 2.")

