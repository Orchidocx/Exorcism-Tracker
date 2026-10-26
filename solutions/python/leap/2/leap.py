"""Module providing a function printing python version."""
import sys

def print_sys_version():
    print(sys.version)
    
def leap_year(year):
    if year % 100 == 0:
        return year % 400 == 0
    return year % 4 == 0
