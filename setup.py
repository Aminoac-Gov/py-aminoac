from setuptools import setup, find_packages

setup(
    name="pyaminoac",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "flask",
        "jieba",
        "pypinyin",
        "click",
        "zhconv",
    ],
    entry_points={
        'console_scripts': [
            'pyaminoac=pyaminoac.cli:main',
        ],
    },
    author="liyanqwq",
    author_email="liyanqwq@gmail.com",
    description="A tool for translating Chinese to Aminoac",
    keywords="chinese, translation, aminoac",
    python_requires=">=3.6",
)