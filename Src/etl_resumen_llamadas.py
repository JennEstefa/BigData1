# Pseudo codigo
#1. Leer archivo.csv
# 2. Extraer el resumen
# 3. Guardar el resumen en formato.csv

from turtle import clear
import numpy as np
import logging
import pandas as pd
import os

from pathlib import Path


def main():

    filename = filename = "llamadas123_julio_2022.csv"
    # leer archivo
    data = get_data(filename = filename)
    # Extraer resumen
    df_resumen = get_summary(data)
    # Guarde el resumen
    save_data(df_resumen, filename = "llamadas123_julio_2022.csv")

def get_data(filename):
    data_dir = "raw1"
    root_dir = Path(".").resolve()
    file_path = os.path.join(root_dir,"data",data_dir, filename)
      
    data = pd.read_csv(file_path, encoding='latin-1',sep=';')
    return data

def get_summary(data):

    # crear un diccionario vacio
    dict_resumen = dict()

    for col in data.columns:
        valores_unicos = data[col].unique()
        n_valores= len(valores_unicos)
        dict_resumen[col] = n_valores

    
    df_resumen = pd.DataFrame.from_dict(dict_resumen, orient="index")
    df_resumen.rename({0: "Count"}, axis=1, inplace=True)
    
    return df_resumen
        

def save_data(df, filename):
    out_name= "resumen_" + filename
    root_dir = Path(".").resolve()
    out_path = os.path.join(root_dir, "data", "processed", out_name)
    
    # print(out_path)
    df.to_csv(out_path)

if __name__ == '__main__':
    main()