import pandas as pd

def corregir_datos(archivo_entrada, archivo_salida):
    # Cargar el archivo CSV
    df = pd.read_csv(archivo_entrada)
    
    # Eliminar filas donde cliente_id esté vacío
    df = df.dropna(subset=["cliente_id"])
    
    # Asegurar que la columna cliente_id sea numérica y corregir IDs secuenciales
    df["cliente_id"] = pd.to_numeric(df["cliente_id"], errors="coerce")
    df["cliente_id"] = range(1, len(df) + 1)
    
    # Asegurar que la columna edad es numérica y convertir a entero sin decimales
    df["edad"] = pd.to_numeric(df["edad"], errors="coerce").fillna(0).astype(int)
    
    # Ajustar edades para que no tengan más de dos dígitos
    df["edad"] = df["edad"].apply(lambda x: int(str(x)[:2]))
    
    # Guardar el archivo corregido
    df.to_csv(archivo_salida, index=False)
    print(f"Archivo corregido guardado como: {archivo_salida}")

# Uso del script
def main():
    archivo_entrada = "clientes.csv"  # Cambia esto por la ruta de tu archivo
    archivo_salida = "clientes_corregidos.csv"
    corregir_datos(archivo_entrada, archivo_salida)

if __name__ == "__main__":
    main()