import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="randypy",
    version="0.1.0",
    author="dinogarlic",
    author_email="xldpsl1003@gmail.com",
    description="A Python library for generating random data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Dinogarlic/RandyPy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
