import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
import requests
import json
from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QPixmap, QIcon
from datetime import datetime


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.main_window = loader.load("main_window.ui")
        self.main_window.show()

        
        self.main_window.search_box.setMaxLength(10)
        self.main_window.search_box.setPlaceholderText("Which city?")

        

        self.main_window.btn_search.clicked.connect(self.search_weather)

        

        


    def search_weather(self):

        city_name = self.main_window.search_box.text()
        response = requests.get(f"https://goweather.herokuapp.com/weather/{city_name}")
        #print(response.status_code)
        json_data = json.loads(response.text)
        date_time = json_data["data"][0]["datetime"]
        normal_date = datetime.strptime(date_time, '%Y-%m-%d')
        date = normal_date.strftime('%A, %d %B')
        description_weather = json_data["data"][0]["weather"]["description"]
        wind_speed = json_data["data"][0]["wind_spd"]
        today_temp = json_data["data"][0]["temp"]

        




    

        
        


app = QApplication(sys.argv)
main_window = MainWindow()
app.exec()