#!/usr/bin/env python3
"""Here the MyCourses class definition"""

class MyCourses:
    """MyCourses class"""
    def __init__(self):
        self.__selected_courses = []

    def update_my_courses(self, course):
        """Ajoute un cours à la liste des cours sélectionnés si selected == 1"""
        if course.get_selected() == 1:
            self.__selected_courses.append(course)

    def get_selected_courses(self):
        """Retourne la liste des cours sélectionnés"""
        return self.__selected_courses

    def __repr__(self):
        return f"MyCourses({len(self.__selected_courses)} cours sélectionnés)"
