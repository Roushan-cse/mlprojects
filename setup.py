from setuptools import find_packages,setup

HYPEN_E_DOT = "-e ."
def get_requirements(file_path:str)->list[str]:
    """
    This function will return list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","")for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)


setup(
    name = "mlproject",
    version = "0.0.1",
    author = "Roushan",
    author_email="rkak9798770202@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)