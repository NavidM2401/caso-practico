import pandas as pd

def corregir_datos_csv(input_file, output_file):
    # Cargar el archivo CSV
    df = pd.read_csv(input_file)
    
    # Eliminar filas completamente vacías
    df_cleaned = df.dropna(how="all")
    
    # Corregir la ID para que sea secuencial
    df_cleaned = df_cleaned.reset_index(drop=True)
    df_cleaned["producto_id"] = df_cleaned.index + 1
    
    # Redondear los precios a dos decimales
    df_cleaned["precio_base"] = df_cleaned["precio_base"].round(2)
    
    # Guardar el archivo corregido
    df_cleaned.to_csv(output_file, index=False)
    print(f"Archivo corregido guardado como: {output_file}")

# Ejemplo de uso
input_file = "productos.csv"  # Reemplazar con la ruta correcta
output_file = "productos_corregidos.csv"
corregir_datos_csv(input_file, output_file)