from setuptools import setup,find_packages #

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="MLOPS-PROJECT",
    version="0.1",
    author="Leo",
    packages=find_packages(), #busca entre todos los archivos.py
    install_requires = requirements,
)