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
class MainWindow(QMainWindow, QFrame):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.main_window = loader.load("main_window.ui")
        
        self.main_window.show()

             
        #self.main_window.search_box.setMaxLength(10)
        self.main_window.search_box.setPlaceholderText("Which city?")

        background_pixmap = QPixmap('/media/tolo/New Volume/PyDeploy Projects/Python_for_Deployment/GUI based weather app (assignment1)/assets/background_images/wind-spring-white-stratosphere-pure.jpg')
        self.main_window.background_label.setPixmap(background_pixmap)

        icon_loc_pixmap = QPixmap('/media/tolo/New Volume/PyDeploy Projects/Python_for_Deployment/GUI based weather app (assignment1)/assets/location_icon/loc2.png')
        self.main_window.icon_location.setPixmap(icon_loc_pixmap)

        self.main_window.btn_search.clicked.connect(self.search_weather)

        
    def weather_image(self,weather_des):

            if weather_des == "Mix snow/rain":
                img_path = "/media/tolo/New Volume/PyDeploy Projects/Python_for_Deployment/GUI based weather app (assignment1)/assets/weather icons/flat_black/05.png"
            elif weather_des == "Broken clouds":
                img_path = "/media/tolo/New Volume/PyDeploy Projects/Python_for_Deployment/GUI based weather app (assignment1)/assets/weather icons/flat_black/30.png"
            elif weather_des == "Overcast clouds":
                img_path = "/media/tolo/New Volume/PyDeploy Projects/Python_for_Deployment/GUI based weather app (assignment1)/assets/weather icons/flat_black/26.png"
            elif weather_des == "Moderate rain":
                img_path = "/media/tolo/New Volume/PyDeploy Projects/Python_for_Deployment/GUI based weather app (assignment1)/assets/weather icons/flat_black/12.png"
            elif weather_des == "Light rain":
                img_path = "/media/tolo/New Volume/PyDeploy Projects/Python_for_Deployment/GUI based weather app (assignment1)/assets/weather icons/flat_black/09.png"
            elif weather_des == "Light shower rain":
                img_path = "/media/tolo/New Volume/PyDeploy Projects/Python_for_Deployment/GUI based weather app (assignment1)/assets/weather icons/flat_black/02.png"
            elif weather_des == "Few clouds":
                img_path = "/media/tolo/New Volume/PyDeploy Projects/Python_for_Deployment/GUI based weather app (assignment1)/assets/weather icons/flat_black/30.png"
            elif weather_des == "Scattered clouds":
                img_path = "/media/tolo/New Volume/PyDeploy Projects/Python_for_Deployment/GUI based weather app (assignment1)/assets/weather icons/flat_black/28.png"
            elif weather_des == "Clear Sky":
                img_path = "/media/tolo/New Volume/PyDeploy Projects/Python_for_Deployment/GUI based weather app (assignment1)/assets/weather icons/flat_black/32.png"
            elif weather_des == "Thunderstorm with rain":
                img_path = "/media/tolo/New Volume/PyDeploy Projects/Python_for_Deployment/GUI based weather app (assignment1)/assets/weather icons/flat_black/00.png"
            elif weather_des == "Thunderstorm with heavy rain":
                img_path = "/media/tolo/New Volume/PyDeploy Projects/Python_for_Deployment/GUI based weather app (assignment1)/assets/weather icons/flat_black/00.png"
            elif weather_des == "Light snow":
                img_path = "/media/tolo/New Volume/PyDeploy Projects/Python_for_Deployment/GUI based weather app (assignment1)/assets/weather icons/flat_black/13.png"
            elif weather_des == "Heavy snow":
                img_path = "/media/tolo/New Volume/PyDeploy Projects/Python_for_Deployment/GUI based weather app (assignment1)/assets/weather icons/flat_black/16.png"

            elif weather_des == "Heavy rain":
                img_path = "/media/tolo/New Volume/PyDeploy Projects/Python_for_Deployment/GUI based weather app (assignment1)/assets/weather icons/flat_black/01.png"

            elif weather_des == "Snow":
                img_path = "/media/tolo/New Volume/PyDeploy Projects/Python_for_Deployment/GUI based weather app (assignment1)/assets/weather icons/flat_black/14.png"

            elif weather_des == "Flurries":
                img_path = "/media/tolo/New Volume/PyDeploy Projects/Python_for_Deployment/GUI based weather app (assignment1)/assets/weather icons/flat_black/15.png"

            else:
                img_path = "/media/tolo/New Volume/PyDeploy Projects/Python_for_Deployment/GUI based weather app (assignment1)/assets/weather icons/flat_black/44.png" 

            return img_path
    
    def search_weather(self):

        city_name = self.main_window.search_box.text()
        
        url = f"https://api.weatherbit.io/v2.0/forecast/daily?&city={city_name}&key=2effe1f9f06e40cc8ef77eb5be376022"
        response = requests.get(url)
        self.main_window.city_label.setText(city_name)
        #response = requests.get(f"https://goweather.herokuapp.com/weather/{city_name}")
        #print(response.status_code)
        
        if response.status_code == 200:
            json_data = json.loads(response.text)

            # **********TODAY**********
            today_dict = json_data["data"][0]
            # 1.today time
            
            today_date = today_dict["datetime"]
            today_date = datetime.strptime(today_date, '%Y-%m-%d')
            today_str_date = datetime.strftime(today_date, '%A %d %B')
            self.main_window.txt_today.setText("Today")

            # 2.today weather description
            today_weather = today_dict["weather"]["description"]
            self.main_window.now_des.setText(str(today_weather))

            # 3.today wind speed
            today_wind = today_dict["wind_spd"]
            self.main_window.wind_speed.setText(str(today_wind)  + "km/h")

            # 4.today temperature
            today_temp = today_dict["temp"]
            self.main_window.temp_today.setText(str(today_temp) + "°C")
            
            image_path = self.weather_image(today_weather)

            icon_weather_pixmap_today= QPixmap(image_path)
            self.main_window.icon_now_des.setPixmap(icon_weather_pixmap_today)


            # **********TOMORROW**********
            tomorrow_dict = json_data["data"][1]
            # 1.tomorrow time
            
            tomorrow_date = tomorrow_dict["datetime"]
            tomorrow_date = datetime.strptime(tomorrow_date, '%Y-%m-%d')
            today_str_date = datetime.strftime(tomorrow_date, '%A %d %B')
            self.main_window.txt_tomo.setText("Tomorrow")

            # 2.tomorrow weather description
            tomorrow_weather = tomorrow_dict["weather"]["description"]
            self.main_window.now_des.setText(str(tomorrow_weather))

            # 3.tomorrow wind speed
            #tomorrow_wind = today_dict["wind_spd"]
            #self.main_window.wind_speed.setText(str(tomorrow_wind)  + "km/h")

            # 4.tomorrow temperature
            tomorrow_temp = tomorrow_dict["temp"]
            self.main_window.temp_tomo.setText(str(tomorrow_temp) + "°C")
            
            image_path = self.weather_image(tomorrow_weather)

            icon_weather_pixmap_tomorrow= QPixmap(image_path)
            self.main_window.icon_tomo.setPixmap(icon_weather_pixmap_tomorrow)

        else:
            print("*** API onnection problem ***")

        


        

        # date_time = json_data["data"][0]["datetime"]
        # normal_date = datetime.strptime(date_time, '%Y-%m-%d')
        # date = normal_date.strftime('%A, %d %B')
        # description_weather = json_data["data"][0]["weather"]["description"]
        # wind_speed = json_data["data"][0]["wind_spd"]
        # today_temp = json_data["data"][0]["temp"]

        




    

        
        


app = QApplication(sys.argv)
main_window = MainWindow()
app.exec()