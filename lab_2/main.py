import downloader
from datetime import datetime
import os
import pandas as pd

def transform_regions_NOAA_to_ua(index):
    if index == 1: return 22
    elif index == 2: return 24
    elif index == 3: return 23
    elif index == 4: return 25
    elif index == 5: return 3
    elif index == 6: return 4
    elif index == 7: return 8
    elif index == 8: return 19
    elif index == 9: return 20
    elif index == 10: return 21
    elif index == 11: return 9
    elif index == 12: return 90
    elif index == 13: return 10
    elif index == 14: return 11
    elif index == 15: return 12
    elif index == 16: return 13
    elif index == 17: return 14
    elif index == 18: return 15
    elif index == 19: return 16
    elif index == 20: return 250
    elif index == 21: return 17
    elif index == 22: return 18
    elif index == 23: return 6
    elif index == 24: return 1
    elif index == 25: return 2
    elif index == 26: return 7
    elif index == 27: return 5

def download_txt_from_NOAA():
    url = "https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_TS_admin.php?provinceID=%s&country=UKR&yearlyTag=Weekly&type=Mean&TagCropland=land&year1=1982&year2=2023"
    for i in range(1,27):
        downloader.to_txt(url%(i),"downloaded_data/region%s__%s.txt"%(transform_regions_NOAA_to_ua(i), datetime.now().strftime("%Y_%m_%d__%H_%M_%S")))

def clean_directory(path):
    files = os.listdir('downloaded_data')
    for file in files:
        os.remove(path+"/"+file)

def import_txt_to_csv_from_dir(path):
    dataframes = {}
    files = os.listdir(path)
    for file in files:
        dataframes[file[7:10].replace('_','')] = pd.read_csv(path+"/"+file, skipinitialspace = True, sep=";")
    return dataframes

def get_VHI_from_df(dataframes, region_index):
    return dataframes[region_index].VHI.tolist()

print(">>>Setup complete")
#clean_directory("downloaded_data")
#print(">>>Data directory cleaned")
#download_txt_from_NOAA()
#print(">>>Data downloaded")
dataframes = import_txt_to_csv_from_dir("downloaded_data")
print(">>>Data imported")
print(get_VHI_from_df(dataframes,'1'))
print(">>>Program ended")
