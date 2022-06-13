
# Setting up your computer for coding




## Anaconda

As you start doing research you will likely need to use a number of different python packages, sometimes even different python versions. 


Anaconda is a mostly platform-independent software management system that makes your life a lot easier! Highly recommended. There is some alternatives but most people use anaconda

https://www.anaconda.com

* Most standardized way to install Python, tools etc. on Windows and Mac OS, very large community!
* Bundles almost all useful Python packages out of the box!

### How to find information

To get a full understanding of a program or to help remember important commands you can look for documentations and cheat cheets. For example for anaconda

https://docs.conda.io/projects/conda/en/latest/user-guide/index.html

https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf


## Using conda 

Once you have installed anaconda on your system you can create distinct environemnts to run your code in. If you are on windows be sure to check the box that says "Add Anaconda to my PATH environment variable" during installation.


To create a new environment you can run in your command line. If you need a specific version you can add python=3.9

```
conda create --name REUWorkshop 
```

Once the environment is created you can switch to it. (on Windows you might want to use the anaconda command prompt not CMD)

```
conda activate REUWorkshop 
```


Once the environemnt you want to work in is active you can go ahead and install packages you need.


```
conda install numpy
```

If you are using special packages for your research sometimes conda might not find them. Then you can try using pip. This is a little more risky but needed for some packages.

Once you have all the packages you need you can run python code from the command line


```
python part4_classExample.py
```

## Jupyter

To run juypter notebooks on your machine you need to install the accociated package: https://jupyter.org/install , then start a jupyter kernel and open it in your browser



```
jupyter notebook
```

## Other things

There is a number of other useful software that you can look into using in your workflow

* git and github to create a version history of your code
* ssh and ssh keys to access remote machines
* code editors. Many of them offer convenient functionality like git integration and code highlighting. You can have a look at VSCode, Atom, Emacs and Vim