import datetime
import locale
import time
import calendar
print("La fecha y hora actuales: " , datetime.datetime.now())  # Devuelve un objeto datetime
print("Fecha y hora en string con formato: " , datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("ff: ", datetime.date.today())
print("Año actual: ", datetime.date.today().strftime("%Y"))

print("Año actual: ", datetime.date.today().strftime("%Y"))
print("Mes del año: ", datetime.date.today().strftime("%B"))
print("Semana del año: ", datetime.date.today().strftime("%W"))
print("Número de día de la semana: ", datetime.date.today().strftime("%w"))
print("Día del año: ", datetime.date.today().strftime("%j"))
print("Día del mes: ", datetime.date.today().strftime("%d"))
print("Día día de la semana: ", datetime.date.today().strftime("%A"))


print("Segundos desde inicio de época: %s" %time.time())

# Para una fecha específica

fecha = datetime.date(1937, 10, 8)  #year, month, day
print(fecha.strftime("%A"))
# Friday

print(fecha.strftime("%b %d %Y %H:%M:%S"))
# Oct 08 1937 00:00:00


#-----------------------------------------------
print("---------------------------------------------------------2")
# Fecha en string
fecha_str = "2017-05-16 10:30:00"

# Formato en el que está la fecha en string
fecha_fmt = "%Y-%m-%d %H:%M:%S"

# Objeto datetime a partir de la fecha en string
fecha = datetime.datetime.strptime(fecha_str, fecha_fmt)

print(fecha.strftime("%A %d %B, %Y"))
# 'Tuesday 16 May, 2017'

# Cambio de idioma


print(fecha.strftime("%A %d %B, %Y"))
# martes 16 mayo, 2017


hoy = datetime.date.today()
print('Hoy:', hoy)

un_dia = datetime.timedelta(days=1)
print('Lapso de un día:', un_dia)

ayer = hoy - un_dia
print('Ayer:', ayer)

manhana = hoy + un_dia
print('Manhana :', manhana)

print('Manhana - ayer:', manhana - ayer)
print('Ayer - manhana:', ayer - manhana)


cal = calendar.month(2023,5)
print(cal)