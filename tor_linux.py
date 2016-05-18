import os, platform
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver
from selenium.webdriver.common.proxy import *
from xvfbwrapper import Xvfb

PROXY_HOST = '127.0.0.1'
PROXY_PORT = '9050'

def install_proxy(PROXY_HOST, PROXY_PORT):
    fp = webdriver.FirefoxProfile()
    fp.set_preference("network.proxy.type", 1)  
    fp.set_preference("network.proxy.socks",PROXY_HOST)
    fp.set_preference("network.proxy.socks_port",int(PROXY_PORT))   
    print 'proxy set'
    return webdriver.Firefox(firefox_profile=fp)


'''path to the firefox binary inside the Tor package'''
binary = './TorBrowser.app/Contents/MacOS/firefox'
#binary = '/Applications/TorBrowser.app/Contents/MacOS/firefox'


if os.path.exists(binary) is False:
    raise ValueError("The binary path to Tor firefox does not exist.")
firefox_binary = FirefoxBinary(binary)

browser = None
def get_browser(binary=None):
    global browser  
    # only one instance of a browser opens, remove global for multiple instances
    if not browser: 
        browser = webdriver.Firefox(firefox_binary=binary)
    return browser

if __name__ == "__main__":
    #vdisplay = Xvfb(width=1280, height=720)
    #vdisplay.start()
    #print 'xvfb started'

    
    driver = install_proxy(PROXY_HOST, PROXY_PORT)
    driver.set_page_load_timeout(30)
    driver.get('http://icanhazip.com')
    print 'obtained browser'
    elem = driver.find_element_by_tag_name('pre')
    print "ip: %s" % elem.get_attribute('innerHTML')

    #vdisplay.kill()


