# GunDeathsEDA
### By: Trevor Grant

This project was created the satisfy the requirements for the EDA / Regression project
at K2 Data Science bootcamp.

## Goal:

This project is an exploration of the a gun violence dataset posted to Kaggle.com:

https://www.kaggle.com/jameslko/gun-violence-data

The main exploration in this project will involve looking at state by state comparisons between state populations, and state percetage of population located in urban areas to see how these variables affect the number of gun deaths and injuries that that particular state has had in recent years (2013-2018).

Once the initial exploration has been conducted, we will look for noteworthy outliers (i.e. states that per their population should have a significantly lower or higher rate of gun releated deaths or gun related injuries) and *attempt* to explore what may be extraneous factors that are either driving the rate of gun violence up or down in that particular state.

**The Writeup for this project is located at:**

`/docs/writeup/README.md`

## Requirements:

Because I love f-strings more than my girlfriend loves me (low hurdle to volley over, I know), I'm requiring you have at least Python 3.6 in order to run these scripts on your own machine.

If you are following along via the tutorial and do not wish to use Python 3.6 whenever you see me do something like this:

```x = "formatted"

print(f"Here is a {x} string.")```

You may use the `format()` function instead. (But in all honesty, get with the times.)

```x = "formatted"

print("Here is a {0} string.".format(x))```

__Note__: that this has been tested only on MacOSX Sierra (don't get with the times when it comes to
to High Sierra), but it should work in most MacOS and Linux environments, and probably Windows as well. I don't do anything too fancy.

For further requirements see `requirements.txt`.

## EDA Questions.

The project as it currently stands is interested in exploring two questions:

1. Does public policy (i.e. stricter gun regulation) have reduce the number of deaths we might expect to see in a state given it's population?

2. Does Giffords Scorecard http://lawcenter.giffords.org/scorecard/ for gun policy state rankings have an empirical effect (i.e. do states with high scorecard rankings actually reduce the amount of gun injuries and deaths [Or is the gun law rank a baloney measure]).

## Quickstart.
