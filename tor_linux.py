from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium import webdriver
import platform


proxy_address = "127.0.0.1:9050"
sproxy = Proxy({
    'proxyType': ProxyType.MANUAL,
    'httpProxy': proxy_address,
})



if __name__ == "__main__":
    if (platform.system()=='Linux'):
        from xvfbwrapper import Xvfb
        vdisplay = Xvfb(width=1280, height=720)
        vdisplay.start()

    driver = webdriver.Firefox(proxy=sproxy)
    driver.get('https://check.torproject.org/')
    elem = driver.get_element_by_class_name('content')
    print elem.get_attribute('innerHTML')

    if (platform.system()=='Linux'):
        vdisplay.kill()





