# Importamos random, sera necesario a la hora de usar palabras aleatorias (Luis)

import random

# Empezamos a definir variables, palabras contendra como dice su nombre palabras a adivinar, palabra determina la palabra aleatoria dentro del rango de la variable palabras
# vidas es la cantidad de vidas, y letras adivinadas/incorrectas va contando las letras adivinadas/incorrectas (Luis)

# La parte de eleccion fue hecha por (Juan) XD
# La parte de eleccion2 tambien fue hecha por (Juan)... XD

eleccion = input("Desea escribir usted la palabra? (si/no): ").lower()
vidas = 6

if eleccion == "si":
        palabra = input("Escriba la palabra: ")
        letras_adivinadas = set()
        letras_incorrectas = set()

else:
        eleccion2 = int(input("Desea una palabra facil(1) o una palabra dificil(2)?: "))

        if eleccion2 == 1:
            palabras_faciles = ["python", "codigo", "programa", "teclado", "curso","casa", "computadora", "vaso", "pajaro", "suerte", "lentes", "perro", "gato", "aritos"]
            palabra = random.choice(palabras_faciles)
            letras_adivinadas = set()
            letras_incorrectas = set()
        elif eleccion2 == 2:
            palabras_dificiles = ["spinosaurio", "procesador", "esdrujula", "ovoviviparo", "litofotograficamente", "otorrinolaringologo", "idiosincrasia", "desoxirribonucleico"]
            palabra = random.choice(palabras_dificiles)
            letras_adivinadas = set()
            letras_incorrectas = set()

# Aqui abajo vamos a hacer una funcion para el dibujo del ahorcado :D (Juan)

def dibujo (vidas):
    if vidas == 6:
        personaje = print("""
     __
    |/      |
    |      ()
    |      /|\
    |      / \
    |
    |___
    
                       """)
    elif vidas == 5:
        personaje = print("""
     __
    |/      |
    |      ()
    |      /|\
    |      / 
    |
    |___
    
                       """)
    
    elif vidas == 4:
        personaje = print("""
     __
    |/      |
    |      ()
    |      /|\
    |       
    |
    |___
    
                       """)
    
    elif vidas == 3:
        personaje = print("""
     __
    |/      |
    |      ()
    |      /|
    |       
    |
    |___
    
                       """)
    
    elif vidas == 2:
        personaje = print("""
     __
    |/      |
    |      ()
    |       |
    |       
    |
    |___
    
                       """)
    
    elif vidas == 1:
        personaje = print("""
     __
    |/      |
    |      ()
    |      
    |       
    |
    |___
    
        Ultima oportunidad!!!
                       """)
    
    elif vidas == 0:
        personaje = print("""
     __
    |/      |
    |      
    |      
    |       
    |
    |___
    
        Parece que te han AHORCADO.                
                       """)
    return (dibujo)
# Aca se hace una funcion que va a recibir la palabra, la oculta con "_" pero si la letra es adivinada es reemplazada por bueno, su respectiva letra (Luis)

def mostrar_palabra(palabra, letras_adivinadas):
    return ' '.join([letra if letra in letras_adivinadas else '_' for letra in palabra])

# Son los print, no veo necesidad de explicarlos (Luis)

while True:
    dibujo(vidas)
    print("\nPalabra:", mostrar_palabra(palabra, letras_adivinadas))
    print("Vidas restantes:", vidas)
    print("Letras incorrectas:", ' '.join(sorted(letras_incorrectas)))

    # Aca son inputs y la parte donde el jugador ingresa la letra, insisto no veo necesidad de explicar excepto la parte ".lower()"
    # Para los que no sepan eso hace que cada valor ingresado se ponga en minuscula automaticamente, esto para evitar errores, tambien se define si termina el juego o no (Luis)

    entrada = input("Ingresa una letra (o 'salir' para terminar): ").lower()

    if entrada == "salir":
        print("¡Hasta la próxima!")
        break

    if not entrada.isalpha() or len(entrada) != 1:
        print("Por favor, ingresa una letra válida.")
        continue

    if entrada in letras_adivinadas or entrada in letras_incorrectas:
        print("Ya ingresaste esa letra.")
        continue

    if entrada in palabra:
        letras_adivinadas.add(entrada)
    else:
        letras_incorrectas.add(entrada)
        vidas -= 1

    if all(letra in letras_adivinadas for letra in palabra):
        dibujo(vidas)
        print("\n¡Ganaste! La palabra era:", palabra)
        break

    if vidas == 0:
        dibujo(vidas)
        print("\nPerdiste. La palabra era:", palabra)
        break
