# config.py - Magic Mirror com MQTT Público
"""
Configuração completa para Magic Mirror com display LCD
Sistema otimizado para funcionamento com ou sem MQTT
"""

# ==================== IDENTIFICAÇÃO ÚNICA ====================
# IMPORTANTE: Altere este ID para um valor único para seu dispositivo
REGISTRATION_ID = "MIRROR_CASA_001"  # ⚠️ ALTERE AQUI - Deve ser único!

# ==================== CONFIGURAÇÃO DE REDE ====================
# IMPORTANTE: Configure sua rede WiFi aqui
WIFI_SSID = "MinhaRedeWiFi"         # ⚠️ ALTERE AQUI
WIFI_PASSWORD = "MinhaSenha123"     # ⚠️ ALTERE AQUI

# ==================== CONFIGURAÇÃO MQTT (OPCIONAL) ====================
# Broker MQTT público para comunicação com servidor de eventos
MQTT_BROKER = "test.mosquitto.org"  # Broker público gratuito
MQTT_PORT = 1883
TOPIC_PREFIX = ""  # Será definido automaticamente pelo backend

# Alternativos de brokers públicos (caso o principal falhe):
MQTT_BACKUP_BROKERS = [
    "broker.hivemq.com",
    "mqtt.eclipseprojects.io", 
    "broker.emqx.io"
]

# ==================== CONFIGURAÇÃO DO DISPLAY ====================
# Configurações do display LCD
DISPLAY_WIDTH = 480
DISPLAY_HEIGHT = 320
DISPLAY_BRIGHTNESS = 80  # 0-100

# Pinos do display (baseado no hardware shield)
DISPLAY_PINS = {
    'RST': 16,    # Reset
    'CS': 17,     # Chip Select  
    'RS': 15,     # Register Select (DC)
    'WR': 19,     # Write
    'RD': 18,     # Read
    'DATA': [0,1,2,3,4,5,6,7]  # Pinos de dados D0-D7
}

# ==================== CONFIGURAÇÃO DE TEMPO ====================
# Fuso horário brasileiro (UTC-3)
TIMEZONE_OFFSET = -3

# Formato de tempo
TIME_FORMAT = "24H"  # "24H" ou "12H"

# Servidores NTP para sincronização (servidores brasileiros preferenciais)
NTP_SERVERS = [
    "pool.ntp.br",
    "a.ntp.br", 
    "b.ntp.br",
    "time.google.com",
    "pool.ntp.org"
]

# ==================== CONFIGURAÇÃO DE EVENTOS ====================
# Máximo de eventos a exibir na tela
MAX_EVENTS_DISPLAY = 4

# Intervalo de atualização de eventos (em segundos)
EVENTS_UPDATE_INTERVAL = 300  # 5 minutos

# Filtros de eventos (opcionais)
EVENT_FILTERS = {
    'min_duration': 15,  # Eventos com menos de 15 minutos são ignorados
    'keywords_exclude': ['spam', 'teste'],  # Palavras a ignorar
    'time_range': {
        'start': '06:00',  # Mostrar eventos apenas após 6h
        'end': '23:59'     # Mostrar eventos até 23:59
    }
}

# ==================== CONFIGURAÇÃO DE CONEXÃO ====================
# Timeout para conexão WiFi (segundos)
CONNECTION_TIMEOUT = 30

# Número máximo de tentativas de reconexão
MAX_RETRY_ATTEMPTS = 5

# Intervalo entre tentativas (segundos)
RETRY_INTERVAL = 10

# ==================== CONFIGURAÇÃO DE DEBUG ====================
# Habilitar mensagens de debug
DEBUG_ENABLED = True

# Nível de debug (1=básico, 2=médio, 3=detalhado)
DEBUG_LEVEL = 2

# Log de debug para arquivo (se suportado)
DEBUG_TO_FILE = False
DEBUG_FILE_PATH = "/debug.log"

# ==================== INFORMAÇÕES DO FIRMWARE ====================
FIRMWARE_VERSION = "2.0.1"
FIRMWARE_BUILD = "2024.12.25"
HARDWARE_VERSION = "LCD_SHIELD_V1"

# Capacidades do dispositivo
DEVICE_CAPABILITIES = [
    'clock',           # Relógio em tempo real
    'calendar',        # Eventos de calendário
    'display_lcd',     # Display LCD colorido
    'wifi',           # Conectividade WiFi
    'mqtt',           # Comunicação MQTT
    'ntp_sync',       # Sincronização via NTP
    'bitmap_font'     # Fontes bitmap customizadas
]

# ==================== CONFIGURAÇÕES DE ECONOMIA DE ENERGIA ====================
# Habilitar modo de economia (reduz brilho à noite)
POWER_SAVE_ENABLED = True

# Horários do modo econômico
POWER_SAVE_HOURS = {
    'start': '23:00',  # Iniciar economia às 23h
    'end': '06:00',    # Terminar economia às 6h
    'brightness': 30   # Reduzir brilho para 30%
}

# Suspender WiFi/MQTT durante economia (mais economia, menos funcionalidades)
POWER_SAVE_DISABLE_NETWORK = False

# ==================== PERSONALIZAÇÃO DA INTERFACE ====================
# Cores principais (RGB565)
COLORS = {
    'background': 0x0000,  # Preto
    'time': 0xFFFF,        # Branco
    'date': 0x07FF,        # Cyan
    'events': 0xFFFF,      # Branco
    'status': 0xFFE0,      # Amarelo
    'error': 0xF800,       # Vermelho
    'success': 0x07E0,     # Verde
    'warning': 0xFD20      # Laranja
}

# Posições dos elementos na tela
LAYOUT = {
    'clock': {
        'x': 160, 'y': 40,
        'size': 4,
        'color': 'time'
    },
    'date': {
        'y': 100,
        'size': 2, 
        'color': 'date',
        'centered': True
    },
    'events': {
        'y_start': 140,
        'line_height': 20,
        'size': 1,
        'color': 'events',
        'margin': 10
    },
    'status': {
        'y': 285,
        'size': 1,
        'color': 'status',
        'centered': True
    }
}

# ==================== CONFIGURAÇÕES AVANÇADAS ====================
# Intervalo de coleta de lixo (segundos)
GC_INTERVAL = 300  # 5 minutos

# Intervalo de sincronização NTP (segundos) 
NTP_SYNC_INTERVAL = 3600  # 1 hora

# Intervalo de verificação de conectividade (segundos)
CONNECTIVITY_CHECK_INTERVAL = 60  # 1 minuto

# Buffer para mensagens MQTT
MQTT_BUFFER_SIZE = 1024

# Timeout para operações MQTT (segundos)
MQTT_TIMEOUT = 30

# ==================== MENSAGENS PERSONALIZADAS ====================
# Mensagens exibidas na tela
MESSAGES = {
    'startup': "MAGIC MIRROR",
    'wifi_connecting': "Conectando WiFi...",
    'wifi_connected': "WiFi Conectado",
    'wifi_failed': "WiFi Falhou",
    'mqtt_connecting': "Conectando MQTT...", 
    'mqtt_connected': "MQTT Conectado",
    'mqtt_failed': "MQTT Indisponivel",
    'no_events': "Nenhum evento hoje",
    'events_title': "EVENTOS HOJE",
    'system_ready': "Sistema Ativo",
    'error_critical': "ERRO CRITICO",
    'restarting': "Reiniciando...",
    'demo_mode': "MODO DEMO",
    'goodbye': "Sistema Encerrado"
}

# ==================== FUNÇÕES DE VALIDAÇÃO ====================
def validate_config():
    """
    Valida a configuração e retorna lista de problemas encontrados
    """
    issues = []
    
    # Validar ID único
    if REGISTRATION_ID in ["MIRROR_001", "MIRROR_CASA_001"]:
        issues.append("Configure REGISTRATION_ID único (ex: MIRROR_SALA_João)")
    
    # Validar WiFi
    if WIFI_SSID in ["SuaRedeWiFi", "MinhaRedeWiFi", ""]:
        issues.append("Configure WIFI_SSID com o nome da sua rede")
    
    if WIFI_PASSWORD in ["SuaSenha", "MinhaSenha123", ""]:
        issues.append("Configure WIFI_PASSWORD com a senha da sua rede")
    
    # Validar configurações numéricas
    if not (1 <= MAX_EVENTS_DISPLAY <= 10):
        issues.append("MAX_EVENTS_DISPLAY deve estar entre 1 e 10")
    
    if not (10 <= CONNECTION_TIMEOUT <= 120):
        issues.append("CONNECTION_TIMEOUT deve estar entre 10 e 120 segundos")
    
    if TIMEZONE_OFFSET < -12 or TIMEZONE_OFFSET > 12:
        issues.append("TIMEZONE_OFFSET deve estar entre -12 e +12")
    
    # Validar display
    if DISPLAY_WIDTH <= 0 or DISPLAY_HEIGHT <= 0:
        issues.append("DISPLAY_WIDTH e DISPLAY_HEIGHT devem ser positivos")
    
    return issues

def is_debug():
    """
    Retorna se o modo debug está ativo
    """
    return DEBUG_ENABLED

def get_debug_level():
    """
    Retorna o nível atual de debug
    """
    return DEBUG_LEVEL if DEBUG_ENABLED else 0

def get_color(color_name):
    """
    Retorna código de cor RGB565 pelo nome
    """
    return COLORS.get(color_name, COLORS['background'])

def get_message(key):
    """
    Retorna mensagem personalizada pela chave
    """
    return MESSAGES.get(key, key.upper())

def should_power_save(current_hour):
    """
    Verifica se deve ativar modo de economia baseado na hora
    """
    if not POWER_SAVE_ENABLED:
        return False
    
    try:
        start_hour = int(POWER_SAVE_HOURS['start'].split(':')[0])
        end_hour = int(POWER_SAVE_HOURS['end'].split(':')[0])
        
        if start_hour > end_hour:  # Período noturno (ex: 23h às 6h)
            return current_hour >= start_hour or current_hour <= end_hour
        else:  # Período diurno (ex: 12h às 14h)
            return start_hour <= current_hour <= end_hour
    except:
        return False

def get_layout_position(element):
    """
    Retorna posição de layout para um elemento
    """
    return LAYOUT.get(element, {})

def print_config_summary():
    """
    Imprime resumo da configuração atual
    """
    print("\n" + "="*50)
    print("📋 RESUMO DA CONFIGURAÇÃO")
    print("="*50)
    print(f"🆔 Registration ID: {REGISTRATION_ID}")
    print(f"📶 WiFi SSID: {WIFI_SSID}")
    print(f"🖥️  Display: {DISPLAY_WIDTH}x{DISPLAY_HEIGHT}")
    print(f"🌍 Fuso horário: UTC{TIMEZONE_OFFSET:+d}")
    print(f"📅 Max eventos: {MAX_EVENTS_DISPLAY}")
    print(f"🔧 Firmware: {FIRMWARE_VERSION}")
    print(f"🐛 Debug: {'Ativo' if DEBUG_ENABLED else 'Inativo'}")
    print(f"💾 Economia energia: {'Ativa' if POWER_SAVE_ENABLED else 'Inativa'}")
    print("="*50)

# ==================== CONFIGURAÇÕES ESPECÍFICAS DO HARDWARE ====================
# Ajustes específicos para diferentes tipos de display
DISPLAY_CONFIG = {
    'init_sequence': [
        (0x01, None, 100),    # Software reset + delay
        (0x11, None, 100),    # Sleep out + delay  
        (0x3A, [0x55], 0),    # Pixel format 16-bit
        (0x36, [0xE8], 0),    # Memory access control
        (0x29, None, 50),     # Display on + delay
    ],
    'color_order': 'RGB',     # ou 'BGR' dependendo do display
    'invert_colors': False,   # True se cores estiverem invertidas
    'flip_horizontal': False, # True para espelhar horizontalmente
    'flip_vertical': False    # True para espelhar verticalmente
}

# ==================== TESTE DE CONFIGURAÇÃO ====================
if __name__ == "__main__":
    print("🧪 TESTE DE CONFIGURAÇÃO")
    print("-" * 40)
    
    # Mostrar resumo
    print_config_summary()
    
    # Validar configuração
    issues = validate_config()
    
    if issues:
        print("\n❌ PROBLEMAS ENCONTRADOS:")
        for i, issue in enumerate(issues, 1):
            print(f"  {i}. {issue}")
        print("\n🔧 Corrija os problemas acima e teste novamente.")
    else:
        print("\n✅ CONFIGURAÇÃO VÁLIDA!")
        print("🚀 Sistema pronto para execução.")
    
    # Testar funções auxiliares
    print(f"\n🎨 Cor de fundo: 0x{get_color('background'):04X}")
    print(f"📝 Mensagem startup: '{get_message('startup')}'")
    print(f"💤 Economia às 2h: {should_power_save(2)}")
    print(f"💡 Economia às 14h: {should_power_save(14)}")
    
    print("\n✨ Teste de configuração concluído!")