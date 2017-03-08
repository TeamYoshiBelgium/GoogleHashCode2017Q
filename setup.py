from distutils.core import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='hash_code_2017_q',
    version='1.0.0',
    packages=['hash_code_2017_q'],
    url='',
    license='',
    author='',
    author_email='',
    description='',
    long_description=readme(),
    install_requires=[
      ],
    classifiers=[
        '',
    ],
    keywords='',
    include_package_data=True,
    zip_safe=True,
    entry_points={
        'console_scripts': ['package=package.command_line:main'],
    },
    test_suite='nose.collector',
    tests_require=['nose', 'nose-cover3'],
)