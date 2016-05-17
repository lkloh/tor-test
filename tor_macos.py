import os, platform
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver



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

    browser = get_browser(binary=firefox_binary)
    urls = (
        ('tor browser check', 'https://check.torproject.org/'),
        ('ip checker', 'http://icanhazip.com')
    )
    for url_name, url in urls:
        print "getting", url_name, "at", url
        browser.get(url)

    if (platform.system()=='Linux'):
        vdisplay.kill()


