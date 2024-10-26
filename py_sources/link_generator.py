#!/usr/bin/env python3
"""Here the generation of the link"""

from courses_creation import my_courses

selected_courses = my_courses.get_selected_courses()
my_edt_codes = []
for course in selected_courses:
    my_edt_codes.append(str(course.get_edt_code()))

link = "https://edt.grenoble-inp.fr/2024-2025/ensimag/etudiant/jsp"
link += "/custom/modules/plannings/direct_planning.jsp?resources="
link += ",".join(my_edt_codes)

print(link)
