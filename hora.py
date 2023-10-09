import network
import utime
import urequests as requests

# Configura los detalles de tu red Wi-Fi
SSID = "Internet"
PASSWORD = "Contraseña"

# Conecta a la red Wi-Fi
def conectar_wifi():
    wlan = network.WLAN(network.STA_IF)
    if not wlan.isconnected():
        print("Conectando a la red Wi-Fi...")
        wlan.active(True)
        wlan.connect(SSID, PASSWORD)
        while not wlan.isconnected():
            pass
    print("Conexión exitosa a la red Wi-Fi")
    print("Dirección IP:", wlan.ifconfig()[0])

# Función para obtener la hora de Internet
def obtener_hora_de_internet():
    try:
        respuesta = requests.get("http://worldclockapi.com/api/json/pst/now")

        if respuesta.status_code == 200:
            datos = respuesta.json()
            hora_actual = datos["currentDateTime"]

            return hora_actual
        else:
            print("Error al obtener la hora de Internet:", respuesta.status_code)
    except Exception as e:
        print("Error:", e)

    return None

# Conexión a la red Wi-Fi
conectar_wifi()

while True:
    hora = obtener_hora_de_internet()
    if hora:
        print("Hora en PST (Tijuana):", hora)
    
    utime.sleep(3600)  # Espera 1 hora antes de obtener la hora nuevamente
