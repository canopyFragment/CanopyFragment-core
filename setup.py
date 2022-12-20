import setuptools

packages = [
    "can",
]

# Install
setuptools.setup(
    name="can",
    version="1.0.0",
    description="core all news",
    author="Leo Cances",
    author_email="leocances@gmail.com",
    url="",
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    python_requires=">=3.8",
)
