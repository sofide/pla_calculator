import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pla_calculator",
    version="0.0.1",
    author="Sofía Denner",
    description="A small package to calc how much PLA filament you have left.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sofide/pla_calculator",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    entry_points={"console_scripts": ["pla_calculator=pla:main"]}
)
