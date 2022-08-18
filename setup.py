from setuptools import setup, find_packages

setup(
    name="heic-to-jpg",
    version="1.0.0",
    description="Convert HEIC to JPG",
    url="https://github.com/younesaassila/heic-to-jpg",
    author="Younes Aassila",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6, <4",
    install_requires=["click"],
    entry_points={
        "console_scripts": [
            "heic-to-jpg=heic_to_jpg:main",
        ],
    },
)
