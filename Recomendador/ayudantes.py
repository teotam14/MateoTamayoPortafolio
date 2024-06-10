import pandas as pd
import pickle
import os

# Combinar las partes
data_bytes = bytearray()
num_parts = len([name for name in os.listdir() if name.startswith('part_')])

for i in range(num_parts):
    with open(f'part_{i}.pkl', 'rb') as f:
        part = f.read()
        data_bytes.extend(part)

# Convertir los bytes combinados de nuevo al objeto original
data = pickle.loads(data_bytes)


def hacer_recomendacion(item_id: int, n: int = 10):
    # Verifica que el item exista en la matriz
    if item_id in data['id1'].unique():
        # Filtra donde 'id1' sea igual al item proporcionado
        recomendaciones = data[data['id1'] == item_id]
        
        # Ordena por similitud de manera descendente y selecciona los primeros n resultados
        recomendaciones = recomendaciones.sort_values(by='similitud', ascending=False).head(n).reset_index()
        
        return recomendaciones

