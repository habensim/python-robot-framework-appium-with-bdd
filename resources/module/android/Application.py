import sys
import os
from time import sleep
current_directory = os.getcwd()
sys.path.append(current_directory)
from utils.Settings import driver


class Application:
    def run_apk(self):
        driver.launch_app()
        sleep(3)
                       
    

    