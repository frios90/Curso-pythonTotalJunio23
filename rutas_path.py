from pathlib import Path
import os
base = Path.home()
ruta = Path(base, 'www', 'PYTHON', 'Curso.Python-Total')
ruta2 = ruta.with_name('Otra_carpeta')
print(ruta)
print(ruta2)

# os.makedirs("ruta2")

print(os.getlogin())

directorio_actual = os.getcwd()
print("directorio_actual : " + directorio_actual)


ruta3 = Path("/home",os.getlogin())
print(ruta3)

# os.chdir(ruta): cambia el directorio de trabajo a la ruta especificada
os.chdir(ruta3)
directorio_actual = os.getcwd()
print("directorio_actual : " + directorio_actual)

# os.makedirs(ruta): crea una carpeta, así como todas las carpetas intermedias necesarias de acuerdo a la ruta especificada.
try:
    os.makedirs("PYTHON_AUTOCOPY")
except:
    print("error: la carpeta ya existe")


# This would print all the files and directories
dirs = os.listdir(directorio_actual )
for file in dirs:
   print(file)

