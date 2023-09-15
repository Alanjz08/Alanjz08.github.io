# SistemasProgramables
# Sensor DHT22

El sensor DHT22 es un sensor de temperatura y humedad que se utiliza comúnmente con placas de desarrollo como Arduino y Raspberry Pi. 

## Imagenes

- Sensor DHT22
<img src="https://mielectronicafacil.com/wp-content/uploads/2020/08/dht22-pines.jp" alt="Sensor DHT22" width="500" height="450">


## Conexión del sensor

El sensor DHT22 tiene cuatro pines: VCC, GND, Data y NC (No Conectado). Aquí está cómo debes conectarlo:

- Conecta el pin VCC a la fuente de alimentación (generalmente 3.3V o 5V).
- Conecta el pin GND a tierra (GND) en tu placa.
- Conecta el pin Data a un pin digital en tu placa (por ejemplo, GPIO4 en una Raspberry Pi o D2 en un Arduino).

<img src="https://www.hwlibre.com/wp-content/uploads/2019/07/pinout-dht11.jpg.webp" width="600" height="500">

| Pin  | Descripción                                                  |
|------|--------------------------------------------------------------|
| VCC  | Pin (+) Conexión a fuente de alimentación desde 3.3V a 5.5V  |
| DATA | Emite temperatura y humedad a través de datos en serie       |
| NC   | Sin conexión, no utilizar                                    |
| GND  | Pin (-) Conexión a GND o Tierra de la fuente de alimentación |

## Caracteristicas

- Alimentación de 3,3v a 5.5v.
- Consumo de corriente de 2,5mA
- Señal de salida digital
- Rango de temperatura de -40ºC a 125ºC
- Precisión para medir temperatura a 25ºC de 0.5ºC de variación
- La resolución para medir temperatura es de 8-bit, 0,1ºC
- La humedad puede medir desde 0% RH hasta los 100% RH
- Con precisión para la humedad del 2-5% RH para temperaturas que se encuentren entre 0-50ºC
- La resolución es de 0,1% RH, no puede captar variaciones por debajo de esa
- Frecuencia de muestreo de 2 muestras por segundo: 2Hz

## Código de ejemplo

A continuación, se muestra un ejemplo de código en MicroPython para leer la temperatura y humedad del sensor DHT22 en una Raspberry Pi Pico W:

```python
import machine
import dht
import time

# Configura el pin GPIO al que está conectado el sensor DHT22
pin_dht = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)  # Reemplaza "2" con el número de pin correcto

# Crea una instancia del sensor DHT22
sensor = dht.DHT22(pin_dht)

while True:
    try:
        # Lee la temperatura y la humedad
        sensor.measure()
        temperatura = sensor.temperature()
        humedad = sensor.humidity()
        
        # Imprime los resultados
        print("Temperatura: {:.2f}°C".format(temperatura))
        print("Humedad: {:.2f}%".format(humedad))
    
    except Exception as e:
        print("Error al leer el sensor DHT22:", e)

    # Espera un intervalo antes de la próxima lectura (por ejemplo, 2 segundos)
    time.sleep(2)
```
Link del proyecto: https://wokwi.com/projects/375732912259699713
