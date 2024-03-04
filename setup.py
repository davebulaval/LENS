from setuptools import setup, find_packages

packages = find_packages()

setup(
    name="lens",
    version="0.2.1",
    description="A new metric for text simplification",
    packages=packages,
    install_requires=[
        "sentencepiece>=0.1.96",
        "pandas>=1.1.5",
        "transformers>=4.8",
        "pytorch-lightning>=1.6.0",
        "jsonargparse==3.13.1",
        "torch>=1.6.0,<2",
        "numpy>= 1.20.0",
        "torchmetrics>= 0.7",
        "sacrebleu>= 2.0.0",
        "scipy>=1.5.4",
    ],
)
