import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="iromeku",
    version="0.0.1",
    author="Lau Siaw Young",
    author_email="sy@siawyoung.com",
    description="A package for extracting colours from images.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/siawyoung/iromeku",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'pillow',
    ],
    python_requires='>=3.5',
)
