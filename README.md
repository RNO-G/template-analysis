# Template repository for an analysis

## Contents of the dummy package:
- `requirements.txt` with external python packages required / used in your code
- `setup.py` which is needed to install the current directory as a package. Edit with your package name, version number and contact details
- `template_analysis` directory containing all your code, rename to your package name

## Suggested directories in package
- `data`: containing tabulated results from scripts. Edit `.gitignore` to not push huge files to github
- `plots`: containing final result plots. Edit `.gitignore` to not push non-final plots to github


# 1. Installation
Clone repository, change to the directory and install. The `-e` option installs the package in editable mode under the current path, which allows to edit scripts without reinstalling.

```
git clone git@github.com:RNO-G/template-analysis.git && cd template-analysis
pip install -r requirements.txt -e .
```
# 2. Use of `template_analysis` outside the package
After installing you can use all the code inside `template_analysis` from anywhere on your machine.
E.g.: 
```
(pyvenv) shallmann@Steffens-MBP ~ % python -i
Python 3.10.9 (main, Dec 15 2022, 18:25:35) [Clang 14.0.0 (clang-1400.0.29.202)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from template_analysis import example
>>> example.example()
I am a minimal example doing nothing!
```

# 3. Adding command line scripts
It is possible to add command line entry points to `setup.py`. As an example, `run-template-analysis` is set to execute the `main` function in `template_analysis/run.py`.

E.g.:
```
(pyvenv) shallmann@Steffens-MBP ~ % run-template-analysis -h  
usage: run-template-analysis [-h] n_points

Template analysis

positional arguments:
  n_points

options:
  -h, --help  show this help message and exit

(pyvenv) shallmann@Steffens-MBP ~ % run-template-analysis 1000
writing output to /Users/shallmann/Desktop/analysis-template-repo/template_analysis/data/step1_result_1000.txt
writing plot generated from /Users/shallmann/Desktop/analysis-template-repo/template_analysis/data/step1_result_1000.txt to /Users/shallmann/Desktop/analysis-template-repo/template_analysis/plots/step1_result_1000.png
```
