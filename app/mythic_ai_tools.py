# Project: Mythic AI Toolkit - Packaging for Installation

# Directory Structure:
# mythic_ai/
# ├── __init__.py
# ├── cli.py
# ├── core.py
# └── streamlit_ui.py
# setup.py
# README.md
# requirements.txt
# .github/workflows/deploy.yml

# File: setup.py
from setuptools import setup, find_packages

setup(
    name='mythic_ai_tools',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'sounddevice',
        'numpy',
        'matplotlib',
        'transformers',
        'streamlit'
    ],
    entry_points={
        'console_scripts': [
            'mythic-ai=mythic_ai.cli:main'
        ]
    },
    author='Mythic Systems',
    description='Myth-inspired AI tools for symbolic cognition and emotional computing.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)

# File: requirements.txt
sounddevice
numpy
matplotlib
transformers
streamlit

# File: README.md
# Mythic AI Toolkit

A Python package of myth-inspired tools drawn from the ancient Soboba and Luiseño legends. Includes:
- Acoustic signal synchronizer (UuyotSync)
- Nature transformation map (SiwashMorpher)
- Sentiment gatekeeper (EchoVoice)
- Memory loop visualizer (ElsinoreMap)
- Dawn-time script trigger (SunriseScript)

## Installation
```bash
pip install .
```

## CLI Usage
```bash
mythic-ai --chant
mythic-ai --morph Ayasha 13
mythic-ai --echo "Thank you for the story."
mythic-ai --loops
mythic-ai --ritual
```

## GUI
```bash
streamlit run mythic_ai/streamlit_ui.py
```

# File: .github/workflows/deploy.yml
name: CI

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
    - name: Test CLI
      run: |
        python mythic_ai/cli.py --chant
