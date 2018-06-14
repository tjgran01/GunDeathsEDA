import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class GunViolenceTool(object):
    def __init__(self, gv="./data/gun_v.csv", st_pop="./data/state_pop.csv"):
        # Loading in Data
        self.gv_file = gv
        self.st_pop_file = st_pop
        self.gv = pd.read_csv(gv)
        self.st_pop = pd.read_csv(st_pop)
        # Getting quick stats
        self.deadliest = self.gv.iloc[self.gv["n_killed"].idxmax()]
        self.most_injured = self.gv.iloc[self.gv["n_injured"].idxmax()]
        self.total_killed = self.gv["n_killed"].sum()
        self.total_injured = self.gv["n_injured"].sum()
        self.total_casualties = self.total_killed + self.total_injured
