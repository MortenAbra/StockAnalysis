class Stocks():

    def __init__(self, key, data=None, meta_data=None, ts=None):
        # ─── IMPORTS ─────────────────────────────────────────────────────


        import pandas as pd
        import numpy as np
        #
        # ─────────────────────────────────────────────────── IMPORTS ─────
        #



        super().__init__()
        self.key = key
        self.data = data
        self.meta_data = meta_data
        self.ts = ts
        

    def getStock(self, stock):
        # ─── IMPORTS ─────────────────────────────────────────────────────


        from alpha_vantage.timeseries import TimeSeries
        from alpha_vantage.techindicators import TechIndicators
        #
        # ─────────────────────────────────────────────────── IMPORTS ─────
        #



        self.stock = stock
        self.ts = TimeSeries(self.key, output_format='pandas')
        self.data, self.meta_data = self.ts.get_intraday(symbol=stock)
        print(self.data)

    def predictStock(self):
        # ─── IMPORTS ─────────────────────────────────────────────────────
        import sklearn
        #
        # ─────────────────────────────────────────────────── IMPORTS ─────
        #


    def visualize(self, window=None):
        # ─── IMPORTS ─────────────────────────────────────────────────────


        import matplotlib.pyplot as plt
        from matplotlib import style
        #
        # ─────────────────────────────────────────────────── IMPORTS ─────
        #

        

        self.window = window
        self.data.drop(columns=['1. open', '2. high', '3. low', '5. volume']).plot()


        # Moving averages
        if(self.window != None):
            short_rolling = self.data['4. close'].rolling(window).mean()
            plt.plot(short_rolling)
        
        plt.grid(True)
        plt.show()

stock = Stocks('G50K93IV0VXUFJG9')

stock.getStock('GOOGL')
stock.visualize(5)

