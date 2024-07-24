import os.path
import pandas as pd

def generar_csv(path):
    '''Genera un csv con las oraciones y su 
    sentimiento en el path especificado'''

    data = {"oración": [], "sentimiento": []}

    # Recorrer cada archivo de texto y guarda la información en el diccionario
    for root, _, files in os.walk(path):
        for archivo in files:
            if archivo.endswith(".txt"):
                with open(os.path.join(root, archivo), "r") as f:
                    oración = f.read()
                    data["oración"].append(oración)

                    sentimiento = os.path.basename(root)
                    data["sentimiento"].append(sentimiento)
    
    # Se crea el dataframe y el csv
    df = pd.DataFrame(data)
    nombre = path.replace("data/", "")
    df.to_csv(f"{nombre}_dataset.csv", index=False)

if __name__ == "__main__":
    generar_csv("data/test")
    generar_csv("data/train")
    #


        