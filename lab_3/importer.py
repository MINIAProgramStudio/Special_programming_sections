import downloader
from datetime import datetime
import os
import pandas as pd


def remove_items(test_list, item):
    # using list comprehension to perform the task
    res = [i for i in test_list if i != item]
    return res


def transform_regions_NOAA_to_ua(index):
    if index == 1:
        return 22
    elif index == 2:
        return 24
    elif index == 3:
        return 23
    elif index == 4:
        return 25
    elif index == 5:
        return 3
    elif index == 6:
        return 4
    elif index == 7:
        return 8
    elif index == 8:
        return 19
    elif index == 9:
        return 20
    elif index == 10:
        return 21
    elif index == 11:
        return 9
    elif index == 12:
        return 90
    elif index == 13:
        return 10
    elif index == 14:
        return 11
    elif index == 15:
        return 12
    elif index == 16:
        return 13
    elif index == 17:
        return 14
    elif index == 18:
        return 15
    elif index == 19:
        return 16
    elif index == 20:
        return 250
    elif index == 21:
        return 17
    elif index == 22:
        return 18
    elif index == 23:
        return 6
    elif index == 24:
        return 1
    elif index == 25:
        return 2
    elif index == 26:
        return 7
    elif index == 27:
        return 5


def download_txt_from_NOAA(log=False):
    url = "https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_TS_admin.php?provinceID=%s&country=UKR&yearlyTag=Weekly\
    &type=Mean&TagCropland=land&year1=1982&year2=2023"
    for i in range(1, 28):
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
    return dataframes


def get_region_VHI(dataframes, region_index):
    return dataframes[region_index].VHI.tolist()


def get_year_VHI(dataframes, region_index, year):
    VHI_list = get_region_VHI(dataframes, region_index)
    starting_year = int(dataframes[region_index].year.tolist()[0])
    return VHI_list[(year - starting_year) * 52:(year - starting_year + 1) * 52]


def week_index_to_year_week(dataframes, week_index):
    starting_year = int(dataframes['1'].year.tolist()[0])
    year = starting_year + int(week_index / 52)
    week = week_index % 52
    return [year, week]


def find_max_index(in_list):
    return in_list.index(max(in_list))


def find_min_index(in_list):
    return in_list.index(min(in_list))


def extreme_drought_area(dataframes, region_index, area_percentage):
    df = dataframes[region_index]
    percents_list = df.SMN.tolist()
    VHI_list = get_region_VHI(dataframes, region_index)
    i = 0
    output = []
    while i < len(VHI_list):
        if VHI_list[i] >= 0 and VHI_list[i] < 15 and percents_list[i] > area_percentage / 100:
            year = week_index_to_year_week(dataframes, i)[0]
            if not year in output:
                output.append(year)
        i += 1
    return output


def moderate_drought_area(dataframes, region_index, area_percentage):
    df = dataframes[region_index]
    percents_list = df.SMN.tolist()
    VHI_list = get_region_VHI(dataframes, region_index)
    i = 0
    output = []
    while i < len(VHI_list):
        if VHI_list[i] >= 0 and VHI_list[i] < 35 and percents_list[i] > area_percentage / 100:
            year = week_index_to_year_week(dataframes, i)[0]
            if not year in output:
                output.append(year)
        i += 1
    return output


dataframes = {}


def begin(data_update = False):
    global dataframes
    if data_update or not os.path.exists("Downloaded_data"):
        if not os.path.exists("Downloaded_data"):
            os.makedirs("Downloaded_data")
        clean_directory("Downloaded_data")
        download_txt_from_NOAA()
    dataframes = import_txt_to_csv_from_dir("downloaded_data")
    dataframes['1'].to_csv('1.csv', sep=';')