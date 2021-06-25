
import pandas as pd


mart = pd.read_csv("D:/Learnerea/Tables/supermarket_sales.csv")
mart2 = mart[['City','Quantity','Date','Unit price']].head(10)

mart2['Date']=pd.to_datetime(mart2.Date)

mart2.sort_values(by=['City','Date','Quantity'],ascending = False)

mart2.sort_index(axis=1,ascending=False)
