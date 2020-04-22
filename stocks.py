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
        

    def getStock(self, stock, interval, output_format):
        # ─── IMPORTS ─────────────────────────────────────────────────────
        from alpha_vantage.timeseries import TimeSeries
        from alpha_vantage.techindicators import TechIndicators
        #
        # ─────────────────────────────────────────────────── IMPORTS ─────
        #
        self.stock = stock
        self.interval = interval
        self.output_format = output_format
        self.ts = TimeSeries(self.key, output_format=self.output_format)
        self.data, self.meta_data = self.ts.get_intraday(symbol=stock, interval=self.interval)


    def predictStock(self, future, label_predict, split: float = None):
        # ─── VARIABLE DESCRIBTORS ────────────────────────────────────────
        # Future - Days in the future trying to predict

        # ─── IMPORTS ─────────────────────────────────────────────────────
        from sklearn.linear_model import LinearRegression
        from sklearn.svm import SVR
        from sklearn.model_selection import train_test_split
        import numpy as np


        self.future = future
        self.label_predict = label_predict
        self.split = split

        if(self.split !=None):
            return
        else:
            self.split = split

        #print(self.data.head)

        df = self.data.drop(columns=['4. close'])


        y = self.data['4. close']

        x_train, x_test, y_train, y_test = train_test_split(df, y, test_size=0.2)

        model = LinearRegression()

        model.fit(x_train, y_train)

        preds = model.predict(x_test)

        print(preds)

        #https://www.analyticsvidhya.com/blog/2018/10/predicting-stock-price-machine-learningnd-deep-learning-techniques-python/
    def visualize(self, window=None):
        # ─── IMPORTS ─────────────────────────────────────────────────────
        import matplotlib.pyplot as plt
        #
        # ─────────────────────────────────────────────────── IMPORTS ─────
        #
        self.window = window
        data_for_visuals = self.data.drop(columns=['1. open', '2. high', '3. low', '5. volume'])
        data_for_visuals.plot()
        # Moving averages
        if(self.window != None):
            short_rolling = self.data['4. close'].rolling(window).mean()
            plt.plot(short_rolling)
        
        plt.grid(True)
        plt.show()

stock = Stocks('G50K93IV0VXUFJG9')

stock.getStock('GOOGL', '1min', 'pandas')

stock.predictStock(20,'4. close')

#stock.visualize(5)

