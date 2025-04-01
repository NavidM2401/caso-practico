import pandas as pd

def corregir_datos(csv_path, output_path):
    # Cargar datos
    df = pd.read_csv(csv_path)
    
    # Eliminar filas completamente vacías
    df.dropna(how='all', inplace=True)
    
    # Ordenar por proveedor_id
    df = df.sort_values(by='proveedor_id')
    
    # Resetear el índice de proveedor_id de forma secuencial
    df['proveedor_id'] = range(1, len(df) + 1)
    
    # Guardar el archivo corregido
    df.to_csv(output_path, index=False)
    print(f"Archivo corregido guardado en: {output_path}")

# Uso del script
corregir_datos('proveedores.csv', 'proveedores_corregidos.csv')
