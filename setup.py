
from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """
    This function will return a list of requirements.
    """
    requirement_lst: List[str] = []  
    try:
        with open("requirements.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                # Only add non-empty lines that are not '-e .'
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")
        
    return requirement_lst

print(get_requirements())


setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="vathsalasivapalan",
    author_email="vathsalasivapalan@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)


