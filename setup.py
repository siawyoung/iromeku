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
    package_data={"iromeku": ["py.typed"]},
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'pillow',
    ],
)
