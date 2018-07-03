## Writeup.

This project was created the satisfy the requirements for the EDA / Regression project
at K2 Data Science bootcamp.

This is the long, drawn out, version of the write up in which I explain where all of the data came from and give the project some context. To view a more concise version of this writeup, check out `./SUMMARY.md` in this directory.

### Table of Contents
1. [Introduction](#introduction)
2. [Methods](#methods)
  - [Gathering The Data](#gathering-the-data)
  - [Cleaning and Exploring the Data](#cleaning-and-exploring-the-data)
  - [Generating Regression Plots](#generating-regression-plots)
3. [Results](#results)
4. [Discussion](#Discussion)

### Introduction.

Gun violence in the United States has, throughout the years, become a 'hot button' political issue. Oftentimes, the debate is stalemated when the two parties on opposite sides of the debate realize they they are typically arguing past one another, highlighting specific values while downplaying the other side's. Advocates for stricter gun policy often argue that that the sale and possession of firearms should be more regulated than the laws currently on the books require, and that if more strict regulations are put in place then the amount of gun related deaths and injuries will decrease. The opposition contests that limiting the sale, or increasing regulation on firearms, will unjustly infringe upon law-abiding gun owner's second amendment rights. These two arguments both have a valid place in the marketplace of ideas, the gun-control advocate arguing from a place of valuing human life over personal liberty, the second amendment rights advocate arguing that personal liberty comes at a cost, and that the cost in the case of the right to bear arms, is sometimes paid in the lives of people.

The above debate is not the stalemated arguments this project aims to look into. It is impossible for data to tell us what to value. The naturalistic fallacy written of in G.E. Moore's _Principia Ethica_ still ring as true today as they did over a century ago. To paraphrase: We cannot infer _an ought_ from _an is_. That is to say that just because the nature of the world has a certain set of affairs, it does not mean that that set of affairs is the morally correct. Exploring data will not inform us as to whether or the sacrifice of one life for two is a valid moral claim, nor will it tell us if an individual's right to x, outweighs another individual's right to y. That's above data's capabilities, and, frankly, above my pay grade.

What this project aims to do instead is to look at a weaker version of the over-aching arguments posited above, something data can give insights into. The weaker, and less philosophical, debate is an empirical one: What evidence is there that gun control policy actually does what it purports to do? i.e. Do stricter gun regulations _actually_ result in less gun related deaths, and if so, to what degree? This project will look into gun related deaths in the United States over the last five years (Jan 2013 - March 2018), and try to quantify and visualize the relationship between stricter gun policy and the amount of gun deaths.

### Methods

#### Gathering the Data.

I was first inspired to begin work on this project on by downloading and looking into a very thorough dataset posted to Kaggle.com. The dataset was posted by Kaggle user James Ko. According to the user's documentation, this data was compiled from the nonprofit organization Gun Violence Archive (gunviolencearchive.org) through various web scraping and data organization techniques. The data was downloaded in `.csv` format, and moved into this repository under the name `./data/raw/gun_v.csv`.

Though the Kaggle user did an excellent job of categorizing and organizing the `.csv` dataset posted, there were still a few other  variables that needed to be included in order to perform the regression analysis needed to complete this project. In order to perform a proper regression analysis, I decided that it was best to break the information down by state, as individual states oftentimes have gun laws that go above and beyond the federal requirements for purchasing a firearm. Since states vary greatly in population (max=39506094(CA), min=584447(WY), mean=6379576), population information about each state was downloaded from the Census Bureau (https://www.census.gov/), based on the 2010 census of the United States. That information was moved into this repository and stored in `./data/raw/state_pop.csv`. Though this measure may not be a perfect representation of state populations in 2018 the census counts were decided upon so as to avoid having to arbitrarily pick a population estimate value for each state between the years of 2013 - 2018, though these estimates are readily avilable and could be used instead of the census counts. Population was obtained to control for the amount of gun deaths in each state.

Finally, I needed some information about gun policy on the books in each state in the US. To obtain this information I visited the webpage for the Gifford's Law Center to Prevent Gun Violence, a public interest law center who promotes gun control measures as a way to counteract gun violence. The Gifford's page contained their 'ranking' of gun policy by state, with a grade of A+ being the best and a grade of F being the worst. They also ranked state's gun laws in order, with California being ranked highest, and Mississippi being ranked the lowest. It is important to consider that this group does advocate for stronger gun policy, and that their rankings reflect laws that that would like executed in all states. A high ranking from the Gifford's Law Center may therefore be viewed as a proxy for the strong regulations that gun control activists propose. This information, as well as information as to whether or not background checks were required for the purchase of a firearm in each state, was scraped from the site and compiled into a `.csv` file located at `./data/raw/gun_law_rank.csv`.

### Cleaning and Exploring the Data.

Once all the data were gathered into the project, preliminary exploration of the initial dataset gathered began. In the `./GunDeathsEDA/gunviolence.py` file, a class, `GunViolenceTool()`, was created, so that a `GunViolenceTool()` could be imported into a python shell and used for testing. Basic stats, and general information about the dataset were coded as attributes to the class, so that a user could easily import the tool and get meaningful information quickly. For instance, the user could find the deadliest incident in the dataset using just the following lines of code:

`>>>from gunviolence import GunViolenceTool`

`>>>gvt = GunViolenceTool()``

`>>>gvt.deadliest`

This code would return the incident in the dataset with the highest number of fatalities. For other attributes and basic states refer to the documentation for the `gunviolence.py` located at `./GunDeathsEDA/docs/README.md`.

After the ability to generate basic stats about the dataset and information about incidents was generated. A cleaned dataset was created which combined the information about gun deaths per state `n_killed`, state population `st_pop`, Giffords law center letter grade `st_letter_rank`, state law strength rank, `st_law_rank`, and whether or not a state had background checks `bg_check`. These pieces of information were generated through the `GunViolenceTool()` method `make_population_dataset()`, and stored at `./data/cleaned/gun_d_with_pop.csv` in this repository.

### Generating Regression Plots.

All of the the regression plots for this project were generated from the cleaned dataset created based on state populations and gun death rates. Although there was information about country and voting districts in the original dataset, which are interesting data and could be used in a more detailed analysis of gun violence in the US, this project decided to look at state by state information due to the fact that gun laws vary primarily by state, and not county. There are exceptions to this, such as New York City, which has stricter gun requirements than the rest of the state (https://www.nraila.org/gun-laws/state-gun-laws/new-york/), but these exceptions are not the general rule.

To generate the regression plots the `regplot()` method from the `seaborn` package was used. The plots were then styled and made clearer by custom `matplotlib` code, that would color states differently depending on the severity of the laws, or whether or not the states had background checks. Styling involved overriding default colors with a custom color palette, generating a custom legend, and in some cases labeling particular states in the dataset, so that someone looking at the chart would be able to see where some interesting data points might existed in the `regplot()`.

The regression plots with custom `matplotlib` styling code in this project are created by calling the `GunViolenceTool().gun_d_regplot_state_rank()` and `GunViolenceTool().gun_d_regplot_bcg()` methods to plot the information about state gun law ranks and whether or not a state required background checks respectively.

## Results

The first analysis run was to determine whether or not a single policy could be enacted in order to diminish the number of gun deaths in a particular state. In order to accomplish this an Ordinary Least Squares (OLS) linear regression model was created, using state population as the predictor variable. The regression determined that a population increase of x resulted in a increase of y gun deaths per each state. Though it could be argued that this is an imperfect collection of variables, and that variables such as population density within a state, or percentage of urban population within a state could be more predictive of the amount of gun deaths a state has had within the last five years these metrics were not gathered for the analysis, relying instead on the assumption that these factors would be normally distributed throughout the states, and would therefore not strongly effect the analysis.

|![Figure1-1](/figs/bgc_reg.png) |
|:--:|
| _Back Ground Checks Regression Plot_ |
|_Above: A scatterplot with a regression line drawn, expressing the relationship between state population and the amount of gun deaths in that state. Red points indicate states without background checks for firearm purchases. Green points indicate states states that require background checks for firearm purposes._|

After the regression analysis was run, the data was split into two groups: states that required background checks in order to purchase a firearm, and states that did not. States that did not require background checks were assigned as the control group, and states that did were assigned as the treatment group. An independent t-test was run on the two groups, the null Hypothesis being that background checks being required for the purchase of a firearm in a state had no effect on the amount of gun deaths in that state. The t-test results indicated a t-statistic of 2.1418, with a p-value of < .05, indicating a statistically significant difference. The null hypothesis was therefore rejected, and we can say that background check requirements in a particular state do have an effect on the amount of gun deaths that happened within that state.

|![Figure1-2](/figs/bgc_box.png) |
|:--:|
| _Back Ground Checks Regression Plot_ |
|_Above: A box plot, showing the differences in means, variances, maximums and minimums in the amount of gun deaths per capita in states that require background checks for the purchase of firearms and those that do not._|

| ![Figure1-3](/figs/strank_reg.png) |
|:--:|
| _State Rank Regression Plot_ |
|_Above: A scatterplot with a regression line drawn, expressing the relationship between state population and the amount of gun deaths in that state. Colors from cool (blue) to warm (red) indicate the Gifford's law center ranking, with blue being the highest to red being the lowest._|
