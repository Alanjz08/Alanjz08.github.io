# Importaciones
import time
import utime
import network  # para WiFi
from machine import Pin, I2C  # para el LED
import ntptime
import ssd1306

# Variables globales para verificar si se ha establecido la hora y si se ha conectado a la red WiFi
global hora_establecida
global wifi_conectado

ssid = 'TecNM-ITT-Docentes'
password = 'tecnm2022!'

def conectar_wifi(ssid, password):
    global wifi_conectado  # Declarar wifi_conectado como una variable global
    # Conectar a WiFi
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    max_espera = 15
    while max_espera > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_espera -= 1
        time.sleep(5)
        print("Conectando a WiFi...")

    if wlan.status() != 3:
        raise RuntimeError('Fallo en la conexión de red')
    else:
        wifi_conectado = True
        estado = wlan.ifconfig()
        print("Conexión exitosa a la red WiFi")

def sincronizar_hora_NTP():
    # Sincronizar la hora con un servidor NTP
    ntptime.settime()
    # Obtener la hora actual como una tupla
    offset_zona_horaria = -7 * 3600  # 7 horas detrás de UTC en segundos
    # Sincronizar la hora con un servidor NTP
    hora_actual = utime.localtime(utime.mktime(utime.localtime()) + offset_zona_horaria)
    # Componentes individuales de la hora
    año = hora_actual[0]
    mes = hora_actual[1]
    dia = hora_actual[2]
    hora = hora_actual[3]
    minuto = hora_actual[4]
    segundo = hora_actual[5]
    dia_de_la_semana = hora_actual[6]
    dia_del_año = hora_actual[7]
    formateado = "{}:{}".format(hora, minuto)
    i2c = I2C(0, scl=1, sda=0)
    display = ssd1306.SSD1306_I2C(128, 64, i2c)
    if 0 <= hora <= 12:
        display.fill(0)
        display.text("Hora:" + formateado, 0, 0)
        display.text("¡Hola Mundo!", 64, 64)
        display.show()
    elif 12 < hora <= 18:
        display.fill(0)
        display.text("Hora:" + formateado, 0, 0)
        display.text("¡Hola Mundo!", 64, 64)
        display.show()
    else:
        display.fill(0)
        display.text("Hora:" + formateado, 0, 0)
        display.text("¡Hola Mundo!", 64, 64)
        display.show()

while True:
    conectar_wifi(ssid, password)
    sincronizar_hora_NTP()
    time.sleep(60)
