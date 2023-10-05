import downloader
import dataframes_dictionary_handler as ddh
from datetime import datetime
import os
import pandas as pd


def remove_items(test_list, item):
    # using list comprehension to perform the task
    res = [i for i in test_list if i != item]
    return res


def transform_regions_NOAA_to_ua(index):
    return [22,24,23,25,3,4,8,19,20,21,9,90,10,11,12,13,14,15,16,250,17,18,6,1,2,7,5][index]



def download_txt_from_NOAA(log=False):
    url = "https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_TS_admin.php?provinceID=%s&country=UKR&yearlyTag=Weekly&type=Mean&TagCropland=land&year1=1982&year2=2023"
    for i in range(0, 27):
        downloader.to_txt(url % (i), "downloaded_data/region%s__%s.txt" % (transform_regions_NOAA_to_ua(i),
                                                                           datetime.now().strftime(
                                                                               "%Y_%m_%d__%H_%M_%S")))
        if log:
            print(">>>downloaded file %s/27" % i)


def clean_directory(path):
    files = os.listdir('downloaded_data')
    for file in files:
        os.remove(path + "/" + file)


def import_txt_to_csv_from_dir(path):
    dataframes = {}
    files = os.listdir(path)
    for file in files:
        dataframes[file[6:9].replace('_', '')] = pd.read_csv(path + "/" + file, skipinitialspace=True, sep=";")
    dataframes = ddh.drom_minus_one_VHI_all(dataframes)
    return dataframes


dataframes = {}


def begin(forced_data_download = False):
    global dataframes
    if forced_data_download or not os.path.exists("Downloaded_data"):
        if not os.path.exists("Downloaded_data"):
            os.makedirs("Downloaded_data")
        clean_directory("Downloaded_data")
        download_txt_from_NOAA()
    dataframes = import_txt_to_csv_from_dir("Downloaded_data")