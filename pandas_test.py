import pandas as pd

# 1. Definimos los datos en un diccionario
datos = {
    'Producto': ['Laptop', 'Mouse', 'Teclado', 'Monitor'],
    'Precio': [1200, 25, 50, 300],
    'Stock': [5, 50, 30, 12]
}

# 2. Convertimos el diccionario en un DataFrame
df = pd.DataFrame(datos)

# 3. Mostramos el resultado
print(df)
caros = df[df['Precio'] > 100]
print(caros)
