import os, platform
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver
from selenium.webdriver.common.proxy import *

PROXY_HOST = '127.0.0.1'
PROXY_PORT = '8118'

def install_proxy(PROXY_HOST, PROXY_PORT):
    fp = webdriver.FirefoxProfile()
    fp.set_preference("network.proxy.type", 1)  
    fp.set_preference("network.proxy.socks",PROXY_HOST)
    fp.set_preference("network.proxy.socks_port",int(PROXY_PORT))   
    fp.set_preference("general.useragent.override","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A")
    fp.update_preferences()
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
    if (platform.system()=='Linux'):
        from xvfbwrapper import Xvfb
        vdisplay = Xvfb(width=1280, height=720)
        vdisplay.start()
        print 'xvfb started'

    
    driver = install_proxy(PROXY_HOST, PROXY_PORT)
    driver.get('http://icanhazip.com')
    print 'obtained browser'
    elem = driver.find_element_by_tag_name('pre')
    print "ip: %s" % elem.get_attribute('innerHTML')

    if (platform.system()=='Linux'):
        vdisplay.kill()


