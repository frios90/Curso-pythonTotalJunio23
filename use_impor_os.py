import os
import sys
import platform
import distro

print("----------------SYS")
print('uname:', platform.uname())
print('system   :', platform.system())
print('node     :', platform.node())
print('release  :', platform.release())
print('version  :', platform.version())
print('machine  :', platform.machine())
print('processor:', platform.processor())
print('distribution:', distro.name())
print('VERSION distribution:', distro.version())
print('ID distribution:', distro.id())

print("----------------SYS")

print("----------------OS")
# os.chdir("/home/japp/Documentos/") ##para cambiar de directorio
#http://research.iac.es/sieinvens/python-course/modulos.html#conexion-remota-por-ftp-y-ssh

# Esto no imita a ls, no distingue ficheros y directorios
ficheros = os.listdir(".")  # hay que poner una ruta

# nuevoArchivo = open("fechas.py", "w")
# nuevoArchivo.close()

for fichero in ficheros:

    print (os.path.basename)  # .isfile(), islink()

#crear un directorio

try :
    os.mkdir("os_practica")
except :
    print("La carpeta ya existe")
    pass

os.chdir("os_practica")
try :
    os.mkdir("carpeta")
except :
    print("La carpeta ya existe")
    pass

os.chdir("./")
try :
    os.mkdir("carpeta")
except :
    print("La carpeta ya existe")
    pass

ruta = os.getcwd();
print(ruta)

getcwdb=os.getcwdb()
print(getcwdb)

getegid=os.getegid()
print(getegid)