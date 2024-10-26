#!/usr/bin/env python3
"""Here the Course class definition"""

class Course:
    """Course class"""
    def __init__(self, name, edt_code, selected, my_courses):
        self.__name = name
        self.__edt_code = edt_code
        self.__selected = selected
        my_courses.update_my_courses(self)

    def get_name(self):
        """Function docstring."""
        return self.__name

    def get_edt_code(self):
        """Function docstring."""
        return self.__edt_code

    def get_selected(self):
        """Function docstring."""
        return self.__selected

    def __repr__(self):
        return f"Course(edtCode='{self.__edt_code}', code='{self.__name}')"
