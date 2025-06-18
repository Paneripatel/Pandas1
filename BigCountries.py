'''
2 Problem 2 :Big Countries ( https://leetcode.com/problems/big-countries/ )
'''

import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    world = world[(world['population']>=25000000) | (world['area']>=3000000)]
    return world[['name', 'population', 'area']]