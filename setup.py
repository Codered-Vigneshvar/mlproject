from setuptools import setup, find_packages
from typing import List
HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This Function will Call the List of Requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements        
            
setup(
    name="ML_Project",
    version="1.0.0",
    author="Vigneshvar",
    author_email="vigneshvars2001@gmail.com",
    description="A simple Python project",
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt'),
)
