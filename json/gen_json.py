import json

# Crear la lista de objetos con los pares de números y Nombre inicializado a null
data = []
for i in range(500):
    obj = {
        "numeros": [
            f"{i:03d}",
            f"{i + 500:03d}"
        ],
        "Nombre": None
    }
    data.append(obj)

# Crear el diccionario principal
result = {"data": data}

# Convertir el diccionario a una cadena JSON con indentación de 4 espacios para mayor legibilidad
json_data = json.dumps(result, indent=4)

# Guardar el JSON en un archivo (opcional)
with open('output.json', 'w') as f:
    f.write(json_data)

# Imprimir el JSON
print(json_data)

