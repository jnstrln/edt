#!/bin/bash

# Exécute le script Python et capture la sortie
url=$(python3 /home/jeanstierlin/Documents/perso/edt/py_sources/link_generator.py)

# Ouvre l'URL dans Firefox
firefox "$url"
