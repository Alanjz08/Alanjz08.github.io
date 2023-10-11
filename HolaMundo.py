# Importar las bibliotecas necesarias
import machine
import ssd1306

# Configurar el pin SDA y SCL (puertos 0 y 1 en la Raspberry Pi Pico)
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)

# Crear una instancia del controlador de la pantalla OLED
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Borrar la pantalla
oled.fill(0)
oled.show()

# Escribir "Hola Mundo" en la pantalla
oled.text("Hola Mundo", 0, 0)

# Mostrar el texto en la pantalla
oled.show()
