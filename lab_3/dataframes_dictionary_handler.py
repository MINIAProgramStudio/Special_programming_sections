import pandas as pd


def drom_minus_one_VHI_all(dataframes):
    keys = dataframes.keys()
    new_dataframes = {}
    for k in keys:
        new_dataframes[k] = dataframes[k][dataframes[k]["VHI"] >= 0]
    return new_dataframes


def select_year(dataframes, year):
    keys = dataframes.keys()
    new_dataframes = {}
    for k in keys:
        new_dataframes[k] = dataframes[k][dataframes[k]["year"] == year]
    return new_dataframes