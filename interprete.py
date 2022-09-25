import nltk
import json
import unidecode
nltk.download('punkt')

# funcion para cargar el archivo de coleccion de palabras
def cargar_diccionario(ruta, categoria):
    with open(ruta) as contenido:
        diccionario = json.load(contenido)
        return diccionario.get(categoria)

# Se carga la frase

# frase = "Tuve la sensacion al salir de esta cinta de haber visto algo grandioso, algo que senti cuando vi Star Wars en 1977"
# frase = "La película en sí es muy mala, la historia está ya muy vista pero en otras películas está mas entretenida, mas emotiva o con más sentido. En este caso no tiene nada de nada. Los toques de humor son bastante lights e infantiles"
frase = "Que un plataformas se presente como el nuevo trabajo de Yuji Naka, uno de los creadores de Sonic, y el artista de la mascota de Sega Naoto Ohshima, a veces juega en contra del propio proyecto: las expectativas son tan altas que la decepción está casi garantizada. Y no lo decimos únicamente por Balan Wonderworld, hay un caso similar con Yooka-Laylee de PlayTonic Games, que se había marcado un objetivo demasiado ambicioso: ser el sucesor espiritual de Banjo-Kazooie –el estudio se redimiría poco después con el sobresaliente Yooka-Laylee and the Impossible Lair-. Así pues, todo lo que no fuese un juego con la calidad de Sonic 3 o un Sonic Adventure probablemente sería recibido con más palos que aplausos."

# Covertimos la frase a minusculas sin acentos para que sean congruentes con el diccionario
frase = frase.lower()
frase = unidecode.unidecode(frase)

# Separamos la frase por tokens. Se guarda en una lista. 
tokens = nltk.word_tokenize(frase)
print(tokens)

# Ruta al archivo de la colección de palabras
ruta = 'coleccion_palabras.json'

# Cargamos los diccionarios en listas
adj_positivos = cargar_diccionario(ruta, 'adjetivos_positivos')
adj_negativos = cargar_diccionario(ruta, 'adjetivos_negativos')

vrb_positivos = cargar_diccionario(ruta, 'verbos_positivos')
vrb_negativos = cargar_diccionario(ruta, 'verbos_negativos')

adv_positivos = cargar_diccionario(ruta, 'adverbios_positivos')
adv_negativos = cargar_diccionario(ruta, 'adverbios_negativos')

sus_positivos = cargar_diccionario(ruta, 'sustantivos_positivos')
sus_negativos = cargar_diccionario(ruta, 'sustantivos_negativos')

# Inicalizamos contadores
cont_positivo = 0       # Incidencias positivas
cont_negativo = 0       # Incidencias negativas
cont = 0                # En qué número de palabra va 

# Se comienza for que pasa por todas las palabras de la frase, la cual está almacenada en la lista tokens 
for token in tokens:

    # Comparamos la palabra n con todas las palabras en la lista de adjetivos positivos
    for palabra in adj_positivos:
        # Si hay conincidencia, revisaremos la palabra que le precede.
        if palabra == token:
            # Si la palabra que le precede está en la lista de adverbios positivos, se añade un punto a la positividad. 
            for pre in adv_positivos:
                if pre == tokens[cont - 1]:
                    cont_positivo = cont_positivo + 1
                    print("La palabra positiva -", token, "- tiene el prefijo positivo", pre)
            # Si la palabra que le precede está en la lista de adverbios negativos, se le quita un punto a la positividad.
            for pre in adv_negativos:
                if pre == tokens[cont - 1]:
                    cont_positivo = cont_positivo - 2
                    print("La palabra positiva -", token, "- tiene el prefijo negativo", pre)
            cont_positivo = cont_positivo + 1

    # Se repite el mismo proceso pero sumando puntos negativos en vez de positivos.
    for palabra in adj_negativos:
        if palabra == token:
            for pre in adv_positivos:
                if pre == tokens[cont-1]:
                    cont_negativo = cont_negativo + 1
                    print("La palabra negativa -", token, "- tiene el prefijo positivo", pre)
            for pre in adv_negativos:
                if pre == tokens[cont-1]:
                    cont_negativo = cont_negativo - 2
                    print("La palabra negativa -", token, "- tiene el prefijo negativo", pre)
            cont_negativo = cont_negativo + 1

    for palabra in vrb_positivos:
        if palabra == token:
            for pre in adv_positivos:
                if pre == tokens[cont-1]:
                    cont_negativo = cont_negativo + 1
                    print("La palabra positiva -", token, "- tiene el prefijo positivo", pre)
            for pre in adv_negativos:
                if pre == tokens[cont-1]:
                    cont_negativo = cont_negativo - 2
                    print("La palabra positiva -", token, "- tiene el prefijo negativo", pre)
            cont_negativo = cont_negativo + 1

    for palabra in vrb_negativos:
        if palabra == token:
            for pre in adv_positivos:
                if pre == tokens[cont-1]:
                    cont_negativo = cont_negativo + 1
                    print("La palabra negativa -", token, "- tiene el prefijo positivo", pre)
            for pre in adv_negativos:
                if pre == tokens[cont-1]:
                    cont_negativo = cont_negativo - 2
                    print("La palabra negativa -", token, "- tiene el prefijo negativo", pre)
            cont_negativo = cont_negativo + 1

    for palabra in sus_positivos:
        if palabra == token:
            for pre in adv_positivos:
                if pre == tokens[cont-1]:
                    cont_negativo = cont_negativo + 1
                    print("La palabra positiva -", token, "- tiene el prefijo positivo", pre)
            for pre in adv_negativos:
                if pre == tokens[cont-1]:
                    cont_negativo = cont_negativo - 2
                    print("La palabra positiva -", token, "- tiene el prefijo negativo", pre)
            cont_negativo = cont_negativo + 1

    for palabra in sus_negativos:
        if palabra == token:
            for pre in adv_positivos:
                if pre == tokens[cont-1]:
                    cont_negativo = cont_negativo + 1
                    print("La palabra negativa -", token, "- tiene el prefijo positivo", pre)
            for pre in adv_negativos:
                if pre == tokens[cont-1]:
                    cont_negativo = cont_negativo - 2
                    print("La palabra negativa -", token, "- tiene el prefijo negativo", pre)
            cont_negativo = cont_negativo + 1

    cont = cont+1

print ("Puntos positivos: ", cont_positivo)
print ("Puntos negativos: ", cont_negativo)

if (cont_negativo > cont_positivo):
    print ("Se concluye que la reseña es negativa.")
if (cont_positivo > cont_negativo):
    print ("Se concluye que la reseña es positiva.")
if (cont_positivo == cont_negativo):
    print ("Se concluye que la reseña es tan positiva como negativa.")
    
