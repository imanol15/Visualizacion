from elasticsearch import Elasticsearch
from datetime import datetime, timedelta
import random

# Establece una conexión con Elasticsearch
es = Elasticsearch("http://localhost:9200")

# Datos simulados de máquinas y operaciones en una fábrica
machine_ids = [f'Máquina-{i}' for i in range(1, 21)]  
operations = ['Inicio', 'Parada', 'Mantenimiento', 'Error', 'Reinicio']
statuses = ['Operativa', 'No operativa', 'En mantenimiento', 'Defectuosa']

# Función para generar datos de ejemplo
def generate_data():
    timestamps = [datetime.now() - timedelta(hours=i) for i in range(100)]  # Datos de las últimas 100 horas
    
    for _ in range(100):  # Generar 100 documentos
        doc = {
            'id_máquina': random.choice(machine_ids),
            'operación': random.choice(operations),
            'estado': random.choice(statuses),
            'marca_temporal': random.choice(timestamps),
            'duración': random.randint(1, 120)  
        }
        yield doc

# Insertar los datos generados en Elasticsearch
for doc in generate_data():
    res = es.index(index="indice-operaciones-fabrica", document=doc)
    print(f'ID del documento: {res["_id"]} insertado.')

# Confirmación de la inserción de documentos
print("Inserción de datos completa. Revisa tu cluster de Elasticsearch.")
