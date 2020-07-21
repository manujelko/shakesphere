from setuptools import setup, find_packages

with open("README.md", "r") as stream:
    long_description = stream.read()


def read_requirements(file):
    with open(file, "r") as stream:
        content = stream.read()
    return content.split("\n")


setup(
    name="shakesphere",
    version="0.1.0",
    author="Manuel Saric",
    author_email="manujelko@gmail.com",
    description="Shakespearean Pokemon descriptions API.",
    long_description=long_description,
    url="https://packaging.python.org/tutorials/packaging-projects/",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=read_requirements("requirements.txt"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
