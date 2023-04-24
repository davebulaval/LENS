from setuptools import setup, find_packages

packages = find_packages()

setup(
    name="lens",
    version="0.2.0",
    description="A new metric for text simplification",
    packages=packages,
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
)
