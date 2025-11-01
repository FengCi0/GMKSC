from setuptools import setup, find_packages

setup(
    name='gmksc',
    version='1.0.0',
    author='Feng Ci',
    author_email='1719444178@qq.com',
    description='Graph Marker-KEM Stream Cipher',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["cryptography"],
    python_requires=">=3.8",
)
