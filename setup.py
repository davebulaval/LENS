from setuptools import setup

setup(
    name="lens",
    version="0.1.0",
    description="A new metric for text simplification",
    author="Mounica Maddela",
    author_email="mmaddela3@gatech.edu",
    url="https://github.com/Yao-Dou/LENS",
    download_url="https://github.com/Yao-Dou/LENS/archive/refs/tags/v0.1.0.tar.gz",
    license="Apache license",
    packages=["lens"],
    install_requires=[
        "sentencepiece",
        "pandas",
        "transformers>=4.8",
        "pytorch-lightning",
        "jsonargparse==3.13.1",
        "torch",
        "numpy >= 1.20.0",
        "torchmetrics >= 0.7",
        "sacrebleu >= 2.0.0",
        "scipy >=1.5.4",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
    ],
)
