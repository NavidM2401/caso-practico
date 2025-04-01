import pandas as pd

def corregir_datos(archivo_entrada, archivo_salida):
    # Cargar el archivo CSV
    df = pd.read_csv(archivo_entrada)
    
    # Eliminar filas completamente vacías
    df = df.dropna(how='all')
    
    # Ordenar por 'venta_id' y hacer que sean secuenciales
    df = df.sort_values(by='venta_id')
    df['venta_id'] = range(1, len(df) + 1)
    
    # Eliminar decimales de IDs y cantidad
    columnas_a_convertir = ['producto_id', 'cliente_id', 'sucursal_id', 'cantidad']
    for columna in columnas_a_convertir:
        df[columna] = df[columna].fillna(0).astype(int)
    
    # Redondear precios a dos decimales
    df['precio_unitario'] = df['precio_unitario'].round(2)
    df['total'] = df['total'].round(2)
    
    # Guardar el archivo corregido
    df.to_csv(archivo_salida, index=False)
    print(f"Archivo corregido guardado en: {archivo_salida}")

# Uso del script
if __name__ == "__main__":
    archivo_entrada = "ventas.csv"  # Cambiar por la ruta del archivo original
    archivo_salida = "ventas_corregido.csv"
    corregir_datos(archivo_entrada, archivo_salida)