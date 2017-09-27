import urllib2
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import urllib2
import signal
import sys

driver = None
def signal_handler(signal, frame):
        print('Ctrl+C acionado!')
	driver.quit()
        sys.exit(0)

def open_browser(site):
	global driver
	driver = webdriver.Remote(
	   command_executor='http://localhost:4444/wd/hub',
	   desired_capabilities=DesiredCapabilities.CHROME)
	signal.signal(signal.SIGINT, signal_handler)
        print('Ctrl+C p/ fechar o browser e este script')
	driver.get(site)
	signal.pause()
	
achou = False
while (not achou):
    try:
        conteudo = urllib2.urlopen("http://localhost:4444/wd/hub").read()
        if "<title>WebDriver Hub</title>" in conteudo:
            achou = True
            print "Selenium pronto. Conecte via VNC: vncviewer localhost:5900"
            print "Senha: secret"
    except:
        print "Aguardando selenium..."
        time.sleep(30)
        pass

print "Escolha:"
print "0 - BB"
print "1 - ITAU"
opcao = input("Banco? ")

if opcao not in [0, 1]:
	print "Opcao invalida"
else:
	if opcao == 0:
		print "bb"
		open_browser("https://www2.bancobrasil.com.br/aapf/login.jsp")
	elif opcao == 1:
		print "itau"
		open_browser("https://www.itau.com.br")
	else:
		print "opcao nao tratada"
#driver = webdriver.Remote(
#   command_executor='http://localhost:4444/wd/hub',
#   desired_capabilities=DesiredCapabilities.CHROME)
#driver.get("https://www2.bancobrasil.com.br/aapf/login.jsp")
