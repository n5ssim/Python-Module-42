import os


os.hello

def hello():
    x = 42  # Cette variable est inutile, Ruff doit le voir
    print("test")


hello(123)  # Erreur : he:q
llo n'accepte pas d'argument, Pyright doit le voir
