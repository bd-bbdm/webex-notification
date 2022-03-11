import os

import setuptools

version = os.getenv('VERSION', 'v0.0.0')


setuptools.setup(
    name="webEX_notify",
    version=version,
    install_requires=[
        "requests==2.27.1",
    ],
    entry_points={
        'console_scripts': [
            'webEX_notify=webhook.main:main',
        ],
    },
    author="nozomi.nishinohara",
    author_email="nozomi.nishinohara@belldata.co.jp",
    description="cisco webEX incoming webhook",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/nozomi-nishinohara/webex-notification",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.10',
)
