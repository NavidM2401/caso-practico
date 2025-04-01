import pandas as pd
import numpy as np

def corregir_logistica(archivo_entrada, archivo_salida):
    # Cargar el archivo CSV
    df = pd.read_csv(archivo_entrada)
    
    # Eliminar filas donde cualquier campo esté completamente vacío
    df = df.dropna(how='all')
    
    # Convertir IDs a enteros (eliminar decimales)
    df["envio_id"] = pd.to_numeric(df["envio_id"], errors="coerce").fillna(-1).astype(int)
    df["venta_id"] = pd.to_numeric(df["venta_id"], errors="coerce").fillna(-1).astype(int)
    df["proveedor_id"] = pd.to_numeric(df["proveedor_id"], errors="coerce").fillna(-1).astype(int)
    
    # Reemplazar IDs faltantes (-1) con valores aleatorios dentro de un rango alto para evitar colisiones
    df.loc[df["envio_id"] == -1, "envio_id"] = np.random.randint(10000, 99999, size=len(df[df["envio_id"] == -1]))
    df.loc[df["venta_id"] == -1, "venta_id"] = np.random.randint(10000, 99999, size=len(df[df["venta_id"] == -1]))
    df.loc[df["proveedor_id"] == -1, "proveedor_id"] = np.random.randint(10000, 99999, size=len(df[df["proveedor_id"] == -1]))
    
    # Ordenar los envio_id en secuencia numérica
    df = df.sort_values(by="envio_id").reset_index(drop=True)
    df["envio_id"] = range(1, len(df) + 1)
    
    # Guardar el archivo corregido
    df.to_csv(archivo_salida, index=False)
    print(f"Archivo corregido guardado como: {archivo_salida}")

# Uso del script
def main():
    archivo_entrada = "logistica.csv"  # Cambia esto por la ruta de tu archivo
    archivo_salida = "logistica_corregido.csv"
    corregir_logistica(archivo_entrada, archivo_salida)

if __name__ == "__main__":
    main()