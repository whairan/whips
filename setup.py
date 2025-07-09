from setuptools import setup, find_packages

setup(
    name="game1",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pygame>=2.5.0",
        "pygame-gui>=0.6.0",
        "numpy>=1.24.0",
        "pymunk>=6.4.0",
        "pyyaml>=6.0.0",
    ],
    entry_points={
        "console_scripts": [
            "game1=main:main",
        ],
    },
    package_data={
        "": ["assets/**/*"],
    },
    python_requires=">=3.9",
)
