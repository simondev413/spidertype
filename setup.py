from setuptools import  setup,find_packages

setup(
    name='SpiderType',
    version='1.0',
    packages=find_packages(include=['spidertype','spidertype.*']),
    install_requires=[],
    author='Simão Domingos De Oliveira António',
    author_email='simãodomingos@gmail.com',
    description='A Python library for advanced type manipulatio and static typing management.',
    long_description=open('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/simondev413/spidertype',
    classifiers=[
        'Development status :: 3 - Alpha',
        'Intendent Audience :: Developers',
        'Licence :: OSI Approved :: Apache Software Licence',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    python_requires='>=3.7',
    test_suit='tests',
    tests_require=[
        'pytest',
    ],
    entry_points={
        'console_scripts':[
            
        ]
    }

)