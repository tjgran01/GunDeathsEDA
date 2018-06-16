import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

class GunViolenceTool(object):
    def __init__(self, gv="../data/raw/gun_v.csv",
                 st_pop="../data/raw/state_pop.csv",
                 st_abv="../data/raw/st_abv.csv",
                 gun_law_rank="../data/raw/gun_law_rank.csv"):

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

        # Getting quick stats
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

        if not os.path.exists(self.cleaned_file):
            self.deaths_w_pop = self.make_population_dataset(self.cleaned_file)
        else:
            self.deaths_w_pop = pd.read_csv(self.cleaned_file)


    def make_population_dataset(self, out_path):
        fpath = "../data/cleaned/tmp.csv"
        # make deaths df // Gotta be a cleaner way to do this.
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


    def gun_d_regplot_bgc(self, df):

        # set colors in df
        df["colors"] = np.where(df["bg_check"] == 1, "#03bc34", "#bc0303")
        df["edgecolors"] = np.where(df["bg_check"] == 1, "#017a21", "#8c0101")

        # plot
        sns.regplot(df["st_pop"], df["n_killed"], scatter_kws={'facecolors': df['colors'],
                                                               'edgecolors': df['edgecolors']})
        sns.despine()
        plt.show()


    def color_ranker(self, val):
        if val > 39:
            return ("red", "red")
        elif val > 29:
            return ("orange", "orange")
        elif val > 19:
            return ("yellow", "yellow")
        elif val > 9:
            return ("green", "green")
        else:
            return ("blue", "blue")


    def gun_d_regplot_state_rank(self, df):

        # set colors in df
        color_funct = np.vectorize(self.color_ranker)
        colors = color_funct(df["st_law_rank"])
        df["colors"] = colors[0]
        df["edgecolors"] = colors[1]

        # plot
        sns.regplot(df["st_pop"], df["n_killed"], scatter_kws={'facecolors': df['colors'],
                                                               'edgecolors': df['edgecolors']})
        plt.show()

        return df
