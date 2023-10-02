import requests
import os
import pandas as pd

def to_txt(url,save_path):
    raw_data = requests.get(url)  # get data
    raw_data_file = open(save_path,"wb")
    raw_data_file.write(raw_data.content)
    raw_data_file.close()

    raw_data_file = open(save_path)
    text_with_commas = raw_data_file.read()
    raw_data_file.close()

    first_enter = text_with_commas.find('\n')  # delete first line step 1
    text_with_commas = text_with_commas[first_enter + 1:]  # delete first line step 2

    arrow_right_pos = text_with_commas.find('<')
    arrow_left_pos = text_with_commas.find('>')
    while not arrow_right_pos + arrow_left_pos <= -1:
        text_with_commas = text_with_commas[0:arrow_right_pos] + text_with_commas[arrow_left_pos + 1:]  # deleting html
        arrow_right_pos = text_with_commas.find('<')
        arrow_left_pos = text_with_commas.find('>')

    text_clean = text_with_commas.replace(',\n', '\n')  # delete commas at the end of the lines
    text_clean = text_clean.replace(',', ';')  # replace comas with ;

    file_clean = open(save_path, 'w')  # open text file for data
    file_clean.write(text_clean)  # save data
    file_clean.close()  # close file

def to_csv(url,save_path):
    to_txt(url, 'temporary_downloader_file_for_url_handling.txt')
    vhi_csv = pd.read_csv('temporary_downloader_file_for_url_handling.txt')
    vhi_csv.to_csv(save_path, index=False)
    os.remove('temporary_downloader_file_for_url_handling.txt')