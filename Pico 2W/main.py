"""
# === CONFIGURAÇÕES WIFI ===
WIFI_SSID = "iPhone A C Dratcu"      # Altere para seu WiFi
WIFI_PASSWORD = "s7wgr4dobgdse"  # Altere para sua senha



font = {
    # NÚMEROS
    '0': [0x3C, 0x66, 0x6A, 0x72, 0x66, 0x66, 0x3C, 0x00],
    '1': [0x18, 0x18, 0x38, 0x18, 0x18, 0x18, 0x7E, 0x00],
    '2': [0x3C, 0x66, 0x06, 0x0C, 0x30, 0x60, 0x7E, 0x00],
    '3': [0x3C, 0x66, 0x06, 0x1C, 0x06, 0x66, 0x3C, 0x00],
    '4': [0x06, 0x0E, 0x1E, 0x66, 0x7F, 0x06, 0x06, 0x00],
    '5': [0x7E, 0x60, 0x7C, 0x06, 0x06, 0x66, 0x3C, 0x00],
    '6': [0x3C, 0x66, 0x60, 0x7C, 0x66, 0x66, 0x3C, 0x00],
    '7': [0x7E, 0x66, 0x0C, 0x18, 0x18, 0x18, 0x18, 0x00],
    '8': [0x3C, 0x66, 0x66, 0x3C, 0x66, 0x66, 0x3C, 0x00],
    '9': [0x3C, 0x66, 0x66, 0x3E, 0x06, 0x66, 0x3C, 0x00],
    
    # SÍMBOLOS
    ':': [0x00, 0x00, 0x18, 0x00, 0x00, 0x18, 0x00, 0x00],
    '/': [0x00, 0x03, 0x06, 0x0C, 0x18, 0x30, 0x60, 0x00],
    '-': [0x00, 0x00, 0x00, 0x7E, 0x00, 0x00, 0x00, 0x00],
    '.': [0x00, 0x00, 0x00, 0x00, 0x00, 0x18, 0x18, 0x00],
    ' ': [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    
    # MAIÚSCULAS
    'A': [0x18, 0x3C, 0x66, 0x7E, 0x66, 0x66, 0x66, 0x00],
    'B': [0x7C, 0x66, 0x66, 0x7C, 0x66, 0x66, 0x7C, 0x00],
    'C': [0x3C, 0x66, 0x60, 0x60, 0x60, 0x66, 0x3C, 0x00],
    'D': [0x78, 0x6C, 0x66, 0x66, 0x66, 0x6C, 0x78, 0x00],
    'E': [0x7E, 0x60, 0x60, 0x78, 0x60, 0x60, 0x7E, 0x00],
    'F': [0x7E, 0x60, 0x60, 0x78, 0x60, 0x60, 0x60, 0x00],
    'G': [0x3C, 0x66, 0x60, 0x6E, 0x66, 0x66, 0x3C, 0x00],
    'H': [0x66, 0x66, 0x66, 0x7E, 0x66, 0x66, 0x66, 0x00],
    'I': [0x3C, 0x18, 0x18, 0x18, 0x18, 0x18, 0x3C, 0x00],
    'J': [0x1E, 0x0C, 0x0C, 0x0C, 0x0C, 0x6C, 0x38, 0x00],
    'K': [0x66, 0x6C, 0x78, 0x70, 0x78, 0x6C, 0x66, 0x00],
    'L': [0x60, 0x60, 0x60, 0x60, 0x60, 0x60, 0x7E, 0x00],
    'M': [0x63, 0x77, 0x7F, 0x6B, 0x63, 0x63, 0x63, 0x00],
    'N': [0x66, 0x76, 0x7E, 0x7E, 0x6E, 0x66, 0x66, 0x00],
    'O': [0x3C, 0x66, 0x66, 0x66, 0x66, 0x66, 0x3C, 0x00],
    'P': [0x7C, 0x66, 0x66, 0x7C, 0x60, 0x60, 0x60, 0x00],
    'Q': [0x3C, 0x66, 0x66, 0x66, 0x6A, 0x6C, 0x36, 0x00],
    'R': [0x7C, 0x66, 0x66, 0x7C, 0x78, 0x6C, 0x66, 0x00],
    'S': [0x3C, 0x66, 0x60, 0x3C, 0x06, 0x66, 0x3C, 0x00],
    'T': [0x7E, 0x18, 0x18, 0x18, 0x18, 0x18, 0x18, 0x00],
    'U': [0x66, 0x66, 0x66, 0x66, 0x66, 0x66, 0x3C, 0x00],
    'V': [0x66, 0x66, 0x66, 0x66, 0x66, 0x3C, 0x18, 0x00],
    'W': [0x63, 0x63, 0x63, 0x6B, 0x7F, 0x77, 0x63, 0x00],
    'X': [0x66, 0x66, 0x3C, 0x18, 0x3C, 0x66, 0x66, 0x00],
    'Y': [0x66, 0x66, 0x66, 0x3C, 0x18, 0x18, 0x18, 0x00],
    'Z': [0x7E, 0x06, 0x0C, 0x18, 0x30, 0x60, 0x7E, 0x00],
    
    # MINÚSCULAS
    'a': [0x00, 0x00, 0x3C, 0x06, 0x3E, 0x66, 0x3E, 0x00],
    'b': [0x60, 0x60, 0x7C, 0x66, 0x66, 0x66, 0x7C, 0x00],
    'c': [0x00, 0x00, 0x3C, 0x60, 0x60, 0x60, 0x3C, 0x00],
    'd': [0x06, 0x06, 0x3E, 0x66, 0x66, 0x66, 0x3E, 0x00],
    'e': [0x00, 0x00, 0x3C, 0x66, 0x7E, 0x60, 0x3C, 0x00],
    'f': [0x0E, 0x18, 0x18, 0x7E, 0x18, 0x18, 0x18, 0x00],
    'g': [0x00, 0x00, 0x3E, 0x66, 0x66, 0x3E, 0x06, 0x7C],
    'h': [0x60, 0x60, 0x7C, 0x66, 0x66, 0x66, 0x66, 0x00],
    'i': [0x18, 0x00, 0x38, 0x18, 0x18, 0x18, 0x3C, 0x00],
    'j': [0x06, 0x00, 0x0E, 0x06, 0x06, 0x06, 0x66, 0x3C],
    'k': [0x60, 0x60, 0x66, 0x6C, 0x78, 0x6C, 0x66, 0x00],
    'l': [0x38, 0x18, 0x18, 0x18, 0x18, 0x18, 0x3C, 0x00],
    'm': [0x00, 0x00, 0x66, 0x7F, 0x7F, 0x6B, 0x63, 0x00],
    'n': [0x00, 0x00, 0x7C, 0x66, 0x66, 0x66, 0x66, 0x00],
    'o': [0x00, 0x00, 0x3C, 0x66, 0x66, 0x66, 0x3C, 0x00],
    'p': [0x00, 0x00, 0x7C, 0x66, 0x66, 0x7C, 0x60, 0x60],
    'q': [0x00, 0x00, 0x3E, 0x66, 0x66, 0x3E, 0x06, 0x06],
    'r': [0x00, 0x00, 0x7C, 0x66, 0x60, 0x60, 0x60, 0x00],
    's': [0x00, 0x00, 0x3E, 0x60, 0x3C, 0x06, 0x7C, 0x00],
    't': [0x18, 0x18, 0x7E, 0x18, 0x18, 0x18, 0x0E, 0x00],
    'u': [0x00, 0x00, 0x66, 0x66, 0x66, 0x66, 0x3E, 0x00],
    'v': [0x00, 0x00, 0x66, 0x66, 0x66, 0x3C, 0x18, 0x00],
    'w': [0x00, 0x00, 0x63, 0x6B, 0x7F, 0x7F, 0x36, 0x00],
    'x': [0x00, 0x00, 0x66, 0x3C, 0x18, 0x3C, 0x66, 0x00],
    'y': [0x00, 0x00, 0x66, 0x66, 0x66, 0x3E, 0x0C, 0x78],
    'z': [0x00, 0x00, 0x7E, 0x0C, 0x18, 0x30, 0x7E, 0x00],
    
    # CARACTERES ESPECIAIS PORTUGUÊS
    'ã': [0x36, 0x6C, 0x3C, 0x06, 0x3E, 0x66, 0x3E, 0x00],
    'Ã': [0x36, 0x6C, 0x18, 0x3C, 0x66, 0x7E, 0x66, 0x00],
    'ç': [0x00, 0x00, 0x3C, 0x60, 0x60, 0x3C, 0x18, 0x30],
    'Ç': [0x3C, 0x66, 0x60, 0x60, 0x60, 0x3C, 0x18, 0x30],
    'é': [0x00, 0x18, 0x00, 0x3C, 0x66, 0x7E, 0x60, 0x3C],~
    'Õ': [0x34, 0x58, 0x00, 0x3C, 0x66, 0x66, 0x66, 0x3C],
    'õ':[0x34, 0x58, 0x00, 0x3C, 0x66, 0x66, 0x66, 0x3C]
}
"""
# main.py - Magic Mirror - VERSÃO FINAL SEM ERROS
import machine
import utime
import ujson
import ubluetooth
import gc
import network
import ntptime
import urequests
from machine import Pin, RTC

print("MAGIC MIRROR - Iniciando...")

# === CONFIGURACOES ===
WIFI_SSID = "Bruno Dratcu"
WIFI_PASSWORD = "deniederror"
SERVER_IP = "192.168.1.100"
SERVER_PORT = 5000

SERVICE_UUID = ubluetooth.UUID("12345678-1234-5678-9abc-123456789abc")
EVENTS_CHAR_UUID = ubluetooth.UUID("12345678-1234-5678-9abc-123456789abd")
RESPONSE_CHAR_UUID = ubluetooth.UUID("12345678-1234-5678-9abc-123456789abe")

# === HARDWARE ===
rtc = RTC()

rst = Pin(16, Pin.OUT, value=1)
cs = Pin(17, Pin.OUT, value=1)
rs = Pin(15, Pin.OUT, value=0)
wr = Pin(19, Pin.OUT, value=1)
rd = Pin(18, Pin.OUT, value=1)
data_pins = [Pin(i, Pin.OUT) for i in [0,1,2,3,4,5,6,7]]

# Cores
BLACK = 0x0000
WHITE = 0xFFFF
RED = 0xF800
GREEN = 0x07E0
CYAN = 0x07FF

# Estado global
display_on = True
events = []
ble_connected = False
message_buffer = ""
wifi_status = False
modo_offline = True

# === DISPLAY ===
def write_byte(data):
    for i in range(8):
        data_pins[i].value((data >> i) & 1)

def cmd(c):
    cs.value(0)
    rs.value(0)
    write_byte(c)
    wr.value(0)
    wr.value(1)
    cs.value(1)

def dat(d):
    cs.value(0)
    rs.value(1)
    write_byte(d)
    wr.value(0)
    wr.value(1)
    cs.value(1)

def init_lcd():
    rst.value(0)
    utime.sleep_ms(50)
    rst.value(1)
    utime.sleep_ms(50)
    cmd(0x01)
    utime.sleep_ms(100)
    cmd(0x11)
    utime.sleep_ms(100)
    cmd(0x3A)
    dat(0x55)
    cmd(0x36)
    dat(0xE8)
    cmd(0x29)
    utime.sleep_ms(50)

def set_area(x0, y0, x1, y1):
    cmd(0x2A)
    dat(x0>>8)
    dat(x0&0xFF)
    dat(x1>>8)
    dat(x1&0xFF)
    cmd(0x2B)
    dat(y0>>8)
    dat(y0&0xFF)
    dat(y1>>8)
    dat(y1&0xFF)
    cmd(0x2C)

def fill_rect(x, y, w, h, color):
    if not display_on or w<=0 or h<=0: 
        return
    try:
        set_area(x, y, x+w-1, y+h-1)
        ch = color >> 8
        cl = color & 0xFF
        cs.value(0)
        rs.value(1)
        for _ in range(w*h):
            write_byte(ch)
            wr.value(0)
            wr.value(1)
            write_byte(cl)
            wr.value(0)
            wr.value(1)
        cs.value(1)
    except:
        pass

# === FONTE ===
font = {
    '0': [0x3C, 0x66, 0x6A, 0x72, 0x66, 0x66, 0x3C, 0x00],
    '1': [0x18, 0x18, 0x38, 0x18, 0x18, 0x18, 0x7E, 0x00],
    '2': [0x3C, 0x66, 0x06, 0x0C, 0x30, 0x60, 0x7E, 0x00],
    '3': [0x3C, 0x66, 0x06, 0x1C, 0x06, 0x66, 0x3C, 0x00],
    '4': [0x06, 0x0E, 0x1E, 0x66, 0x7F, 0x06, 0x06, 0x00],
    '5': [0x7E, 0x60, 0x7C, 0x06, 0x06, 0x66, 0x3C, 0x00],
    '6': [0x3C, 0x66, 0x60, 0x7C, 0x66, 0x66, 0x3C, 0x00],
    '7': [0x7E, 0x66, 0x0C, 0x18, 0x18, 0x18, 0x18, 0x00],
    '8': [0x3C, 0x66, 0x66, 0x3C, 0x66, 0x66, 0x3C, 0x00],
    '9': [0x3C, 0x66, 0x66, 0x3E, 0x06, 0x66, 0x3C, 0x00],
    ':': [0x00, 0x00, 0x18, 0x00, 0x00, 0x18, 0x00, 0x00],
    '/': [0x00, 0x03, 0x06, 0x0C, 0x18, 0x30, 0x60, 0x00],
    '-': [0x00, 0x00, 0x00, 0x7E, 0x00, 0x00, 0x00, 0x00],
    ' ': [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    'A': [0x18, 0x3C, 0x66, 0x7E, 0x66, 0x66, 0x66, 0x00],
    'B': [0x7C, 0x66, 0x66, 0x7C, 0x66, 0x66, 0x7C, 0x00],
    'C': [0x3C, 0x66, 0x60, 0x60, 0x60, 0x66, 0x3C, 0x00],
    'D': [0x78, 0x6C, 0x66, 0x66, 0x66, 0x6C, 0x78, 0x00],
    'E': [0x7E, 0x60, 0x60, 0x78, 0x60, 0x60, 0x7E, 0x00],
    'F': [0x7E, 0x60, 0x60, 0x78, 0x60, 0x60, 0x60, 0x00],
    'G': [0x3C, 0x66, 0x60, 0x6E, 0x66, 0x66, 0x3C, 0x00],
    'H': [0x66, 0x66, 0x66, 0x7E, 0x66, 0x66, 0x66, 0x00],
    'I': [0x3C, 0x18, 0x18, 0x18, 0x18, 0x18, 0x3C, 0x00],
    'J': [0x1E, 0x0C, 0x0C, 0x0C, 0x0C, 0x6C, 0x38, 0x00],
    'L': [0x60, 0x60, 0x60, 0x60, 0x60, 0x60, 0x7E, 0x00],
    'M': [0x63, 0x77, 0x7F, 0x6B, 0x63, 0x63, 0x63, 0x00],
    'N': [0x66, 0x76, 0x7E, 0x7E, 0x6E, 0x66, 0x66, 0x00],
    'O': [0x3C, 0x66, 0x66, 0x66, 0x66, 0x66, 0x3C, 0x00],
    'P': [0x7C, 0x66, 0x66, 0x7C, 0x60, 0x60, 0x60, 0x00],
    'R': [0x7C, 0x66, 0x66, 0x7C, 0x78, 0x6C, 0x66, 0x00],
    'S': [0x3C, 0x66, 0x60, 0x3C, 0x06, 0x66, 0x3C, 0x00],
    'T': [0x7E, 0x18, 0x18, 0x18, 0x18, 0x18, 0x18, 0x00],
    'U': [0x66, 0x66, 0x66, 0x66, 0x66, 0x66, 0x3C, 0x00],
    'V': [0x66, 0x66, 0x66, 0x66, 0x66, 0x3C, 0x18, 0x00],
    'X': [0x66, 0x66, 0x3C, 0x18, 0x3C, 0x66, 0x66, 0x00],
    'Y': [0x66, 0x66, 0x66, 0x3C, 0x18, 0x18, 0x18, 0x00],
    'Õ': [0x34, 0x58, 0x00, 0x3C, 0x66, 0x66, 0x66, 0x3C],
    'õ': [0x34, 0x58, 0x00, 0x3C, 0x66, 0x66, 0x66, 0x3C]
}

def draw_char(x, y, char, color, size):
    if not display_on or char not in font: 
        return
    try:
        bitmap = font[char]
        for row in range(8):
            byte = bitmap[row]
            for col in range(8):
                if byte & (0x80 >> col):
                    fill_rect(x + col*size, y + row*size, size, size, color)
    except:
        pass

def draw_text(x, y, text, color, size):
    if not display_on: 
        return
    try:
        for i, c in enumerate(text):
            draw_char(x + i*(8*size + 2*size), y, c.upper(), color, size)
    except:
        pass

def draw_centered(y, text, color, size):
    if not display_on: 
        return
    try:
        w = len(text) * (8*size + 2*size) - 2*size
        x = (480 - w) // 2
        draw_text(x, y, text, color, size)
    except:
        pass

def format_date(d, m, y):
    d_str = "0" + str(d) if d < 10 else str(d)
    m_str = "0" + str(m) if m < 10 else str(m)
    return d_str + "/" + m_str + "/" + str(y)

# === WIFI ===
def conectar_wifi():
    global wifi_status, modo_offline
    
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    if wlan.isconnected():
        if not wifi_status:
            print("WiFi detectado como conectado!")
            wifi_status = True
            modo_offline = False
            utime.sleep_ms(200)
            redesenhar_tela_completa()
            sincronizar_horario_ntp()
        return True
    
    print("Tentando conectar WiFi...")
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)
    
    timeout = 3
    while timeout > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        timeout -= 1
        utime.sleep(1)
    
    if wlan.isconnected():
        print("WiFi conectado!")
        wifi_status = True
        modo_offline = False
        utime.sleep_ms(200)
        redesenhar_tela_completa()
        sincronizar_horario_ntp()
        return True
    else:
        wifi_status = False
        modo_offline = True
        return False

def sincronizar_horario_ntp():
    if not wifi_status:
        return False
        
    try:
        ntptime.settime()
        timestamp_utc = utime.time()
        timestamp_brasilia = timestamp_utc - (3 * 3600)
        brasilia_time = utime.localtime(timestamp_brasilia)
        
        rtc.datetime((brasilia_time[0], brasilia_time[1], brasilia_time[2], 
                     brasilia_time[6], brasilia_time[3], brasilia_time[4], 
                     brasilia_time[5], 0))
        
        return True
    except:
        return False

def verificar_status_wifi():
    global wifi_status, modo_offline
    
    wlan = network.WLAN(network.STA_IF)
    wifi_conectado_agora = wlan.isconnected()
    
    if wifi_conectado_agora != wifi_status:
        if wifi_conectado_agora:
            print("WiFi reconectado - atualizando...")
            wifi_status = True
            modo_offline = False
            redesenhar_tela_completa()
            sincronizar_horario_ntp()
            buscar_eventos_servidor()
        else:
            print("WiFi desconectado")
            wifi_status = False
            modo_offline = True

def buscar_eventos_servidor():
    if not wifi_status:
        return False
        
    try:
        wlan = network.WLAN(network.STA_IF)
        if not wlan.isconnected():
            return False
        
        url = "http://" + SERVER_IP + ":" + str(SERVER_PORT) + "/api/eventos-hoje"
        response = urequests.get(url, timeout=5)
        
        if response.status_code == 200:
            eventos_json = response.json()
            response.close()
            
            global events
            events = []
            
            for evento in eventos_json:
                events.append({
                    'id': evento.get('id'),
                    'nome': evento.get('nome', 'Sem nome'),
                    'hora': evento.get('hora', '--:--')
                })
            
            return True
        else:
            response.close()
            return False
    except:
        return False

def mostrar_status_wifi():
    fill_rect(430, 10, 40, 12, BLACK)
    if modo_offline:
        draw_text(430, 10, "OFF", RED, 1)
    else:
        draw_text(430, 10, "ON", GREEN, 1)

def mostrar_status_ble():
    fill_rect(10, 10, 30, 12, BLACK)
    draw_text(10, 10, "BLE", GREEN if ble_connected else RED, 1)

def redesenhar_tela_completa():
    try:
        fill_rect(0, 0, 480, 320, BLACK)
        utime.sleep_ms(100)
        
        draw_text(160, 80, ":", WHITE, 4)
        draw_text(280, 80, ":", WHITE, 4)
        
        mostrar_status_ble()
        mostrar_status_wifi()
        
    except:
        pass

# === BLE ===
class BLE:
    def __init__(self):
        try:
            self.ble = ubluetooth.BLE()
            self.ble.active(True)
            self.ble.irq(self._irq)
            
            events_char = (EVENTS_CHAR_UUID, ubluetooth.FLAG_WRITE | ubluetooth.FLAG_WRITE_NO_RESPONSE)
            response_char = (RESPONSE_CHAR_UUID, ubluetooth.FLAG_READ | ubluetooth.FLAG_NOTIFY)
            
            service = (SERVICE_UUID, (events_char, response_char))
            ((self.events_handle, self.response_handle),) = self.ble.gatts_register_services((service,))
            
            self._advertise()
            
        except:
            pass
    
    def _advertise(self):
        try:
            name = b'MagicMirror'
            payload = bytearray()
            payload.extend(b'\x02\x01\x06')
            payload.extend(bytes([len(name) + 1, 0x09]) + name)
            self.ble.gap_advertise(100, payload)
        except:
            pass
    
    def _irq(self, event, data):
        global ble_connected, message_buffer
        
        try:
            if event == 1:
                ble_connected = True
                message_buffer = ""
                
            elif event == 2:
                ble_connected = False
                message_buffer = ""
                self._advertise()
                
            elif event == 3:
                conn_handle, attr_handle = data
                if attr_handle == self.events_handle:
                    written_data = self.ble.gatts_read(attr_handle)
                    self._handle_received_data(written_data)
        except:
            pass
    
    def _handle_received_data(self, data):
        global message_buffer
        
        try:
            chunk = data.decode('utf-8')
            message_buffer += chunk
            
            while '\n' in message_buffer:
                line, message_buffer = message_buffer.split('\n', 1)
                line = line.strip()
                
                if line and line.startswith('{'):
                    self._process_json_message(line)
        except:
            message_buffer = ""
    
    def _process_json_message(self, json_str):
        global events
        
        try:
            print("Decodificando JSON BLE...")
            message = ujson.loads(json_str)
            action = message.get("action", "")
            
            print("AÇÃO BLE RECEBIDA: " + action)
            
            if action == "ping":
                print("Ping recebido do servidor")
                
            elif action == "sync_events":
                new_events = message.get("events", [])
                count = message.get("count", 0)
                server_date = message.get("date", "")
                
                print("=== SINCRONIZAÇÃO BLE ===")
                print("Eventos recebidos: " + str(count))
                print("Data servidor: " + server_date)
                
                if len(new_events) > 0:
                    print("Primeiro evento: " + str(new_events[0]))
                
                t = rtc.datetime()
                current_date_str = str(t[0]) + "-"
                if t[1] < 10:
                    current_date_str += "0"
                current_date_str += str(t[1]) + "-"
                if t[2] < 10:
                    current_date_str += "0"
                current_date_str += str(t[2])
                
                print("Data local: " + current_date_str)
                
                eventos_hoje = []
                for event in new_events:
                    event_date = event.get('data', '')
                    event_nome = event.get('nome', '')
                    event_hora = event.get('hora', '')
                    
                    print("Verificando evento: " + event_date + " vs " + current_date_str)
                    
                    if event_date == current_date_str:
                        eventos_hoje.append({
                            'id': event.get('id'),
                            'nome': event_nome,
                            'hora': event_hora
                        })
                        print("EVENTO ADICIONADO: " + event_hora + " - " + event_nome)
                    else:
                        print("Evento ignorado (data diferente): " + event_date)
                
                # Atualiza lista global
                events = eventos_hoje[:3]
                print("TOTAL EVENTOS SINCRONIZADOS: " + str(len(events)))
                
                # Lista eventos finais
                for i, evt in enumerate(events):
                    print("Evento " + str(i+1) + ": " + evt['hora'] + " - " + evt['nome'])
                
            else:
                print("Ação BLE desconhecida: " + action)
                
        except Exception as e:
            print("ERRO ao processar JSON BLE: " + str(e))
            print("JSON problemático: " + json_str[:100])

# === CONTROLES ===
last_time = {'h': None, 'm': None, 's': None}
last_date = {'d': None, 'm': None, 'y': None}
last_events_display = []
last_ble = None
last_wifi_status = None

def update_display():
    global last_time, last_date, last_events_display, last_ble, last_wifi_status
    
    if not display_on: 
        return
    
    try:
        t = rtc.datetime()
        h, m, s = t[4], t[5], t[6]
        d, mo, y = t[2], t[1], t[0]
        
        if h != last_time['h']:
            fill_rect(80, 80, 80, 40, BLACK)
            h_str = "0" + str(h) if h < 10 else str(h)
            draw_text(80, 80, h_str, WHITE, 4)
            last_time['h'] = h
        
        if m != last_time['m']:
            fill_rect(200, 80, 80, 40, BLACK)
            m_str = "0" + str(m) if m < 10 else str(m)
            draw_text(200, 80, m_str, WHITE, 4)
            last_time['m'] = m
        
        if s != last_time['s']:
            fill_rect(320, 80, 80, 40, BLACK)
            s_str = "0" + str(s) if s < 10 else str(s)
            draw_text(320, 80, s_str, WHITE, 4)
            last_time['s'] = s
        
        if d != last_date['d'] or mo != last_date['m'] or y != last_date['y']:
            fill_rect(120, 140, 240, 25, BLACK)
            date_str = format_date(d, mo, y)
            draw_centered(140, date_str, WHITE, 2)
            last_date = {'d': d, 'm': mo, 'y': y}
        
        if ble_connected != last_ble:
            mostrar_status_ble()
            last_ble = ble_connected
        
        if wifi_status != last_wifi_status:
            mostrar_status_wifi()
            last_wifi_status = wifi_status
        
        eventos_atuais = []
        for evt in events[:3]:
            eventos_atuais.append({
                'nome': evt.get('nome', ''),
                'hora': evt.get('hora', '')
            })
        
        if eventos_atuais != last_events_display:
            fill_rect(10, 180, 460, 100, BLACK)
            
            if eventos_atuais:
                draw_centered(185, "EVENTOS", CYAN, 2)
                
                y_inicial = 210
                altura_linha = 25
                
                for i, evt in enumerate(eventos_atuais):
                    nome = evt['nome']
                    hora = evt['hora']
                    
                    if nome and hora:
                        y_pos = y_inicial + (i * altura_linha)
                        max_chars = 30
                        nome_display = nome[:max_chars]
                        linha_texto = hora + " " + nome_display
                        draw_text(15, y_pos, linha_texto, WHITE, 1)
            
            last_events_display = eventos_atuais[:]
    except:
        pass

# === INICIALIZACAO ===
print("Iniciando LCD...")
init_lcd()

fill_rect(0, 0, 480, 320, BLACK)
draw_centered(100, "MAGIC MIRROR", WHITE, 3)
utime.sleep(1)

print("Verificando WiFi...")
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

if wlan.isconnected():
    print("WiFi ja conectado!")
    wifi_status = True
    modo_offline = False
    sincronizar_horario_ntp()
else:
    print("WiFi nao conectado")
    conectar_wifi()

events = []
if wifi_status:
    buscar_eventos_servidor()

ble_handler = BLE()

fill_rect(0, 0, 480, 320, BLACK)
draw_text(160, 80, ":", WHITE, 4)
draw_text(280, 80, ":", WHITE, 4)

mostrar_status_ble()
mostrar_status_wifi()

print("SISTEMA PRONTO")

# === LOOP PRINCIPAL ===
loop_count = 0

while True:
    try:
        if loop_count % 50 == 0:
            verificar_status_wifi()
        
        update_display()
        
        loop_count += 1
        
        if loop_count % 1500 == 0 and modo_offline:
            conectar_wifi()
        
        utime.sleep_ms(200)
        
        if loop_count % 600 == 0:
            gc.collect()
            
    except KeyboardInterrupt:
        break
    except:
        utime.sleep(1)

print("Finalizado")
