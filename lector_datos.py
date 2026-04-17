import pandas as pd

# 1. Cargar el archivo
# pd.read_csv es la función mágica que convierte el archivo en una tabla de Python
try:
    df = pd.read_csv('datos_ventas.csv')
    
    print("--- Vista previa de los datos ---")
    print(df.head()) # Muestra las primeras filas

    # 2. Análisis rápido
    total_ventas = df['Venta'].sum()
    promedio_venta = df['Venta'].mean()

    print(f"\nTotal de ventas acumuladas: ${total_ventas}")
    print(f"Venta promedio por producto: ${promedio_venta:.2f}")

    # 3. Filtrado (Ciencia de datos básica)
    # Buscamos solo las ventas mayores a 2000
    ventas_altas = df[df['Venta'] > 2000]
    print("\nProductos de gama alta vendidos:")
    print(ventas_altas)

except FileNotFoundError:
    print("Error: No encontré el archivo 'datos_ventas.csv'. Asegúrate de que esté en la misma carpeta.")
