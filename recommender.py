import pandas as pd
import numpy as np
pd.set_option("display.max_rows", None)
pd.set_option('future.no_silent_downcasting', True)
df= None
minvotes= None
class NetflixRecomennderSystem:
    def  __init__(self,dataset,genre,votesThrs,topN):
        self._dataset = dataset
        self._genre = genre
        self._votesThrs= votesThrs
        self._topN = topN
        self.df= None
        self._minvotes= None
        
    def read_file(self):
        self.df= pd.read_csv(self._dataset)
    def cleanData(self):
        self.df= self.df.drop(["year"],axis=1)
        self.df= self.df.drop(["kind"],axis=1)
        self.df= self.df.drop(["runtime"],axis=1)
        self.df= self.df.drop(["cast"],axis=1)
        self.df= self.df.drop(["director"],axis=1)
        self.df= self.df.drop(["composer"],axis=1)
        self.df= self.df.drop(["writer"],axis=1)
        self.df= self.df.drop(["Unnamed: 0"],axis=1)
        self.df=self.df.drop_duplicates(subset='title')
        self.df= self.df.fillna(0)
    def filter_genre(self):
        self.df= self.df[self.df['genre'].str.contains(self._genre, case=False,).fillna(False)] 
    def Thresh_votes(self):
        self._minvotes= np.quantile(self.df['vote'],self._votesThrs)
        self.df = self.df.drop(self.df[self.df.vote < self._minvotes].index)
    def avg_score(self):
        mean = self.df['rating'].mean()
        print(mean)
        avg=[]
        self.df = self.df.reset_index(drop=True)
        for i in range(0,len(self.df['rating'])):
            res= (self.df['vote'][i]/(self.df['vote'][i]+self._minvotes)*self.df['rating'][i])+ (self._minvotes/(self.df['vote'][i]+self._minvotes))*mean
            avg.append(res)
        self.df['Weighted Average'] = (avg)
    def sort_score(self):
        sort= self.df.sort_values('Weighted Average',ascending= False).head(self._topN)
        sort=sort.reset_index(drop=True)
        return sort 
    def run(self):
        self.read_file()
        self.cleanData()
        self.filter_genre()
        self.Thresh_votes()
        self.avg_score()
        return self.sort_score()
