from setuptools import setup


setup(
    name='zettelpy',
    version='0.7.0',
    author='Santiago Gonzalez',
    author_email='santiagogonzalezbogado@gmail.com',
    description='Personal Knowledge System based on Zettelkasten',
    packages=['zettelpy'],
    entry_points={'console_scripts': ['zettelpy = zettelpy.__main__:main']},
)
