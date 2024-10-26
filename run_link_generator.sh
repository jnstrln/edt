#!/bin/bash

# Exécute le script Python et capture la sortie
url=$(./py_sources/link_generator.py)

# Ouvre l'URL dans Firefox
firefox "$url"

# Supprime le dossier __pycache__ s'il existe
if [ -d "py_sources/__pycache__" ]; then
    rm -r py_sources/__pycache__
fi
