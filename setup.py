import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="iromeku-siawyoung", # Replace with your own username
    version="0.0.1",
    author="Lau Siaw Young",
    author_email="sy@siawyoung.com",
    description="A package for extracting dominant colours from images.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/siawyoung/iromeku",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
