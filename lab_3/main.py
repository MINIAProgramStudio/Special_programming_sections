from spyre import server
import matplotlib.pyplot as plt
import pandas as pd
import urllib3
import json


import importer

importer.begin()

class Options:
    columns_plot = [
        {
            "label": "SMN", "value":"SMN",
        },
        {
            "label": "SMT", "value":"SMT",
        },
        {
            "label": "VCI", "value":"VCI",
        },
        {
            "label": "TCI", "value":"TCI",
        },
        {
            "label": "VHI", "value":"VHI",
        },
    ]

class SimpleApp(server.App):
    title = "Historical Stock Prices"
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
            "label": 'Область',
            "options": [
                {"label": "Вінницька", "value": "1"},
                {"label": "Волинська", "value": "2"},
                {"label": "Дніпропетровська", "value": "3"}],
            "key": 'selected_region',
            "action_id": "update_data"}
    ]

    controls = [{"type": "hidden", "id": "update_data"}]

    tabs = ["Plot"]

    outputs = [
        {
            "type": "plot","id" : "plot",
            "control_id" : "update_data",
            "tab" : "Plot"}]


    def getData(self, params):
        return importer.dataframes['1']

    def getPlot(self, params):
        df = importer.dataframes[params['selected_region']]
        plt_obj = df.plot(y = params['plot_value'])
        fig = plt_obj.get_figure()
        return fig

app = SimpleApp()
app.launch()
