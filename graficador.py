import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar los datos
try:
    df = pd.read_csv('datos_ventas.csv')

    # 2. Configurar la gráfica
    plt.figure(figsize=(10, 6)) # Tamaño de la imagen
    
    # Creamos una gráfica de barras: Eje X (Producto), Eje Y (Venta)
    plt.bar(df['Producto'], df['Venta'], color='skyblue', edgecolor='navy')

    # 3. Personalización (Esto lo hace ver profesional)
    plt.title('Reporte de Ventas por Producto', fontsize=16)
    plt.xlabel('Productos', fontsize=12)
    plt.ylabel('Monto de Venta ($)', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # 4. Guardar la imagen
    # En WSL no siempre se abre una ventana, así que guardamos el archivo directamente
    plt.savefig('grafica_ventas.png')
    print("¡Gráfica generada con éxito! Busca el archivo 'grafica_ventas.png' en tu carpeta.")

except Exception as e:
    print(f"Ocurrió un error: {e}")
