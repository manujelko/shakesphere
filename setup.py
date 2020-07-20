from setuptools import setup, find_packages

with open("README.md", "r") as stream:
    long_description = stream.read()


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
    install_requires=[
        "bottle",
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
