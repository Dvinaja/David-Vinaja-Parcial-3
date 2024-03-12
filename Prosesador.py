#David Camilo Vinaja Acevedo IRC9.1
import platform
import sys
import subprocess
sistemaop = sys.platform  
sistema = platform.system()  
version = platform.win32_ver()  
hostname = platform.node()
marca_cpu = platform.processor()

print("Estamos en {} en versión: {}".format(sistema, version))
print("Tipo SO: {}".format(sistemaop))
print("Hostname: {}".format(hostname))
print("Marca del CPU: {}".format(marca_cpu))
if sistema == 'Windows':
    local = subprocess.getoutput("""for /f "tokens=2 delims=[]" %a in ('ping -n 1 -4 "%computername%"') do @echo %a""")
else:
    local = subprocess.getoutput("ifconfig | grep 'inet ' | grep -Fv 127.0.0.1 | awk '{print $2}'")
print("Dirección IP local: {}".format(local))
