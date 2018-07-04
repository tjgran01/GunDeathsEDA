###### NOTE: For a full writeup, view the `README.md` file in this directory.

## Results

### Background Checks.

The first analysis run was to determine whether or not a single policy could be enacted in order to diminish the number of gun deaths in a particular state. In order to accomplish this an Ordinary Least Squares (OLS) linear regression model was created, using state population as the predictor variable (F(1, 49) = 439.3, 0.000) with an r<sup>2</sup> of 0.900). The regression determined that a population increase of 5,000 resulted in a increase of 1 gun death per each state (over the five year period from which the data was gathered). Though it could be argued that this is an imperfect collection of variables, and that variables such as population density within a state, or percentage of urban population within a state could be more predictive of the amount of gun deaths a state has had within the last five years these metrics were not gathered for the analysis, relying instead on the assumption that these factors would be normally distributed throughout the states, and would therefore not strongly effect the analysis.

|![Figure1-1](/figs/bgc_reg.png) |
|:--:|
| _Back Ground Checks Regression Plot_ |
|_Above: A scatterplot with a regression line drawn, expressing the relationship between state population and the amount of gun deaths in that state. Red points indicate states without background checks for firearm purchases. Green points indicate states states that require background checks for firearm purposes._|

After the regression analysis was run, the data was split into two groups: states that required background checks in order to purchase a firearm, and states that did not. States that did not require background checks were assigned as the control group, and states that did were assigned as the treatment group. An independent t-test was run on the two groups, the null hypothesis being that background checks being required for the purchase of a firearm in a state had no effect on the amount of gun deaths in that state. The t-test results indicated a t-statistic of -2.1418, with a p-value of < .05, indicating a statistically significant difference. The null hypothesis was therefore rejected, and we can say that background check requirements in a particular state do have an effect on the amount of gun deaths that happened within that state. Furthermore, this significant difference indicates states with background checks have less gun deaths per capita than states that do not require them.

|![Figure1-2](/figs/bgc_box.png) |
|:--:|
| _Back Ground Checks Regression Plot_ |
|_Above: A box plot, showing the differences in means, variances, maximums and minimums in the amount of gun deaths per capita in states that require background checks for the purchase of firearms and those that do not. **It is worth pointing out that the y axis is not counting yearly deaths. These numbers were recorded over a period of five years.**_|

### State Law Ranking

The same regression plot was generated for visualizing state law rankings. The scatter plot was colored differently to indicate which states had the most restrictive ranking of gun laws, to those of which had the least restrictive. Some interesting trends came to light as a result of the visualization. It appears that the higher a state population, the less likely it is to have the least restrictive gun laws. This perhaps makes sense because per capita deaths in highly populated states are a lot larger in raw numbers than they are for their lest populated counterparts. Another point to note is that Illinois is in the top ten rank for state gun law ranks, but falls very high above it's predicted value for gun deaths based on it's state population. This is nearly the inverse of New York, which scores similarly with respect to gun law rank, but seems to fall far below it's predicted value in terms of gun deaths. This discrepancy might be worth looking into to see what other factors might play a role in reducing the amount of gun deaths.

| ![Figure1-3](/figs/strank_reg.png) |
|:--:|
| _State Rank Regression Plot_ |
|_Above: A scatterplot with a regression line drawn, expressing the relationship between state population and the amount of gun deaths in that state. Colors from cool (blue) to warm (red) indicate the Gifford's law center ranking, with blue being the highest to red being the lowest._|

After the regression analysis was run, the data was split into their five groups according to their gun policy state law ranking. An ANOVA test was run between the groups to determine if there was a statistically significant difference in per capita gun deaths. The ANOVA results indicated a F-statistic of 1.839, with a p-value of 0.1379, greater than the .05 alpha level required for statistical significance. We therefore do not reject the null hypothesis. Further evidence needs to be gathered in order to validate the rankings given to take gun laws by Giffords Law Center if they wish to justify their state rankings empirically.

| ![Figure1-3](/figs/st_rank_box.png) |
|:--:|
| _State Rank Regression Plot_ |
|_Above: A box plot, showing the differences in means, variances, maximums and minimums in the amount of gun deaths per capita in states with differing gun laws. Colors from cool (blue) to warm (red) indicate the Gifford's law center state ranking, with blue being the highest to red being the lowest._|
