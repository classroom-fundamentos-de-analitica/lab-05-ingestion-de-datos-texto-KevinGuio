import os.path
import pandas as pd

def generar_csv(path):
    '''Genera un archivo csv con los datos de las frases y su 
    sentimiento en el path especificado'''

    data = {"phrase": [], "sentiment": []}

    # Recorrer los archivos de texto y guardar los datos
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".txt"):
                with open(os.path.join(root, file), "r") as f:
                    phrase = f.read()
                    data["phrase"].append(phrase)

                    sentiment = os.path.basename(root)
                    data["sentiment"].append(sentiment)
    
    # Crear el dataframe y guardarlo en un archivo csv
    df = pd.DataFrame(data)
    name = path.replace("data/", "")
    df.to_csv(f"{name}_dataset.csv", index=False)


generar_csv("data/train")
generar_csv("data/test")
    

