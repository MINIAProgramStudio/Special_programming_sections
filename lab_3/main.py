from spyre import server
import matplotlib.pyplot as plt
import pandas as pd
import urllib3
import json


import importer

importer.begin()

def select_years_from_str(dataframe, selection):
    try:
        year0 = int(selection[0:selection.find("-")])
        year1 = int(selection[selection.find("-")+1:])+1
        return dataframe.loc[dataframe['year'].isin(range(year0,year1))]
    except:
        Exception("Invaild year selection")
        print("Invaild year selection")
        return dataframe

def select_weeks_from_str(dataframe, selection):
    try:
        week0 = int(selection[0:selection.find("-")])
        week1 = int(selection[selection.find("-")+1:])+1
        print(str(range(week0,week1)))
        return dataframe.loc[dataframe['week'].isin(range(week0,week1))]
    except:
        Exception("Invaild week selection")
        print("Invaild week selection")
        return dataframe


class SimpleApp(server.App):
    title = "NOAA visualization"
    inputs = [
        {
            "type": 'dropdown',
            "label": 'Обрана колонка графіку',
            "options": [
                {"label": "VCI", "value": "VCI"},
                {"label": "TCI", "value": "TCI"},
                {"label": "VHI", "value": "VHI"}],
            "key": 'plot_value',
            "action_id": "update_data"},
        {
            "type": 'dropdown',
            "label": 'Адміністративна одиниця',
            "options": [
                {"label": "Вінницька", "value": "1"},
                {"label": "Волинська", "value": "2"},
                {"label": "Дніпропетровська", "value": "3"},
                {"label": "Донецька", "value": "4"},
                {"label": "Житомирська", "value": "5"},
                {"label": "Закарпатська", "value": "6"},
                {"label": "Запорізька", "value": "7"},
                {"label": "Івано-Франківська", "value": "8"},
                {"label": "Київська область", "value": "9"},
                {"label": "Місто Київ", "value": "90"},
                {"label": "Кіровоградська", "value": "10"},
                {"label": "Луганська", "value": "11"},
                {"label": "Львівська", "value": "12"},
                {"label": "Миколаївська", "value": "13"},
                {"label": "Одеська", "value": "14"},
                {"label": "Полтавська", "value": "15"},
                {"label": "Рівенська", "value": "16"},
                {"label": "Сумська", "value": "17"},
                {"label": "Тернопільська", "value": "18"},
                {"label": "Харківська", "value": "19"},
                {"label": "Херсонська", "value": "20"},
                {"label": "Хмельницька", "value": "21"},
                {"label": "Черкаська", "value": "22"},
                {"label": "Чернівецька", "value": "23"},
                {"label": "Чернігівська", "value": "24"},
                {"label": "АР Крим", "value": "25"},
                {"label": "Севастополь", "value": "250"},
            ],
            "key": 'selected_region',
            "action_id": "update_data"},
        {
            "type": 'text',
            "label": 'Оберіть тижні',
            "value": "1-52",
            "key": 'selected_weeks',
            "action_id": "update_data"
        },
        {
            "type": 'text',
            "label": 'Оберіть роки',
            "value": "1982-2023",
            "key": 'selected_years',
            "action_id": "update_data"
        }
    ]

    controls = [{"type": "hidden", "id": "update_data"}]

    tabs = ["Plot", "Table"]

    outputs = [
        {
            "type": "plot","id" : "plot",
            "control_id" : "update_data",
            "tab" : "Plot"},
        {"type": "table",
         "id": "table_id",
         "control_id": "update_data",
         "tab": "Table",
         "on_page_load": True}
    ]


    def getData(self, params):
        df = importer.dataframes[params['selected_region']]
        df = select_weeks_from_str(select_years_from_str(df, params['selected_years']),  params['selected_weeks'])
        return df


    def getPlot(self, params):
        df = importer.dataframes[params['selected_region']]
        df = select_weeks_from_str(select_years_from_str(df, params['selected_years']),  params['selected_weeks'])
        plt_obj = df.plot(y = params['plot_value'])
        fig = plt_obj.get_figure()
        return fig

app = SimpleApp()
app.launch()
