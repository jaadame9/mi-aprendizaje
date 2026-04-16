import pandas as pd

# Creamos un diccionario con datos locales
datos_mty = {
    'Municipio': ['Apodaca', 'Monterrey', 'San Nicolás', 'Guadalupe'],
    'Tipo': ['Industrial', 'Capital', 'Residencial', 'Comercial'],
    'Proyectos': [15, 10, 8, 12]
}

# Convertimos el diccionario en un DataFrame (la estructura reina de Ciencia de Datos)
df = pd.DataFrame(datos_mty)

print("--- Análisis de Datos Local ---")
print(df)
print("\nResumen estadístico:")
print(df.describe())
