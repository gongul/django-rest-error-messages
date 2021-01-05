import setuptools

setuptools.setup(
    name="django-rest-inherits-error-messages",
    version='1.0.0',
    license='MIT',
    author='gongul',
    author_email='projectgongul@gmail.com',
    description='ModelSerializer inherits the error_messages of the model',
    long_description=open('README.md').read(),
    url='https://github.com/gongul/django-rest-inherits-error-messages',
    packages=setuptools.find_packages(),
    install_requires=[
        'Django>=1.8.0',
        'djangorestframework>=3.1.3'
    ],
    tests_require=[
        'Django>=1.8.0',
        'djangorestframework>=3.1.3'
    ],
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
    ],
)