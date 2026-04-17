import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar los mismos datos
try:
    df = pd.read_csv('datos_ventas.csv')

    # 2. Configurar la gráfica de pastel
    plt.figure(figsize=(8, 8)) # Un cuadrado para que el círculo no se vea ovalado
    
    # Creamos el pastel
    # 'labels' son los nombres, 'autopct' pone el % con un decimal
    plt.pie(df['Venta'], 
            labels=df['Producto'], 
            autopct='%1.1f%%', 
            startangle=140, 
            colors=['#ff9999','#66b3ff','#99ff99','#ffcc99', '#c2c2f0'])

    # 3. Estética
    plt.title('Distribución de Ingresos por Producto', fontsize=15)
    plt.axis('equal')  # Asegura que el pastel sea un círculo perfecto

    # 4. Guardar
    plt.savefig('reporte_pastel.png')
    print("¡Gráfica de pastel generada! Abre 'reporte_pastel.png' para verla.")

except Exception as e:
    print(f"Error: {e}")
