#!/usr/bin/env python3
"""Here the creation of all courses"""

from course import Course
from my_courses import MyCourses

my_courses = MyCourses()

# Infrastructures et modèles
# Fondamentaux du Cloud
cloud_cm = Course("5MMFCLD_2024_S9_CM_G1", 5630, 1, my_courses)
cloud_tp1 = Course("5MMFCLD_2024_S9_TP_G1", 5629, 1, my_courses)
cloud_tp2 = Course("5MMFCLD_2024_S9_TP_G2", 5631, 0, my_courses)
# Réseaux avancés et sécurité
ras = Course("5MMRAS_2024_S9_CM_G1", 5602, 1, my_courses)

# Tronc commun ISI
# Algorithmique répartie
algo = Course("5MMALGR_2024_S9_CM_G1", 5617, 1, my_courses)
# Evénements ISI
even2 = Course("5MMEISI_2024_S9_CM2_G1", 5643, 1, my_courses)
even1 = Course("5MMEISI_2024_S9_CM_G1", 5642, 1, my_courses)
# Sécurité des SI
ssi_cm = Course("5MMSDSI_2024_S9_CM_G1", 5594, 1, my_courses)
ssi_td1 = Course("5MMSDSI_2024_S9_TD_G1", 5596, 0, my_courses)
ssi_td2 = Course("5MMSDSI_2024_S9_TD_G2", 5595, 1, my_courses)

# SHEME
# Anglais
anglais = Course("5MMANGL6_2024_S9_TD_G9", 19002, 1, my_courses)
# Sport
sport = Course("5MMAPSA_2024_S9_TD_G1", 18963, 1, my_courses)
# Droit et informatique
droit = Course("5MMDROI6_2024_S9_TD_G1", 9395, 1, my_courses)
# Retour d'expérience
rex = Course("5MMREX_2024_S9_TD_G1", 9422, 1, my_courses)

# Systèmes d'information et projets
# Challenge Open Data
cod = Course("5MMCOD7_2024_S9_Projet_G1", 5636, 1, my_courses)
# Projet Intelligence Articielle
pia_cm = Course("5MMPIA_2024_S9_CM_G1", 5620, 1, my_courses)
pia_sou = Course("5MMPIA_2024_S9_Soutenance_G1", 5623, 1, my_courses)
pia_tp = Course("5MMPIA_2024_S9_TP_G1", 5622, 1, my_courses)
# Projet objets connectés
poc = Course("5MMPOC_2024_S9_Projet_G1", 5605, 1, my_courses)

# Données et systèmes
# Gestion des données à gd échelle
gdge_cm = Course("5MMGDDGE_2024_S9_CM_G1", 5612, 1, my_courses)
gdge_ctd = Course("5MMGDDGE_2024_S9_CTD_G1", 5610, 1, my_courses)
gdge_tp = Course("5MMGDDGE_2024_S9_TP_G1", 5613, 1, my_courses)
# Système distribué
sysd_cm = Course("5MMSYSD_2024_S9_CM_G1", 5589, 1, my_courses)
sysd_tp = Course("5MMSYSD_2024_S9_TP_G1", 5590, 1, my_courses)
