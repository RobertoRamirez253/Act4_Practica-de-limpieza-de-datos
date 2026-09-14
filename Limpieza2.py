# ============================================================
# LIMPIEZA DE DATOS - DIRTY CAFE SALES
# ============================================================


# 1. Importar librerías necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import datetime as dt
#import missingno as msno
#import fuzzywuzzy
#import recordlinkage


# ============================================================
# 2. Cargar e integrar datos
# ============================================================

df = pd.read_csv('dirty_cafe_sales.csv')

# print(df.head())


# ============================================================
# 3. Eliminar columnas duplicadas e inservibles
# ============================================================

# En este caso no se eliminaron columnas duplicadas ni
# inservibles, ya que el dataset no contenía ninguna.

'''
print(df['Transaction ID'].describe())
print(df['Item'].describe())
print(df['Quantity'].describe())
print(df['Price Per Unit'].describe())
print(df['Total Spent'].describe())
print(df['Payment Method'].describe())
print(df['Location'].describe())
print(df['Transaction Date'].describe())
'''

print("\nValores nulos por columna:")
print(df.isnull().sum())


# ============================================================
# 4. Eliminar filas duplicadas
# ============================================================

df = df.drop_duplicates()

df = df.reset_index(drop=True)


# ============================================================
# 5. Eliminar filas inservibles
# ============================================================

# Se considera que una fila es válida si tiene al menos
# el 80% de sus datos completos.

porcentaje_validas = 0.8

num_validas = df.notnull().sum(axis=1)

porc_validas = num_validas / df.shape[1]

filas_validas = porc_validas >= porcentaje_validas

df = df[filas_validas]

df = df.reset_index(drop=True)


# ============================================================
# 6. Eliminar filas con dos o más valores UNKNOWN o ERROR
# ============================================================

# Se cuentan los valores UNKNOWN y ERROR presentes en cada fila.

valores_invalidos = ['UNKNOWN', 'ERROR']

cantidad_invalidos = df.isin(valores_invalidos).sum(axis=1)

# Conservar únicamente las filas que tengan menos de
# dos valores UNKNOWN o ERROR.

df = df[cantidad_invalidos < 2]

df = df.reset_index(drop=True)


# Mostrar cuántas filas quedaron después del filtrado

print("\nFilas después de eliminar registros con 2 o más")
print("valores UNKNOWN o ERROR:")

print(len(df))


# ============================================================
# 7. Estandarizar las categorías de cada columna
# ============================================================

'''
print(df['Transaction ID'].value_counts())
print(df['Item'].value_counts())
print(df['Quantity'].value_counts())
print(df['Price Per Unit'].value_counts())
print(df['Total Spent'].value_counts())
print(df['Payment Method'].value_counts())
print(df['Location'].value_counts())
print(df['Transaction Date'].value_counts())
'''

# Las categorías del dataset ya se encuentran
# estandarizadas.


# ============================================================
# 8. Verificar errores en datos numéricos
# ============================================================

df.info()

# Las columnas Quantity, Price Per Unit y Total Spent
# contienen datos almacenados como texto.
#
# Los valores que no puedan convertirse, como ERROR,
# serán convertidos en NaN.


# ------------------------------------------------------------
# Convertir columnas numéricas
# ------------------------------------------------------------

df['Quantity'] = pd.to_numeric(
    df['Quantity'],
    errors='coerce'
)

df['Price Per Unit'] = pd.to_numeric(
    df['Price Per Unit'],
    errors='coerce'
)

df['Total Spent'] = pd.to_numeric(
    df['Total Spent'],
    errors='coerce'
)


# ------------------------------------------------------------
# Convertir fecha
# ------------------------------------------------------------

df['Transaction Date'] = pd.to_datetime(
    df['Transaction Date'],
    format='%Y-%m-%d',
    errors='coerce'
)


# ============================================================
# 9. Realizar el tratamiento de datos vacíos
# ============================================================

# Para las columnas numéricas se utiliza la media.
#
# Para las columnas categóricas se eliminan las filas que
# tengan valores nulos.


# ------------------------------------------------------------
# Quantity
# ------------------------------------------------------------

df['Quantity'] = df['Quantity'].fillna(
    df['Quantity'].mean()
)

# Redondear Quantity y convertirlo a entero
df['Quantity'] = df['Quantity'].round().astype(int)


# ------------------------------------------------------------
# Price Per Unit
# ------------------------------------------------------------

df['Price Per Unit'] = df['Price Per Unit'].fillna(
    df['Price Per Unit'].mean()
)


# ------------------------------------------------------------
# Total Spent
# ------------------------------------------------------------

df['Total Spent'] = df['Total Spent'].fillna(
    df['Total Spent'].mean()
)


# ------------------------------------------------------------
# Eliminar filas con valores nulos en columnas categóricas
# ------------------------------------------------------------

df = df.dropna(
    subset=[
        'Transaction ID',
        'Item',
        'Payment Method',
        'Location'
    ]
)

df = df.reset_index(drop=True)


# ============================================================
# 10. Verificar que no existan valores nulos
# ============================================================

print("\nValores nulos después del tratamiento:")

print(df.isnull().sum())


# ============================================================
# 11. Remover duplicados
# ============================================================

df = df.drop_duplicates()

df = df.reset_index(drop=True)


# ============================================================
# 12. Retirar o corregir valores atípicos
# ============================================================

# Se utiliza el método IQR para identificar valores atípicos.
#
# IQR = Q3 - Q1
#
# Límite inferior = Q1 - 1.5 * IQR
#
# Límite superior = Q3 + 1.5 * IQR


def detectar_atipicos(df, columna):

    Q1 = df[columna].quantile(0.25)

    Q3 = df[columna].quantile(0.75)

    IQR = Q3 - Q1

    limite_inferior = Q1 - 1.5 * IQR

    limite_superior = Q3 + 1.5 * IQR

    atipicos = df[
        (df[columna] < limite_inferior) |
        (df[columna] > limite_superior)
    ]

    print(f"\nValores atípicos encontrados en {columna}:")

    print(len(atipicos))

    return atipicos


# Detectar valores atípicos

atipicos_quantity = detectar_atipicos(
    df,
    'Quantity'
)

atipicos_price = detectar_atipicos(
    df,
    'Price Per Unit'
)

atipicos_total = detectar_atipicos(
    df,
    'Total Spent'
)


# ============================================================
# VERIFICACIÓN FINAL
# ============================================================

print("\n==========================================")
print("VERIFICACIÓN FINAL")
print("==========================================")


# Valores nulos

print("\nValores nulos por columna:")

print(df.isnull().sum())


# Valores UNKNOWN y ERROR restantes

print("\nValores UNKNOWN y ERROR restantes:")

print(
    df.isin(['UNKNOWN', 'ERROR']).sum()
)


# Información del DataFrame

print("\nInformación final del DataFrame:")

df.info()


# Cantidad de filas y columnas

print("\nDimensiones finales del DataFrame:")

print(df.shape)


# Mostrar las primeras filas

print("\nPrimeras filas del DataFrame limpio:")

print(df.head())


# ============================================================
# 13. Exportar datos
# ============================================================

df.to_csv(
    'dirty_cafe_sales_limpio.csv',
    index=False
)

print("\n==========================================")
print("LIMPIEZA COMPLETADA")
print("==========================================")

print("\nArchivo generado:")

print("dirty_cafe_sales_limpio.csv")