# Casualty

# Table of content
- [Instalation](#instalation)
- [Folders](#folders)
  - [myscripts](#myscripts)
  - [notebooks](#notebooks)
  - [tests](#tests)

## Installation
- Install Packages
```
git clone 
cd Causal_inference
pip install -r requriements.txt
```

- Jupyter Noteboks
```
cd notebooks
jupyter notebook
```

## Folders
Folder structure of the project try to follwo more organized and modularized format.

#### myscripts:
This folder contain python modules. The main purpose of this forlder is for code modularization and increase code reusability. 

- ```file.py```: python module concerned with reading csv files from file and haldeling errors while reading the file.
- ```plot.py``` : python module concerned with generating graphs and plots from provided data frame.

#### notebooks:
This folder contain notebooks files that are necessary for data exploration and to get more indepth analysis on the data set.
- ```EDA``` : Notebook file for making exploratory data analysis and help us understand more about the data.

#### tests:
This folder contain test files for critical part of the application.

## Technologies uses
- ```DVC``` : for remote storage and data versioning.
- ```CML```: for getting model performance result when we push our code. 
