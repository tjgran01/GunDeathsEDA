import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from scipy import stats
import statsmodels.api as sm
import palette_dicts

class GunViolenceTool(object):
    """A class used to explore the gun violence data set.
        Args:
            gv(str): Filepath to gun violence dataset.
            st_pop(str): Filepath to state population dataset.
            st_abv(str): Filepath to state abbreviations dataset.
            gun_law_rank(str): Filepath to state gun law dataset.
        Return:
            None"""
    def __init__(self, gv="../data/raw/gun_v.csv",
                 st_pop="../data/raw/state_pop.csv",
                 st_abv="../data/raw/st_abv.csv",
                 gun_law_rank="../data/raw/gun_law_rank.csv"):

        self.palette = palette_dicts.soft_colors
        self.box_pal = palette_dicts.box_plot_colors
        self.box_pal_5 = palette_dicts.box_plot_colors_5

        # Loading in files
        self.cleaned_file = "../data/cleaned/gun_d_with_pop.csv"
        self.gv_file = gv
        self.st_pop_file = st_pop
        self.st_abv_file = st_abv
        self.gun_law_rank_file = gun_law_rank

        # Creating DataFrames
        self.gv = pd.read_csv(gv)
        self.st_pop = pd.read_csv(st_pop, names=["abbv", "st_pop"])
        self.st_abv = pd.read_csv(st_abv, names=["state", "abbv"])
        self.gun_law_rank = pd.read_csv(gun_law_rank,
                                        names=["st_law_rank", "state",
                                               "st_letter_rank",
                                               "gun_death_rate_rank",
                                               "bg_check"])

        # Getting quick info
        self.deadliest = self.gv.iloc[self.gv["n_killed"].idxmax()]
        self.most_injured = self.gv.iloc[self.gv["n_injured"].idxmax()]
        self.total_killed = self.gv["n_killed"].sum()
        self.total_injured = self.gv["n_injured"].sum()
        self.total_casualties = self.total_killed + self.total_injured

        # Grouping By State
        self.st_incidents = self.gv.groupby("state").size().sort_values(
                            ascending=False)
        self.st_total_killed = self.gv.groupby("state")["n_killed"].sum().sort_values(ascending=False)
        self.st_total_injured = self.gv.groupby("state")["n_injured"].sum().sort_values(ascending=False)

        # Creating or loading cleaned datafile for modeling / plotting
        if not os.path.exists(self.cleaned_file):
            self.deaths_w_pop = self.make_population_dataset(self.cleaned_file)
        else:
            self.deaths_w_pop = pd.read_csv(self.cleaned_file)

# Data Cleaning Methods --------------------------------------------------------

    def make_population_dataset(self, out_path):
        """Creates a dataset that tallys to the amount of gun deaths per state,
        and combines that information with state population and current gun law
        infomration.
        Args:
            out_path(str): File path where the dataset will be stored.
        Returns:
            df(DataFrame): A pandas DataFrame that combines gun deaths and state
            information."""

        fpath = "../data/cleaned/tmp.csv"

        # make deaths df // Gotta be a cleaner way to do this.
        # reset_index() method
        df = pd.DataFrame(self.st_total_killed, columns=["n_killed"], index=None)
        df.to_csv(fpath)
        df = pd.read_csv(fpath)

        os.remove(fpath)
        # merge state abbv to df
        df = pd.merge(df, self.st_abv[["abbv", "state"]], on="state")
        # merge population to df
        df = pd.merge(df, self.st_pop[["abbv", "st_pop"]], on="abbv")
        # merge gun law_rank to df
        df = pd.merge(df,
                      self.gun_law_rank[["st_law_rank", "state",
                                             "st_letter_rank",
                                             "gun_death_rate_rank",
                                             "bg_check"]],
                      on="state")
        df.to_csv(out_path, index=False)
        return df

# Stats Methods ----------------------------------------------------------------

    def bgc_t_test(self, df):
        """Performs a t_test on states that have a background check and states
        that do not.
        Args:
            df(DataFrame): The cleaned state gun deaths DataFrame.
        Returns:
            df(DataFrame): The cleaned state gun deaths DataFrame. With
            'd_per_capita' col included."""

        df["d_per_capita"] = df["n_killed"] / df["st_pop"]
        df["Gun Deaths Per 10000 Residents"] = df["d_per_capita"] * 10000
        df_bgc = df.loc[df["bg_check"] == 1]
        df_no_bgc = df.loc[df["bg_check"] == 0]

        t_stat, p_val = stats.ttest_ind(df_no_bgc["d_per_capita"],
                                        df_bgc["d_per_capita"])
        print(f"T-Stat: {t_stat}")
        print(f"P Value: {p_val}")
        return(df)


    def state_rank_anova(self, df):
        """Performs an ANOVA test on states that have different gun law
        rankings.
        Args:
            df(DataFrame): The cleaned state gun deaths DataFrame.
        Returns:
            df(DataFrame): The cleaned state gun deaths DataFrame. With
            'd_per_capita' col included."""

        df["d_per_capita"] = df["n_killed"] / df["st_pop"]
        df["Gun Deaths Per 10000 Residents"] = df["d_per_capita"] * 10000
        df = self.set_state_rank_colors(df)
        groups = df.groupby("rank_group")
        rank_groups = [data[1]["d_per_capita"] for data in groups]
        print(rank_groups)
        F, p = stats.f_oneway(rank_groups[0], rank_groups[1], rank_groups[2],
                              rank_groups[3], rank_groups[4])
        print(f"F Stat: {F}")
        print(f"p value: {p}")

# Modeling Methods -------------------------------------------------------------

    def death_pop_reg(self):
        """Creates a liner regression model with number of people killed by guns
        in a state being predicted by it's state population.
        Args:
            None
        Returns:
            model.summary(DataFrame): A DataFrame that provides information about
            the regression model."""

        model = sm.OLS(self.deaths_w_pop["n_killed"],
                       self.deaths_w_pop["st_pop"]).fit()

        predictions = model.predict(self.deaths_w_pop["st_pop"])
        print(predictions)
        print(predictions.params)
        return model.summary()


# Plotting Helper Methods ------------------------------------------------------

    def add_text_to_points(self, ax, df):
        """Plots the state abbreviations next to their scatter points.
        Args:
            ax(ax object): The current plt.ax being drawn to.
            df: The cleaned state gun deaths DataFrame.
        Returns:
            ax: The ax, with the text values plotted next to their scatter
            point."""
        for x, y, state in zip(df["st_pop"], df["n_killed"], df["abbv"]):
            sts_of_interest = ["NY", "CA", "TX", "FL", "IL", "PA", "OH"]
            if state in sts_of_interest:
                ax.text(x - 10000, y + 100, state, color=self.palette["black"],
                        fontsize="8")
        return ax


    def color_ranker(self, val):
        """Returns a color value, and a rank string to be placed in the current
        DataFrame, to properly color and label the different state gun laws in
        the regplot.
        Args:
            val(int): The state's gun law rank.
        Returns:
            tuple: The color(hex), edgecolor(hex), rank_group(str) for each
            state."""
        if val > 39:
            return (self.palette["red"], self.palette["red"], "Ranked 41-50")
        elif val > 29:
            return (self.palette["orange"], self.palette["orange"], "Ranked 11-20")
        elif val > 19:
            return (self.palette["yellow"], self.palette["yellow"], "Ranked 21-30")
        elif val > 9:
            return (self.palette["green"], self.palette["green"], "Ranked 31-40")
        else:
            return (self.palette["blue"], self.palette["blue"], "Ranked 1-10")


    def make_color_rank_set(self, df):
        """Creates a set of color and value pairs to be used when creating a
        plot's legend.
        Args:
            df(DataFrame): The cleaned state gun deaths DataFrame.
        Returns:
            set: a set of (color, rank) tuples."""

        colors = df["colors"].tolist()
        ranks = df["rank_group"].tolist()
        return set(list(zip(colors, ranks)))


    def create_legend(self, ax, colors):
        """Creates a custom legend corresponding the the color coding of the
        scatter plots.
        Args:
            ax(ax object): The current plt.ax being drawn to.
            colors(set):  set of (color, rank) tuples.
        Returns:
            ax(ax object): The current plt.ax being drawn to with the legend
            drawn"""

        leg_elms = [Line2D([0], [0], marker='o', color=color, label=label,
                           markerfacecolor=color, markersize=5) for color, label in colors]
        if len(leg_elms) == 5:
            ax.legend(handles=leg_elms, title="State Gun Law Ranks")
        else:
            ax.legend(handles=leg_elms, title="Background Checks")
        return ax


    def set_bgc_colors(self, df):
        """Sets the colors for the points in back ground check regplots.
        Args:
            df(DataFrame): The cleaned state gun deaths DataFrame.
        Returns:
            df(DataFrame): df with new cols for colors, edgecolors, and
            rank_group."""

        df["colors"] = np.where(df["bg_check"] == 1, self.palette["green"],
                                self.palette["red"])
        df["edgecolors"] = np.where(df["bg_check"] == 1, self.palette["green"],
                                    self.palette["red"])
        df["rank_group"] = np.where(df["bg_check"] == 1, "Yes", "No")
        return df


    def set_state_rank_colors(self, df):
        """Sets the colors for the points in state rank regplots.
        Args:
            df(DataFrame): The cleaned state gun deaths DataFrame.
        Returns:
            df(DataFrame): df with new cols for colors, edgecolors, and
            rank_group."""

        color_funct = np.vectorize(self.color_ranker)
        colors = color_funct(df["st_law_rank"])
        df["colors"] = colors[0]
        df["edgecolors"] = colors[1]
        df["rank_group"] = colors[2]
        return df


    def set_plot_titles(self, plt, df):
        """Adds final touches to the generated plot, such as gridlines, tiles,
        and axis labels.
        Args:
            plt(plt object): The plot to be displayed the the user.
            df(DataFrame): The cleaned state gun deaths DataFrame."""
        # Adjust Axes
        sns.despine()
        plt.xlim([0, df["st_pop"].max() + 1000000])
        plt.ylim([0, 6000])
        plt.grid(color=self.palette["white"], zorder=0)
        plt.title("Gun Deaths vs. State Population.")
        plt.xlabel("State Population (In Millions)")
        plt.ylabel("Gun Deaths")
        return plt

# Plotting Methods -------------------------------------------------------------

    def gun_d_regplot_bgc(self, df):
        """Plots a regression plot of every states amount of gun deaths v. their
        state population. Color's scatter based on whether or not the state
        requires background checks to purchase a firearm.
        Args:
            df(DataFrame): The cleaned state gun deaths DataFrame.
        Returns:
            None: Currently displays the plot to user's screen."""
        df = self.set_bgc_colors(df)
        ax = sns.regplot(df["st_pop"], df["n_killed"], label="BG Checks",
                         scatter_kws={'facecolors': df['colors'],
                                      'edgecolors': df['edgecolors'],
                                      's': 20},
                         line_kws={'color': self.palette["d_grey"]})
        ax = self.add_text_to_points(ax, df)
        ax.set_facecolor(self.palette["back_grey"])

        color_rank_set = self.make_color_rank_set(df)
        ax = self.create_legend(ax, color_rank_set)
        out_plt = self.set_plot_titles(plt, df)
        out_plt.savefig('../figs/bgc_reg.png', format="png", dpi=600)
        out_plt.show()


    def gun_d_regplot_state_rank(self, df):
        """Plots a regression plot of every states amount of gun deaths v. their
        state population. Color's scatter plot by state's gun law rank.
        Args:
            df(DataFrame): The cleaned state gun deaths DataFrame.
        Returns:
            None: Currently displays the plot to users screen."""
        df = self.set_state_rank_colors(df)
        ax = sns.regplot(df["st_pop"], df["n_killed"],
                         scatter_kws={'facecolors': df['colors'],
                                      'edgecolors': df['edgecolors'],
                                      's': 35},
                         line_kws={'color': self.palette["d_grey"]})
        ax = self.add_text_to_points(ax, df)
        ax.set_facecolor(self.palette["back_grey"])

        color_rank_set = self.make_color_rank_set(df)
        ax = self.create_legend(ax, color_rank_set)
        out_plt = self.set_plot_titles(plt, df)
        out_plt.savefig('../figs/strank_reg.png', format="png", dpi=600)
        out_plt.show()


    def bgc_box_plot(self, df):
        """Generates a boxplot comparing gun deaths per capita between states
        that require a background check and states that do not.
        Args:
            df(DataFrame):  The cleaned state gun deaths DataFrame.
        Returns:
            None (shows and saves the plot.)"""

        df = self.set_bgc_colors(df)
        df = self.bgc_t_test(df)
        df["bgc_text"] = np.where(df["bg_check"] == 1, "Yes", "No")
        ax = sns.boxplot(df["bgc_text"], df["Gun Deaths Per 10000 Residents"],
                         data=df, palette=self.box_pal)
        ax.set_facecolor(self.palette["back_grey"])
        sns.despine()
        plt.title("Gun Deaths Per Capita - Background Checks")
        plt.xlabel("Background Checks Required")
        plt.ylabel("Gun Deaths Per 10,000 Residents")
        plt.savefig('../figs/bgc_box.png', format="png", dpi=600)
        plt.show()


    def state_rank_box_plot(self, df):
        """Generates a boxplot comparing gun deaths per capita between states
        that have different Gifford's Law Center gun law rankings.
        Args:
            df(DataFrame):  The cleaned state gun deaths DataFrame.
        Returns:
            None (shows and saves the plot.)"""
        df = self.set_state_rank_colors(df)
        df = self.bgc_t_test(df)
        ax = sns.boxplot(df["rank_group"], df["Gun Deaths Per 10000 Residents"],
                         data=df, palette=self.box_pal_5)
        ax.set_facecolor(self.palette["back_grey"])
        sns.despine()
        plt.title("Gun Deaths Per Capita - State Rank")
        plt.xlabel("State Gun Law Rank")
        plt.ylabel("Gun Deaths Per 10,000 Residents")
        plt.savefig('../figs/st_rank_box.png', format="png", dpi=600)
        plt.show()
