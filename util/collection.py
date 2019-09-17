#   --------------------------------------------------------------------------   #
#   -                          Imports de uso Geral                          -   #
#   --------------------------------------------------------------------------   #
import os
import os.path
import re
import sys
import sysconfig
import time
import json
import random
import pathlib
import inspect
import enum
import zeep
import glob
import shutil
import datetime
from datetime import date
from unidecode import unidecode

from enum import unique
from enum import Enum

#   --------------------------------------------------------------------------   #
#   -                          Imports do Selenium                           -   #
#   --------------------------------------------------------------------------   #
import selenium
from selenium import common
from selenium import webdriver

from selenium.webdriver import common
from selenium.webdriver import support

from webautomators import WebRemoteDriver
from webautomators.extended_options import WebChromeOptions

from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import invisibility_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By as by
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions

#   --------------------------------------------------------------------------   #
#   -                          Imports do PyAutomator                        -   #
#   --------------------------------------------------------------------------   #
import Pyautomators
import orcautomators
import webautomators