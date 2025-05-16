from setuptools import find_packages, setup

setup(
    name="pnpl",
    version="0.0.2",
    packages=find_packages(),
    install_requires=[
        "mne",
        "numpy",
        "pandas",
        "torch",
        "h5py",
        "huggingface_hub"
    ],
    author="Miran Özdogan",
    author_email="miran.ozdogan@trinity.ox.ac.uk",
    description="Load and process brain datasets for deep learning",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/neural-processing-lab/frozen-pnpl",
    classifiers=[
        "License :: OSI Approved :: BSD-3-Clause License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
)
