# GunDeathsEDA
### By: Trevor Grant

This project was created the satisfy the requirements for the EDA / Regression project
at K2 Data Science bootcamp.

##### Important: The original dataset that I am working off of for this exploration is not included in this repo (it's too big to store on GitHub without me shelling out money! [Which is chilling, actually]). The original file can (and should) be downloaded from the kaggle link in the Goal section.

##### If you wish to play around with some of the scripts and stuff in this repo place that .csv file into `.\data\raw\` and name in `gun_v.csv`

## Goal:

This project is an exploration of a gun violence dataset posted to Kaggle.com:

https://www.kaggle.com/jameslko/gun-violence-data

The main exploration in this project will involve looking at the relationship between state population and the number of gun deaths and injuries that that particular state has had in recent years (2013-2018).

Once the initial exploration has been conducted, we will look for noteworthy outliers (i.e. states that per their population should have a significantly lower or higher rate of gun releated deaths or gun related injuries) and *attempt* to explore what may be the extraneous factors that are either driving the rate of gun violence up or down in that particular state.

**The Writeup for this project is located at:**

`/docs/writeup/README.md`

## Requirements:

Because I love f-strings more than my girlfriend loves me (low hurdle to volley over, I know), these scripts require at least Python 3.6 in order to run on your own machine.

If you are following along via the tutorial and do not wish to use Python 3.6 you can feel free to use the `.format()` string method.

i.e whenever you see me do something like this:

`1. x = "formatted"`

`2. print(f"Here is a {x} string.")`

You may use the `format()` function instead. (But in all honesty, get with the times.)

`1. x = "formatted"`

`2. print("Here is a {0} string.".format(x))`

__Note__: This project has been tested only on MacOSX Sierra (don't get with the times when it comes to
to High Sierra), but it should work in most MacOS and Linux environments, and probably Windows as well. I don't believe I am doing anything that wouldn't be platform independent.

### Installing Requirements.

For further requirements see `requirements.txt`, or just plop all the requirements into a python virtual environment:

from the command line (In the main project directory):

1. Create the virtual environment.

  `python3.6 -m venv venv`

2. Activate the virtual environment.

  `source venv/bin/activate`

3. Install the project requirements.

  `pip install -r requirements.txt`

4. Throw a party.

## EDA Questions.

The project as it currently stands is interested in exploring two questions:

1. Does public policy (i.e. stricter gun regulation) have reduce the number of deaths we might expect to see in a state given it's population?

2. Does Giffords Scorecard (http://lawcenter.giffords.org/scorecard/) for gun policy state rankings have an empirical effect (i.e. do states with high scorecard rankings actually reduce the amount of gun injuries and deaths [Or is their gun law state ranking a baloney measure]).

## (No so Quick)start.

1. Download the original Kaggle dataset.

Again: https://www.kaggle.com/jameslko/gun-violence-data

2. Move that bad boy into `/data/raw`.

3. Name that bad boy `gun_v.csv`

4. Install your virtual environment. (See above section on installing requirements if you are unsure how to do this.)

5. Install requirements once you've activated the virtual environment.

  `pip install -r requirement.txt`

6. Navigate to `./explore`

7. Open up your python shell and import the gunviolence tool, and create a `GunViolenceTool()` instance.

  `from gunviolence import GunViolenceTool`
  `gvt = GunViolenceTool()`

8. Refer to my bad documentation forever.
