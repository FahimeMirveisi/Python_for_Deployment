import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QApplication
import requests
import json
from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QPixmap, QIcon
from datetime import datetime


# create main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.main_window = loader.load("main_window.ui")
        
        self.main_window.show()

             
        #self.main_window.search_box.setMaxLength(10)
        self.main_window.search_box.setPlaceholderText("Which city?")

        background_pixmap = QPixmap('/media/tolo/New Volume1/PyDeploy Projects/Python_for_Deployment/GUI based weather app (assignment1)/assets/background_images/wind-spring-white-stratosphere-pure.jpg')
        self.main_window.background_label.setPixmap(background_pixmap)

        icon_loc_pixmap = QPixmap('/media/tolo/New Volume1/PyDeploy Projects/Python_for_Deployment/GUI based weather app (assignment1)/assets/location_icon/loc2.png')
        self.main_window.icon_location.setPixmap(icon_loc_pixmap)

        self.main_window.btn_search.clicked.connect(self.search_weather)

        

        


    def search_weather(self):

        city_name = self.main_window.search_box.text()
        
        url = f"https://api.weatherbit.io/v2.0/forecast/daily?&city={city_name}&key=2effe1f9f06e40cc8ef77eb5be376022"
        response = requests.get(url)
        #response = requests.get(f"https://goweather.herokuapp.com/weather/{city_name}")
        #print(response.status_code)
        
        if response.status_code == 200:
            json_data = json.loads(response.text)
            #print(json_data)
            print(json_data["city_name"])

        else:
            print("*** connection problem ***")


        # date_time = json_data["data"][0]["datetime"]
        # normal_date = datetime.strptime(date_time, '%Y-%m-%d')
        # date = normal_date.strftime('%A, %d %B')
        # description_weather = json_data["data"][0]["weather"]["description"]
        # wind_speed = json_data["data"][0]["wind_spd"]
        # today_temp = json_data["data"][0]["temp"]

        




    

        
        


app = QApplication(sys.argv)
main_window = MainWindow()
app.exec()