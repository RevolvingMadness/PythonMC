from setuptools import setup, find_packages

setup(
    name="pythonmc",
    version="1.0.5",
    author="RevolvingMadness",
    author_email="revolvingmad@gmail.com",
    description="The python library for PythonMC",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/RevolvingMadness/PythonMC",
    project_urls={"Bug Tracker": "https://github.com/RevolvingMadness/PythonMC/issues"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages("src"),
    package_dir={"": "src"},
    python_requires=">=3.9",
    package_data={"pythonmc": ["py.typed"]},
)
