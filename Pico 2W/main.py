#!/usr/bin/env python3
"""
Magic Mirror - Main com Display LCD Funcional
Sistema completo com relógio, data e eventos do calendário
"""

import machine
import utime
import json
import network
import ntptime
import gc
from machine import Pin, RTC

# Importar configurações e fonte
from config import *
from font import get_char_bitmap, get_text_width, center_text_x, normalize_text

try:
    from umqtt.simple import MQTTClient
    MQTT_AVAILABLE = True
except ImportError:
    MQTT_AVAILABLE = False
    print("AVISO: MQTT não disponível")

# ==================== CONFIGURAÇÕES LCD DISPLAY ====================
# Pinos do display shield (baseado no hardware disponível)
rst = Pin(16, Pin.OUT, value=1)
cs = Pin(17, Pin.OUT, value=1) 
rs = Pin(15, Pin.OUT, value=0)
wr = Pin(19, Pin.OUT, value=1)
rd = Pin(18, Pin.OUT, value=1)
data_pins = [Pin(i, Pin.OUT) for i in [0,1,2,3,4,5,6,7]]

# Cores RGB565
BLACK = 0x0000
WHITE = 0xFFFF
RED = 0xF800
GREEN = 0x07E0
BLUE = 0x001F
CYAN = 0x07FF
YELLOW = 0xFFE0
MAGENTA = 0xF81F

# RTC para controle de tempo
rtc = RTC()

# ==================== FUNÇÕES DO DISPLAY ====================
def write_byte(data):
    """Escreve um byte nos pinos de dados"""
    for i in range(8):
        data_pins[i].value((data >> i) & 1)

def cmd(c):
    """Envia comando para o display"""
    cs.value(0)
    rs.value(0)
    write_byte(c)
    wr.value(0)
    wr.value(1)
    cs.value(1)

def dat(d):
    """Envia dados para o display"""
    cs.value(0)
    rs.value(1)
    write_byte(d)
    wr.value(0)
    wr.value(1)
    cs.value(1)

def init_lcd():
    """Inicializa o display LCD"""
    print("Inicializando LCD...")
    rst.value(0)
    utime.sleep_ms(50)
    rst.value(1)
    utime.sleep_ms(50)
    
    # Sequência de inicialização do display
    cmd(0x01)  # Software reset
    utime.sleep_ms(100)
    cmd(0x11)  # Sleep out
    utime.sleep_ms(100)
    cmd(0x3A)  # Pixel format
    dat(0x55)  # 16-bit RGB565
    cmd(0x36)  # Memory access control
    dat(0xE8)  # Orientation
    cmd(0x29)  # Display on
    utime.sleep_ms(50)
    print("LCD inicializado com sucesso")

def set_area(x0, y0, x1, y1):
    """Define área de desenho no display"""
    cmd(0x2A)  # Column address
    dat(x0>>8)
    dat(x0&0xFF)
    dat(x1>>8)
    dat(x1&0xFF)
    cmd(0x2B)  # Row address
    dat(y0>>8)
    dat(y0&0xFF)
    dat(y1>>8)
    dat(y1&0xFF)
    cmd(0x2C)  # Memory write

def fill_rect(x, y, w, h, color):
    """Preenche retângulo com cor"""
    if w <= 0 or h <= 0:
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
    except Exception as e:
        if is_debug():
            print(f"Erro fill_rect: {e}")

def draw_char(x, y, char, color, size):
    """Desenha um caractere usando a fonte bitmap"""
    try:
        bitmap = get_char_bitmap(char)
        for row in range(8):
            byte = bitmap[row]
            for col in range(8):
                if byte & (0x80 >> col):
                    fill_rect(x + col*size, y + row*size, size, size, color)
    except Exception as e:
        if is_debug():
            print(f"Erro draw_char '{char}': {e}")

def draw_text(x, y, text, color, size):
    """Desenha texto na tela"""
    try:
        normalized_text = normalize_text(text)
        char_spacing = size * 10  # 8 pixels da fonte + 2 de espaçamento
        
        for i, char in enumerate(normalized_text):
            char_x = x + i * char_spacing
            if char_x < DISPLAY_WIDTH:  # Verificar limites da tela
                draw_char(char_x, y, char, color, size)
    except Exception as e:
        if is_debug():
            print(f"Erro draw_text: {e}")

def draw_centered(y, text, color, size):
    """Desenha texto centralizado horizontalmente"""
    try:
        x = center_text_x(text, DISPLAY_WIDTH, size)
        draw_text(x, y, text, color, size)
    except Exception as e:
        if is_debug():
            print(f"Erro draw_centered: {e}")

def format_time(h, m, s):
    """Formata tempo como HH:MM:SS"""
    return f"{h:02d}:{m:02d}:{s:02d}"

def format_date(d, m, y):
    """Formata data como DD/MM/AAAA"""
    return f"{d:02d}/{m:02d}/{y}"

# ==================== CLASSE DISPLAY ====================
class Display:
    def __init__(self):
        self.last_time = {'h': -1, 'm': -1, 's': -1}
        self.last_date = {'d': -1, 'm': -1, 'y': -1}
        self.last_events = []
        self.initialized = False
        
        try:
            init_lcd()
            self.clear()
            self.show_startup()
            self.initialized = True
        except Exception as e:
            print(f"Erro inicialização display: {e}")
    
    def clear(self):
        """Limpa a tela completamente"""
        try:
            fill_rect(0, 0, DISPLAY_WIDTH, DISPLAY_HEIGHT, BLACK)
            if is_debug():
                print("Display limpo")
        except Exception as e:
            print(f"Erro clear: {e}")
    
    def show_startup(self):
        """Mostra tela de inicialização"""
        try:
            self.clear()
            draw_centered(80, "MAGIC MIRROR", WHITE, 3)
            draw_centered(120, f"ID: {REGISTRATION_ID}", CYAN, 2)
            draw_centered(150, "Inicializando...", GREEN, 2)
            utime.sleep(3)
            if is_debug():
                print("Tela de startup exibida")
        except Exception as e:
            print(f"Erro show_startup: {e}")
    
    def show_status(self, status):
        """Mostra status na parte inferior"""
        try:
            # Limpar área de status
            fill_rect(0, 280, DISPLAY_WIDTH, 40, BLACK)
            draw_centered(285, f"Status: {status}", YELLOW, 1)
            if is_debug():
                print(f"Status atualizado: {status}")
        except Exception as e:
            print(f"Erro show_status: {e}")
    
    def update_clock(self):
        """Atualiza relógio na tela - otimizado para atualizar apenas partes modificadas"""
        if not self.initialized:
            return
        
        try:
            t = rtc.datetime()
            h, m, s = t[4], t[5], t[6]
            d, mo, y = t[2], t[1], t[0]
            
            # Posições fixas do relógio
            clock_y = 40
            date_y = 100
            
            # Atualizar horas se mudou
            if h != self.last_time['h']:
                fill_rect(160, clock_y, 50, 32, BLACK)  # Limpar área das horas
                draw_text(160, clock_y, f"{h:02d}", WHITE, 4)
                self.last_time['h'] = h
            
            # Atualizar minutos se mudou  
            if m != self.last_time['m']:
                fill_rect(240, clock_y, 50, 32, BLACK)  # Limpar área dos minutos
                draw_text(240, clock_y, f"{m:02d}", WHITE, 4)
                self.last_time['m'] = m
            
            # Atualizar segundos se mudou
            if s != self.last_time['s']:
                fill_rect(320, clock_y, 50, 32, BLACK)  # Limpar área dos segundos
                draw_text(320, clock_y, f"{s:02d}", WHITE, 4)
                self.last_time['s'] = s
            
            # Desenhar separadores : (sempre visíveis)
            if self.last_time['h'] == -1:  # Primeira vez
                draw_text(220, clock_y, ":", WHITE, 4)
                draw_text(300, clock_y, ":", WHITE, 4)
            
            # Atualizar data se mudou
            if d != self.last_date['d'] or mo != self.last_date['m'] or y != self.last_date['y']:
                fill_rect(0, date_y, DISPLAY_WIDTH, 25, BLACK)  # Limpar área da data
                date_str = format_date(d, mo, y)
                draw_centered(date_y, date_str, CYAN, 2)
                self.last_date = {'d': d, 'm': mo, 'y': y}
                
        except Exception as e:
            if is_debug():
                print(f"Erro update_clock: {e}")
    
    def show_events(self, events):
        """Mostra eventos do calendário"""
        try:
            if not self.initialized:
                return
                
            # Verificar se eventos mudaram para evitar redesenhos desnecessários
            if events == self.last_events:
                return
            
            # Área de eventos (parte inferior da tela)
            events_y_start = 140
            events_height = 120
            
            # Limpar área de eventos
            fill_rect(0, events_y_start, DISPLAY_WIDTH, events_height, BLACK)
            
            if not events:
                draw_centered(events_y_start + 20, "Nenhum evento hoje", GREEN, 2)
            else:
                # Título da seção
                draw_centered(events_y_start, "EVENTOS HOJE", MAGENTA, 2)
                
                # Mostrar até 4 eventos
                y_pos = events_y_start + 30
                line_height = 20
                
                for i, event in enumerate(events[:4]):
                    if y_pos + line_height > DISPLAY_HEIGHT - 40:  # Deixar espaço para status
                        break
                    
                    # Extrair informações do evento
                    title = event.get('title', event.get('nome', 'Evento'))
                    time = event.get('time', event.get('hora', '--:--'))
                    
                    if title and time:
                        # Truncar título se muito longo (considerando tamanho da fonte)
                        max_chars = 35  # Aproximadamente para fonte tamanho 1
                        title_display = title[:max_chars] + '...' if len(title) > max_chars else title
                        
                        # Montar linha do evento
                        event_line = f"{time} - {title_display}"
                        
                        # Desenhar evento (alinhado à esquerda com pequena margem)
                        draw_text(10, y_pos, event_line, WHITE, 1)
                        y_pos += line_height
            
            self.last_events = events.copy()  # Salvar cópia dos eventos
            if is_debug():
                print(f"Eventos atualizados na tela: {len(events)}")
                
        except Exception as e:
            print(f"Erro show_events: {e}")
    
    def setup_main_screen(self):
        """Configura layout da tela principal"""
        try:
            self.clear()
            
            # Desenhar elementos fixos
            draw_text(220, 40, ":", WHITE, 4)  # Separador horas:minutos
            draw_text(300, 40, ":", WHITE, 4)  # Separador minutos:segundos
            
            # Reset dos valores para forçar atualização completa
            self.last_time = {'h': -1, 'm': -1, 's': -1}
            self.last_date = {'d': -1, 'm': -1, 'y': -1}
            self.last_events = []
            
            if is_debug():
                print("Tela principal configurada")
        except Exception as e:
            print(f"Erro setup_main_screen: {e}")

# ==================== CONECTIVIDADE WIFI ====================
class WiFi:
    def __init__(self):
        self.wlan = network.WLAN(network.STA_IF)
        self.connected = False
    
    def connect(self):
        """Conecta à rede WiFi"""
        try:
            self.wlan.active(True)
            
            # Verificar se já está conectado
            if self.wlan.isconnected():
                ip = self.wlan.ifconfig()[0]
                print(f"WiFi já conectado: {ip}")
                self.connected = True
                return True
            
            print(f"Conectando WiFi: {WIFI_SSID}")
            
            # Tentar conectar múltiplas vezes
            for attempt in range(MAX_RETRY_ATTEMPTS):
                try:
                    self.wlan.connect(WIFI_SSID, WIFI_PASSWORD)
                    
                    # Aguardar conexão
                    timeout = 0
                    while not self.wlan.isconnected() and timeout < CONNECTION_TIMEOUT:
                        utime.sleep(1)
                        timeout += 1
                        if timeout % 5 == 0:
                            print(f"Conectando... {timeout}s")
                    
                    if self.wlan.isconnected():
                        ip = self.wlan.ifconfig()[0]
                        print(f"WiFi conectado com sucesso: {ip}")
                        self.connected = True
                        
                        # Sincronizar horário automaticamente após conectar
                        if self.sync_ntp():
                            print("Horário sincronizado via NTP")
                        
                        return True
                    else:
                        print(f"Tentativa {attempt + 1} falhou")
                        
                except Exception as e:
                    print(f"Erro na tentativa {attempt + 1}: {e}")
            
            print("Falha na conexão WiFi após todas as tentativas")
            return False
            
        except Exception as e:
            print(f"Erro crítico WiFi: {e}")
            return False
    
    def sync_ntp(self):
        """Sincroniza horário via NTP com servidor brasileiro"""
        if not self.connected:
            return False
        
        try:
            print("Sincronizando horário via NTP...")
            
            # Tentar sincronizar algumas vezes
            for attempt in range(3):
                try:
                    ntptime.settime()
                    
                    # Ajustar para fuso horário brasileiro (UTC-3)
                    timestamp_utc = utime.time()
                    timestamp_br = timestamp_utc + (TIMEZONE_OFFSET * 3600)  # TIMEZONE_OFFSET já é negativo
                    br_time = utime.localtime(timestamp_br)
                    
                    # Configurar RTC com horário local
                    rtc.datetime((br_time[0], br_time[1], br_time[2], 
                                 br_time[6], br_time[3], br_time[4], 
                                 br_time[5], 0))
                    
                    # Verificar se funcionou
                    current = rtc.datetime()
                    print(f"Horário sincronizado: {current[2]:02d}/{current[1]:02d}/{current[0]} {current[4]:02d}:{current[5]:02d}:{current[6]:02d}")
                    return True
                    
                except Exception as e:
                    print(f"Tentativa NTP {attempt + 1} falhou: {e}")
                    if attempt < 2:
                        utime.sleep(2)
            
            return False
            
        except Exception as e:
            print(f"Erro sincronização NTP: {e}")
            return False
    
    def is_connected(self):
        """Verifica se ainda está conectado"""
        try:
            self.connected = self.wlan.isconnected()
            return self.connected
        except:
            self.connected = False
            return False

# ==================== MQTT PARA EVENTOS ====================
class MQTTHandler:
    def __init__(self, display):
        self.display = display
        self.client = None
        self.connected = False
        self.registered = False
        self.device_id = None
        self.topic_prefix = None
        
    def connect(self):
        """Conecta ao broker MQTT público"""
        if not MQTT_AVAILABLE:
            print("MQTT não disponível - continuando sem eventos remotos")
            return False
        
        try:
            client_id = f"mirror_{machine.unique_id().hex()[:8]}"
            self.client = MQTTClient(client_id, MQTT_BROKER, port=MQTT_PORT)
            self.client.set_callback(self.on_message)
            self.client.connect()
            
            self.connected = True
            print(f"MQTT conectado: {MQTT_BROKER}")
            
            # Iniciar processo de descoberta do servidor
            self.discover_server()
            return True
            
        except Exception as e:
            print(f"Erro conexão MQTT: {e}")
            return False
    
    def discover_server(self):
        """Envia descoberta para encontrar servidor backend"""
        if not self.connected:
            return
        
        try:
            discovery_data = {
                'action': 'discover',
                'registration_id': REGISTRATION_ID,
                'timestamp': utime.time(),
                'firmware': FIRMWARE_VERSION
            }
            
            discovery_topic = f"magic_mirror/discovery/{REGISTRATION_ID}"
            self.client.publish(discovery_topic, json.dumps(discovery_data))
            self.client.subscribe(f"magic_mirror/discovery/{REGISTRATION_ID}/response")
            print("Descoberta de servidor enviada")
            
        except Exception as e:
            print(f"Erro descoberta: {e}")
    
    def on_message(self, client, userdata, msg):
        """Processa mensagens recebidas via MQTT"""
        try:
            topic = msg.topic.decode()
            payload = json.loads(msg.payload.decode())
            
            if is_debug():
                print(f"MQTT recebido - Tópico: {topic}")
            
            if "/discovery/" in topic and topic.endswith("/response"):
                self.handle_discovery_response(payload)
            elif topic.endswith("/events"):
                self.handle_events(payload)
            elif topic.endswith("/registration"):
                self.handle_registration(payload)
                
        except Exception as e:
            print(f"Erro processar mensagem MQTT: {e}")
    
    def handle_discovery_response(self, payload):
        """Processa resposta de descoberta do servidor"""
        try:
            if payload.get('registration_id') != REGISTRATION_ID:
                return
            
            self.topic_prefix = payload.get('topic_prefix')
            if self.topic_prefix:
                print(f"Servidor encontrado - Prefix: {self.topic_prefix}")
                
                # Inscrever-se no tópico de registro
                self.client.subscribe(f"{self.topic_prefix}/registration")
                
                # Enviar registro
                self.send_registration()
                
        except Exception as e:
            print(f"Erro discovery response: {e}")
    
    def send_registration(self):
        """Envia registro do dispositivo"""
        if not self.connected or not self.topic_prefix:
            return
        
        try:
            registration_data = {
                'registration_id': REGISTRATION_ID,
                'firmware_version': FIRMWARE_VERSION,
                'timestamp': utime.time(),
                'capabilities': ['clock', 'calendar', 'display_lcd']
            }
            
            topic = f"{self.topic_prefix}/registration"
            self.client.publish(topic, json.dumps(registration_data))
            print("Registro enviado para servidor")
            
        except Exception as e:
            print(f"Erro enviar registro: {e}")
    
    def handle_registration(self, payload):
        """Processa resposta de registro"""
        try:
            if payload.get('registration_id') != REGISTRATION_ID:
                return
            
            status = payload.get('status')
            
            if status == 'approved':
                self.device_id = payload.get('device_id')
                self.registered = True
                
                # Inscrever-se no tópico de eventos
                if self.device_id:
                    events_topic = f"{self.topic_prefix}/devices/{self.device_id}/events"
                    self.client.subscribe(events_topic)
                
                print(f"Dispositivo aprovado - ID: {self.device_id}")
                self.display.show_status("Conectado - Eventos ativos")
                
            elif status == 'pending':
                print("Registro pendente - aguardando aprovação")
                self.display.show_status("Aguardando aprovação")
            else:
                print(f"Registro rejeitado: {status}")
                self.display.show_status("Registro rejeitado")
                
        except Exception as e:
            print(f"Erro handle registration: {e}")
    
    def handle_events(self, payload):
        """Processa eventos recebidos do calendário"""
        try:
            events = payload.get('events', [])
            print(f"Eventos recebidos: {len(events)}")
            
            if is_debug():
                for event in events[:3]:  # Mostrar apenas primeiros 3 no debug
                    title = event.get('title', 'Sem título')
                    time = event.get('time', 'Sem horário')
                    print(f"  - {time}: {title}")
            
            # Atualizar display com eventos
            self.display.show_events(events)
            
        except Exception as e:
            print(f"Erro processar eventos: {e}")
    
    def check_messages(self):
        """Verifica mensagens MQTT pendentes"""
        if self.connected and self.client:
            try:
                self.client.check_msg()
                return True
            except Exception as e:
                print(f"Erro check MQTT messages: {e}")
                self.connected = False
                return False
        return False

# ==================== APLICAÇÃO PRINCIPAL ====================
class MagicMirror:
    def __init__(self):
        print("=" * 50)
        print("MAGIC MIRROR - Sistema Iniciando")
        print("=" * 50)
        
        # Validar configuração antes de continuar
        config_issues = validate_config()
        if config_issues:
            print("ERROS DE CONFIGURAÇÃO:")
            for issue in config_issues:
                print(f"  ❌ {issue}")
            print("\nConfigure o arquivo config.py e reinicie!")
            return
        
        print("✅ Configuração válida")
        
        # Inicializar componentes
        self.display = None
        self.wifi = None
        self.mqtt = None
        self.running = True
        
        # Inicializar display
        print("Inicializando display...")
        self.display = Display()
        
        if not self.display.initialized:
            print("❌ Falha na inicialização do display")
            return
        
        print("✅ Display inicializado")
        
        # Inicializar WiFi
        print("Inicializando WiFi...")
        self.wifi = WiFi()
    
    def run(self):
        """Executa o loop principal da aplicação"""
        if not self.display or not self.display.initialized:
            print("❌ Display não inicializado - abortando")
            return
        
        # Conectar WiFi
        self.display.show_status("Conectando WiFi...")
        if not self.wifi.connect():
            self.display.show_status("ERRO: WiFi falhou")
            print("❌ Falha na conexão WiFi")
            return
        
        print("✅ WiFi conectado")
        
        # Conectar MQTT (opcional)
        self.display.show_status("Conectando MQTT...")
        self.mqtt = MQTTHandler(self.display)
        
        if self.mqtt.connect():
            print("✅ MQTT conectado")
            self.display.show_status("MQTT conectado")
        else:
            print("⚠️  MQTT falhou - continuando sem eventos remotos")
            self.display.show_status("Sem MQTT - Somente relógio")
        
        # Aguardar um pouco e configurar tela principal
        utime.sleep(3)
        self.display.setup_main_screen()
        self.display.show_status("Sistema ativo")
        
        print("🚀 Sistema iniciado - entrando no loop principal")
        
        # Variáveis de controle do loop
        loop_count = 0
        last_ntp_sync = 0
        last_mqtt_retry = 0
        discovery_attempts = 0
        
        # Loop principal
        while self.running:
            try:
                current_time = utime.time()
                
                # ===== ATUALIZAR RELÓGIO (sempre) =====
                self.display.update_clock()
                
                # ===== VERIFICAR CONEXÃO WIFI =====
                if not self.wifi.is_connected():
                    print("⚠️  WiFi desconectado - tentando reconectar")
                    self.display.show_status("Reconectando WiFi...")
                    if self.wifi.connect():
                        print("✅ WiFi reconectado")
                    else:
                        print("❌ Falha na reconexão WiFi")
                
                # ===== SINCRONIZAÇÃO NTP (a cada hora) =====
                if self.wifi.is_connected() and (current_time - last_ntp_sync) > 3600:  # 1 hora
                    print("🕐 Ressincronizando horário...")
                    if self.wifi.sync_ntp():
                        last_ntp_sync = current_time
                        print("✅ Horário ressincronizado")
                    else:
                        print("⚠️  Falha na ressincronização")
                
                # ===== GERENCIAMENTO MQTT =====
                if MQTT_AVAILABLE and self.mqtt:
                    # Verificar mensagens se conectado
                    if self.mqtt.connected:
                        if not self.mqtt.check_messages():
                            print("⚠️  MQTT desconectado")
                            self.mqtt.connected = False
                    
                    # Tentar reconectar se desconectado
                    elif (current_time - last_mqtt_retry) > 60:  # Tentar a cada minuto
                        print("🔄 Tentando reconectar MQTT...")
                        if self.mqtt.connect():
                            print("✅ MQTT reconectado")
                        last_mqtt_retry = current_time
                    
                    # Processo de descoberta se ainda não registrado
                    if self.mqtt.connected and not self.mqtt.topic_prefix:
                        if (current_time - last_mqtt_retry) > 30 and discovery_attempts < 10:
                            print(f"🔍 Descoberta #{discovery_attempts + 1}")
                            self.mqtt.discover_server()
                            discovery_attempts += 1
                            last_mqtt_retry = current_time
                
                # ===== MANUTENÇÃO DO SISTEMA =====
                loop_count += 1
                
                # Coleta de lixo a cada 5 minutos (300 loops de 1 segundo)
                if loop_count % 300 == 0:
                    gc.collect()
                    if is_debug():
                        print(f"🧹 Limpeza de memória - Loop #{loop_count}")
                
                # Status de debug a cada 10 minutos
                if is_debug() and loop_count % 600 == 0:
                    mem_free = gc.mem_free()
                    wifi_status = "Conectado" if self.wifi.is_connected() else "Desconectado"
                    mqtt_status = "Conectado" if (self.mqtt and self.mqtt.connected) else "Desconectado"
                    print(f"📊 Status - Memória: {mem_free} | WiFi: {wifi_status} | MQTT: {mqtt_status}")
                
                # Aguardar 1 segundo antes da próxima iteração
                utime.sleep(1)
                
            except KeyboardInterrupt:
                print("\n🛑 Interrupção pelo usuário - parando sistema")
                self.running = False
                break
                
            except Exception as e:
                print(f"❌ Erro no loop principal: {e}")
                # Mostrar erro na tela por alguns segundos
                self.display.show_status(f"ERRO: {str(e)[:20]}")
                utime.sleep(5)
                
                # Se muitos erros seguidos, reiniciar
                if loop_count % 10 == 0:  # A cada 10 erros
                    print("⚠️  Muitos erros - considerando reinicialização")
        
        # ===== LIMPEZA E ENCERRAMENTO =====
        print("🔄 Encerrando sistema...")
        
        if self.mqtt and self.mqtt.connected:
            try:
                # Enviar mensagem de desconexão se possível
                if self.mqtt.topic_prefix and self.mqtt.device_id:
                    disconnect_msg = {
                        'action': 'disconnect',
                        'device_id': self.mqtt.device_id,
                        'timestamp': utime.time()
                    }
                    topic = f"{self.mqtt.topic_prefix}/devices/{self.mqtt.device_id}/status"
                    self.mqtt.client.publish(topic, json.dumps(disconnect_msg))
                
                self.mqtt.client.disconnect()
                print("✅ MQTT desconectado")
            except:
                pass
        
        if self.wifi and self.wifi.connected:
            try:
                self.wifi.wlan.disconnect()
                self.wifi.wlan.active(False)
                print("✅ WiFi desconectado")
            except:
                pass
        
        # Mostrar tela de encerramento
        if self.display and self.display.initialized:
            try:
                self.display.clear()
                draw_centered(100, "SISTEMA", WHITE, 3)
                draw_centered(140, "ENCERRADO", WHITE, 3)
                draw_centered(180, "Obrigado!", CYAN, 2)
                utime.sleep(2)
                self.display.clear()
            except:
                pass
        
        print("👋 Sistema encerrado")

def main():
    """Função principal - ponto de entrada"""
    try:
        # Banner de inicialização
        print("\n" + "=" * 60)
        print("🪞 MAGIC MIRROR - DISPLAY LCD")
        print("=" * 60)
        print(f"📱 Registration ID: {REGISTRATION_ID}")
        print(f"🌐 WiFi Network: {WIFI_SSID}")
        print(f"🖥️  Display: {DISPLAY_WIDTH}x{DISPLAY_HEIGHT}")
        print(f"🔧 Firmware: {FIRMWARE_VERSION}")
        print("=" * 60)
        
        # Criar e executar aplicação
        app = MagicMirror()
        
        # Verificar se inicialização foi bem-sucedida
        if not hasattr(app, 'display') or not app.display or not app.display.initialized:
            print("❌ FALHA CRÍTICA: Display não inicializado")
            print("Verifique as conexões de hardware e reinicie")
            return
        
        if not hasattr(app, 'wifi') or not app.wifi:
            print("❌ FALHA CRÍTICA: WiFi não inicializado")
            print("Verifique as configurações de rede no config.py")
            return
        
        # Executar aplicação principal
        app.run()
        
    except Exception as e:
        print(f"💥 ERRO CRÍTICO: {e}")
        print("Sistema será reiniciado em 10 segundos...")
        
        try:
            # Tentar mostrar erro na tela se possível
            if 'app' in locals() and app.display and app.display.initialized:
                app.display.clear()
                draw_centered(80, "ERRO CRITICO", RED, 2)
                draw_centered(110, str(e)[:25], WHITE, 1)
                draw_centered(140, "Reiniciando...", YELLOW, 2)
        except:
            pass
        
        utime.sleep(10)
        machine.reset()  # Reinicialização automática

# ==================== FUNÇÕES DE TESTE ====================
def test_display():
    """Função de teste do display - útil para debug"""
    print("🧪 TESTE DO DISPLAY")
    print("-" * 30)
    
    try:
        init_lcd()
        
        # Teste 1: Cores básicas
        print("Testando cores...")
        colors = [RED, GREEN, BLUE, CYAN, MAGENTA, YELLOW, WHITE]
        for i, color in enumerate(colors):
            fill_rect(i*60, 0, 60, 40, color)
        
        utime.sleep(2)
        
        # Teste 2: Texto
        print("Testando texto...")
        fill_rect(0, 0, DISPLAY_WIDTH, DISPLAY_HEIGHT, BLACK)
        
        draw_centered(50, "TESTE DISPLAY", WHITE, 3)
        draw_centered(100, "Magic Mirror", CYAN, 2)
        draw_centered(130, "Fonte bitmap funcionando!", GREEN, 1)
        
        # Teste 3: Relógio fictício
        draw_text(150, 180, "12:34:56", WHITE, 4)
        draw_text(150, 220, "25/12/2024", YELLOW, 2)
        
        print("✅ Teste concluído - verifique a tela")
        return True
        
    except Exception as e:
        print(f"❌ Erro no teste: {e}")
        return False

def test_font():
    """Teste das fontes bitmap"""
    print("🔤 TESTE DAS FONTES")
    print("-" * 30)
    
    test_strings = [
        "0123456789",
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ", 
        "abcdefghijklmnopqrstuvwxyz",
        "!@#$%^&*()_+-=[]{}|;:,.<>?",
        "ãáçéêíóôõúÃÁÇÉÊÍÓÔÕÚ",
        "Magic Mirror 2024!"
    ]
    
    for text in test_strings:
        normalized = normalize_text(text)
        width = get_text_width(text, 1)
        print(f"Texto: '{text}'")
        print(f"Normalizado: '{normalized}'")
        print(f"Largura: {width}px")
        print("-" * 20)
    
    print("✅ Teste de fonte concluído")

# ==================== MODO DEMO ====================
def demo_mode():
    """Modo demonstração - exibe funcionalidades sem conectividade"""
    print("🎯 MODO DEMONSTRAÇÃO")
    print("-" * 30)
    
    try:
        # Inicializar apenas o display
        display = Display()
        
        if not display.initialized:
            print("❌ Falha na inicialização do display para demo")
            return
        
        # Configurar horário fictício no RTC para demonstração
        # 25/12/2024 15:30:00
        rtc.datetime((2024, 12, 25, 3, 15, 30, 0, 0))  # 3=Quarta-feira
        
        print("🎬 Iniciando demonstração...")
        display.setup_main_screen()
        
        # Eventos fictícios para demonstração
        demo_events = [
            {"title": "Reunião de equipe", "time": "09:00"},
            {"title": "Almoço com cliente", "time": "12:30"},
            {"title": "Apresentação projeto", "time": "15:00"},
            {"title": "Call internacional", "time": "17:30"}
        ]
        
        display.show_events(demo_events)
        display.show_status("MODO DEMO - Sem conectividade")
        
        # Loop de demonstração por 5 minutos
        start_time = utime.time()
        demo_duration = 300  # 5 minutos
        
        print(f"⏰ Demo rodando por {demo_duration//60} minutos...")
        
        while (utime.time() - start_time) < demo_duration:
            display.update_clock()
            
            # Simular mudança de eventos a cada 30 segundos
            if (utime.time() - start_time) % 30 == 0:
                import random
                random.shuffle(demo_events)
                display.show_events(demo_events[:3])
            
            utime.sleep(1)
        
        print("✅ Demonstração concluída")
        display.clear()
        draw_centered(160, "FIM DA DEMO", WHITE, 3)
        utime.sleep(3)
        display.clear()
        
    except Exception as e:
        print(f"❌ Erro no modo demo: {e}")

# ==================== PONTO DE ENTRADA ====================
if __name__ == "__main__":
    # Verificar se há argumentos especiais para modos de teste
    import sys
    
    # No MicroPython, sys.argv pode não estar disponível
    try:
        args = sys.argv if hasattr(sys, 'argv') else []
    except:
        args = []
    
    # Modos especiais (se suportado pelo sistema)
    if "test" in str(args):
        test_display()
    elif "font" in str(args):
        test_font() 
    elif "demo" in str(args):
        demo_mode()
    else:
        # Execução normal
        main()