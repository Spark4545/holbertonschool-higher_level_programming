#!/usr/bin/python3
"""
Module 9-student
Contains class Student
that initializes public instance attributes first_name, last_name, and age,
and has public method to_json that retrieves its dictionary representation
"""


class Student():
    """
    Public Attributes:
        first_name
        last_name
        age

    Public Methods:
        to_json: retrieves its dictionary representation
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes student with full name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns:
            dictionaryu representation of student
        """
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
