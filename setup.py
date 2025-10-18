from setuptools import setup, find_packages

# Figure out requirements from requirements.txt. This was generated with pipreqs.
with open("requirements.txt") as f:
    install_requires = f.read().splitlines()

setup(
    name="agviz",
    version="1.0.0",
    description="AutoGrad Visualizer (agviz): Visualize dependencies between states/parameters in autograd tree.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="James Hazelden",
    url="https://github.com/meeree/agviz",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=install_requires,
    python_requires=">=3.2",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
