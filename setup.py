from setuptools import setup, find_packages
from typing import List

HYPHEN_DOT_E = '-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    
    try:
        with open(file_path) as file_obj:
            requirements = [req.strip() for req in file_obj.readlines()]
            
            if HYPHEN_DOT_E in requirements:
                requirements.remove(HYPHEN_DOT_E)

    except FileNotFoundError:
        print(f"Warning {file_path} not found.")

    return requirements

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Hitesh Gupta",
    author_email="hiteshgupta2006@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)