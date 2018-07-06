# Table of Contents
1. [Overview](#overview)
    - [To Contribute](#to_contribute)
2. [Scripts](#scripts)
    - [gunviolence.py](#gunviolencepy)
    - [rungun.py](#rungunpy)
    - [palette_dicts.py](#palette_dictspy)

# Overview

This README should be used as a reference for all of the scripts located within the
`/GoodreadsEDA/GoodreadsEDA/` directory of this project. Currently, this section is a work in
progress and will be updated as more general purpose scripts are created/updated.

### To Contribute.

I will try to follow my own rules to the best of my ability, so that clear documentation
is provided for both contributors and users of this project.

This means that for every commit a developer makes to this repo they also need to include:

1. In line comments for non-function related changes.

  - Use your head when it comes to this, if you're just printing something out, you
    probably don't exhaustive documentation, but things like indexing certain elements
    in lists should probably include an in line comment explaining what you are grabbing
    from a list because it is not always clear.

  - You don't need to comment every single line, but should highlight what certain sections
    of the code are doing. Do these four lines process textual data? Comment it. Do these
    six lines check to make sure what the user inputted, and what data is actually in the data
    consistent? Comment it.

2. Docstrings for function related changes.

  - Every single function must include an INFORMATIVE docstring to be submitted to this repo.
   No matter how clear you think your code is, always assume it isn't. Comments and
   docstrings are quite literally free. (I'm bad at this.)

  - Best practice is to write out what the inputs and outputs are for any function, that way
  no one has to read the function line by line to understand what it does. (I'm very bad at
  this.)

3. An Update to this file, and it's table of contents.
  - Every script will have it's own section in this file, and will also have it's own link
    to that section in the TOC. (I'm extremely bad at this.)

If in doubt, consider your audience might be users who are wholly unfamiliar with programming.
Or, assume I (who is looking over your code), am an idiot. Which is not a wholly unfounded assumption.

For questions or suggestions on formatting, etc, feel free to contact Trevor Grant at tjgran01@syr.edu.

# Scripts

## gunviolence.py

##### Created: 5/2018
##### Created by: Trevor Grant
##### Email Support: tjgran01@syr.edu
##### Created for: Generating plots and basic statistics for gun violence dataset.

#### What this script does:

Within this file is the `GunViolenceTool()` class. A class that is used to generate basic statistics, create linear models, and generate plots from the gun violence dataset.

#### *This file takes as input*:

The `GunViolenceTool()` needs a few data sets in order to run properly. These datasets are stored within the `../data/raw/` directory in this repository.

__Note: As mentioned in the `README.md` file within this project's main directory. The main gun violence dataset is not included. It can be found by visiting the link provided in the heading of that `README.md` file.__

#### *This script gives as output*:

Depending on the method run (for more detailed information on individual methods refer to the docstrings within the methods) the output could be a plot, or the results of an analysis outputted to the user's terminal window.

#### Notes, Future, etc:

Should be good for now - could definitely be cleaned up as importing all the data at this time isn't entirely necessary.

## rungun.py

##### Created: 5/2018
##### Created by: Trevor Grant
##### Email Support: tjgran01@syr.edu
##### Created for: Generating plots and basic statistics for gun violence dataset.

#### What this script does:

This script is used as a way to quickly run methods from `gunviolence.py`, if the user does not wish to run all of the method calls from a python shell.

#### *This file takes as input*:

Nothing, but it should be kept within the same directory as `gunviolence.py` in order to run.

#### *This script gives as output*:

Depending on the method run (for more detailed information on individual methods refer to the docstrings within the methods) the output could be a plot, or the results of an analysis outputted to the user's terminal window.

#### Notes, Future, etc:

Nada.

## palette_dicts.py

##### Created: 5/2018
##### Created by: Trevor Grant
##### Email Support: tjgran01@syr.edu
##### Created for: Generating plots and basic statistics for gun violence dataset.

#### What this script does:

A series of different palettes (listed as hex numbers), used by `gunviolence.py` for plotting.

#### *This file takes as input*:

Nothing, is used as a reference file by `gunviolence.py`

#### *This script gives as output*:

Nada.

#### Notes, Future, etc:

One could always use more color pallets.
