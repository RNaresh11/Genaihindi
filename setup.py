from urllib.request import install_opener
from setuptools import find_packages,setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='naresh',
    author_email="nareshrawat112002@gmail.com",
    install_requires =['openai','langchain','streamlit','python-dotenv','PyPDF2'],
    packages=find_packages()
)