from setuptools import setup, find_packages

setup(
    name='me-ai',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'fastapi>=0.68.0',
        'uvicorn>=0.15.0',
        'python-dotenv>=0.19.0',
        'pydantic>=1.8.2',
        'openai>=0.27.0',
        'python-multipart>=0.0.5',
    ],
    extras_require={
        'dev': [
            'pytest>=6.2.5',
            'pytest-cov>=2.12.1',
            'pytest-mock>=3.6.1',
            'httpx>=0.18.2',
        ]
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='An AI-powered personal assistant',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/xaiksan1/Me-Ai',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
