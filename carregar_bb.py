import urllib2
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import urllib2

achou = False
while (not achou):
    try:
        conteudo = urllib2.urlopen("http://localhost:4444/wd/hub").read()
        if "<title>WebDriver Hub</title>" in conteudo:
            achou = True
            print "Selenium pronto. Conecte via VNC: localhost:5900"
            print "Senha: secret"
    except:
        print "Aguardando selenium..."
        time.sleep(30)
        pass

driver = webdriver.Remote(
   command_executor='http://localhost:4444/wd/hub',
   desired_capabilities=DesiredCapabilities.CHROME)
driver.get("https://www2.bancobrasil.com.br/aapf/login.jsp")
