import random

adjetivos = ["curioso", "Peludo", "chiquito", "Dulce", "Travieso"]
nombres = ["Borromeo", "Loli", "Lolo", "Sultan", "Carito"]

nombre_mascotas = random.choice(adjetivos) + ' ' + random.choice(nombres)

print("Tu nueva mascota se llama: ", nombre_mascotas)
