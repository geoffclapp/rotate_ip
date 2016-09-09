# rotate_ip
#

import requests
import stem
from stem.control import Controller
import time

from selenium import webdriver
from selenium.webdriver.common.proxy import *

myProxy = '127.0.0.1:8118'

proxy = Proxy({
    'proxyType': ProxyType.MANUAL,
    'httpProxy': myProxy,
    'ftpProxy': myProxy,
    'sslProxy': myProxy,
    'noProxy': ''
    })

driver = webdriver.Firefox(proxy=proxy)

controller = Controller.from_port(port=9051)
controller.authenticate('itstimetomakemoney')

proxies = {
    'http': "127.0.0.1:8118"
}

for i in range(0, 10):

    myip = requests.get('http://api.ipify.org?format=json', proxies=proxies)
    bytes_read = controller.get_info("traffic/read")
    bytes_written = controller.get_info("traffic/written")
    print("My Tor relay has read %s bytes and written %s." % (bytes_read, bytes_written))
    print(myip.content)
    controller.signal(stem.Signal.NEWNYM)
    time.sleep(10)