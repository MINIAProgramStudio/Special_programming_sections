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
            "label": 'Company',
            "options": [
                {"label": "Google", "value": "VHI"},
                {"label": "Yahoo", "value": "TCI"},
                {"label": "Apple", "value": "VCI"}],
            "key": 'ticker',
            "action_id": "update_data"}]

    controls = [{"type": "hidden", "id": "update_data"}]

    tabs = ["Plot", "Table"]

    outputs = [
        {
            "type": "plot","id" : "plot",
            "control_id" : "update_data",
            "tab" : "Plot"},
        {
            "type" : "table",
            "id" : "table_id",
            "control_id" : "update_data",
            "tab" : "Table",
            "on_page_load" : True }]


    def getData(self, params):
        return importer.dataframes['1']

    def getPlot(self, params):
        df = importer.dataframes['1']
        plt_obj = df.plot(y = params['ticker'])
        fig = plt_obj.get_figure()
        return fig

app = SimpleApp()
app.launch()
