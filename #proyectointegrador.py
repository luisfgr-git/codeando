#proyectointegrador.py 
import random

palabras = ["python", "codigo", "programa", "teclado"]
palabra = random.choice(palabras)
vidas = 6
letras_adivinadas = set()
letras_incorrectas = set()

def mostrar_palabra(palabra, letras_adivinadas):
    return ' '.join([letra if letra in letras_adivinadas else '_' for letra in palabra])

while True:
    print("\nPalabra:", mostrar_palabra(palabra, letras_adivinadas))
    print("Vidas restantes:", vidas)
    print("Letras incorrectas:", ' '.join(sorted(letras_incorrectas)))

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
        print("\n¡Ganaste! La palabra era:", palabra)
        break

    if vidas == 0:
        print("\nPerdiste. La palabra era:", palabra)
        break

