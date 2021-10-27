# 599-Knitting-Assignments
This repository contains the code needed to complete the programming assignments in UW CSE 599 on E-Textiles for the Fall Quarter of 2021.


## Installation
In the command line, type:
```console
git clone https://github.com/mhofmann-uw/599-Knitting-Assignments.git
```
Next, change into the working directory by typing:
```console
cd 599-Knitting-Assignments
```
(*note: if you installed the repo in a subdirectory, make sure to type out the full path.*)

If you have trouble opening the file, you likely need to run the following commands:
```console
git submodule init
git submodule update
```
^*These commands initialize and update the submodules (other Git repos) that the visualizer depends on.*

See the github documentation on [cloning a repository](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository) if you need assistance with installation.



## Set Up

This project may work on older versions of Python, but it was developed with Python 3.9

Particularly if you are a Windows User I highly recommend running this code as a [PyCharm Project](https://www.jetbrains.com/help/pycharm/importing-project-from-existing-source-code.html).

Otherwise:

Install the required packages using the `requirements.txt` file:

`pip install -r requirements.txt` while in the project directory.

Add the project directory to your `PYTHONPATH`

In Unix machines: `export PYTHONPATH="${PYTHONPATH}:/path/to/your/project/"`

For Windows: `set PYTHONPATH=%PYTHONPATH%;C:\path\to\your\project\`

Now you should be able to access main methods from cmd line (e.g., `python tests\test_simple_knitgraphs.py`)



## Package Structure
Assignment 1 is spread across two packages and the test package

### knit_graphs
This package contains the classes used to create a knit graph (Loop, Yarn, Knit_Graph, Pull_Direction(Enum)). Methods in these classes need to be implemented to complete Assignment 1

### debugging_tools
This package contains a visualizer method to help visualize simple knitgraphs. This may be useful to extend for debugging future projects
It also contains a set of simple knitgraph which manually generate some simple textures. In future assignments we will make it easier to define more complex knit graphs. 2 of these textures need to be implemented for assignment 1

### knitting_machine
This package contains a representation of a v-bed knitting machine and 'KnitoutGenerator' class to create knitout 
instructions by manipulting that machine-state. Knitout operations are in the machine_operations file.

## Assignment submission readmes

### Assignment: Connecting Dots
The five images are in `./sample_results/hw1`. I fixed a couple of typos in the code (marked with #comment) and in the comments (unmarked).

### Assignment: KnitGraphs to Knitout
The five knitout files are in `./sample_results/hw3`. I fixed a couple of typos in the comments and a couple of bugs in my hw1 code.
