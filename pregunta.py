"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""

import pandas as pd

def clean_data():
# Lectura de datos reestableciendo primer columna como indice
    df = pd.read_csv("solicitudes_credito.csv", sep=";",index_col=0)

# Eliminar filas duplicadas y valores faltantes NaN antes de limpiar
    df.dropna(axis='index',inplace=True)
    df.drop_duplicates(inplace=True)

# Convertir en mínuscula todas las columnas y en su respectivo tipo de dato
    # test 01
    df['sexo'] = df['sexo'].str.lower().astype(str)
    # test 02
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.lower().astype(str)
    # test 03
    df['idea_negocio'] = df['idea_negocio'].str.lower().str.replace(r'[_-]', ' ', regex=True).str.strip().astype(str)
    # test 04
    df['barrio'] = df['barrio'].str.lower().str.replace(r'[_-]', ' ', regex=True).astype(str)
    # test 05 Ya la columna está limpia
    # test 06 Ya la columna está limpia
    # test 07
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'],dayfirst=True)
    # test 08
    df['monto_del_credito'] = df['monto_del_credito'].str.replace(',','').str.replace('$','',regex=False).str.replace(' ','').astype(float) 
    # test 09
    df['línea_credito'] = df['línea_credito'].str.lower().str.replace(r'[_-]', ' ', regex=True).astype(str)

    # Eliminar filas duplicadas y valores faltantes NaN después de homogeneizar datos
    df.drop_duplicates(inplace=True)
    df.dropna(axis='index',inplace=True)

    return df

