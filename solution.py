import os.path
import pandas as pd

def generar_csv(path):

    # Genera un csv con las frases y su sentimiento en la ruta especificada

    diccionario = {"phrase": [], "sentiment": []}

    # Recorrer los archivos de texto y guardar la información en el diccionario

    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".txt"):
                with open(os.path.join(root, file), "r") as f:
                    phrase = f.read()
                    diccionario["phrase"].append(phrase)

                    sentiment = os.path.basename(root)
                    diccionario["sentiment"].append(sentiment)
    
    # Crear el dataframe y el csv
    df = pd.DataFrame(diccionario)
    nombre = path.replace("data/", "")
    df.to_csv(f"{nombre}_dataset.csv", index=False)


generar_csv("data/train")
generar_csv("data/test")
    


        