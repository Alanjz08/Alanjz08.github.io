import time
import network
import socket
from machine import Pin

led = machine.Pin('LED', machine.Pin.OUT)
ledState = "Led State Unknown"

button = Pin(16, Pin.IN, Pin.PULL_UP)

ssid = ""
password = ""

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

html = """
<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="data:,">
    <style>
      html {
        font-family: Helvetica;
        display: inline-block;
        margin: 0px auto;
        text-align: center;
      }

      .buttonON {
        background-color: #ECF766;
        border: 0px solid #000000;
        ;
        color: black;
        padding: 15px 56px;
        text-align: center;
        text-decoration: none;
        display: flex;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
      }

      .buttonOFF {
        background-color: #ADADAD;
        border: 0px solid #000000;
        ;
        color: white;
        padding: 15px 56px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
      }
     
      .button-container {
      display: inline-block;
      vertical-align: top;
    }
    
    .image-container {
      display: block;
    }
    
      text-decoration: none;
      font-size: 30px;
      margin: 2px;
      cursor: pointer;
      }
    </style>
  </head>
  <body>
    <center>
      <h1>Prende y apaga un led</h1>
    </center>
    <br>
    <br>
    <form>
      <center>
        <center>
          <div class="button-container">
              <button class="buttonON" name="led" value="on" type="submit">Encender</button>
          </div>
          <div class="button-container">
              <button class="buttonOFF" name="led" value="off" type="submit">Apagar</button>
          </div>
          <br>
          <br>
          <center>
    </form>
    <br>
    <br>
    <br>
    <br>
    <p>%s
    </p>
  </body>
</html>
"""

max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print("waiting for connection...")
    time.sleep(1)
    
if wlan.status() != 3:
    raise RuntimeError("network connection failed")
else:
    print("Connected")
    status = wlan.ifconfig()
    print("ip =" + status[0])
    
addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
print("listening on", addr)

while True:
    try:
        cl, addr = s.accept()
        print("clien connected from", addr)
        request = cl.recv(1024)
        print("request:")
        print(request)
        request = str(request)
        led_on = request.find('led=on')
        led_off = request.find('led=off')
        
        print('led on =' + str(led_on))
        print( 'led off = ' + str(led_off))
        
        if led_on == 8:
            print('led on')
            led.value(1)
        if led_off == 8:
            print('led off')
            led.value(0)
            
        ledState = "LED is OFF" if led.value() == 0 else "LED is ON"
        
        if button.value() == 1:
            print("button NOT pressed")
            buttonState = "Button is NOT pressed"
        else:
            print("button pressed")
            buttonState = "Button is pressed"
            
        stateis = ledState + " and " + buttonState
        response = html % stateis
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(response)
        cl.close()
        
    except OSError as e:
        cl.close()
        print('connection closed')
