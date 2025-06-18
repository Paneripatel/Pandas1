'''Pandas1

1 Problem 1 : Make a Pandas DataFrame with two-dimensional list ( https://www.geeksforgeeks.org/make-a-pandas-dataframe-with-two-dimensional-list-python/)
'''

import pandas as pd

lst = [['Geek', 25], ['is', 30], 
       ['for', 26], ['Geeksforgeeks', 22]] 
 
df = pd.DataFrame(lst, columns =['Tag', 'number']) 

print(df)