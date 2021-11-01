from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="Bappy Ahmed",
    description="A small package for FaceRecogAcademy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/entbappy/DVC-ML-DEMO",
    author_email="entbappy73@gmail.com",
    packages=["src"],
    python_requires=">=3.6",
    install_requires=[
        'tensorboard==1.14.0',
    ]
)