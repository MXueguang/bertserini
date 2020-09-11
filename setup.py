import setuptools

with open('README.md') as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name='bertserini',
    version='0.0.1',
    packages=['bertserini', 'bertserini.eval', 'bertserini.retriever'],
    url='https://github.com/rsvp-ai/bertserini',
    license='',
    author='bertserini',
    author_email='x93ma@uwaterloo.ca',
    description='An end-to-end Open-Domain question answering system',
    install_requires=requirements,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
