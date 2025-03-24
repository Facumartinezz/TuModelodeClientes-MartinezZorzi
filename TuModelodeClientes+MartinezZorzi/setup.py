from setuptools import setup, find_packages

setup(
    name='paquete1',
    version='0.1.0',
    author='Facundo Martinez Zorzi',
    author_email='facundomzorzi@hotmail.com',
    description='Una aplicación para gestionar clientes en una página de compras.',
    packages=find_packages(),
    install_requires=[
        # Aquí puedes agregar las dependencias necesarias
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)