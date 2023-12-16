# Crear una colección de muestra
users = {"Hans": "active", "Éléonore": "inactive", "景太郎": "active"}

print("Usuarios originales:", users)

# Estrategia: Iterar sobre una copia
for user, status in users.copy().items():
    if status == "inactive":
        del users[user]

print("Usuarios después de eliminar los inactivos:", users)

# Estrategia: Crear una nueva colección
active_users = {}
for user, status in users.items():
    if status == "active":
        active_users[user] = status

print("Usuarios activos en la nueva colección:", active_users)
