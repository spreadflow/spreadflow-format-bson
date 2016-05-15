from setuptools import setup

setup(
    name='SpreadFlowFormatBSON',
    version='0.0.1',
    description='BSON message interchange format for SpreadFlow metadata extraction and processing engine.',
    author='Lorenz Schori',
    author_email='lo@znerol.ch',
    url='https://github.com/znerol/spreadflow-format-bson',
    packages=[
        'spreadflow_format_bson',
        'spreadflow_format_bson.test'
    ],
    install_requires=[
        'pymongo'
    ],
    test_suite="spreadflow_format_bson.test",
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Twisted',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Multimedia'
    ],
)
