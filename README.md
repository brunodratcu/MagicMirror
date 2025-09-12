# Magic Mirror - Display LCD

Um sistema completo de Magic Mirror para Raspberry Pi Pico com display LCD, sincronização de horário via NTP e integração com calendários via MQTT.

## ✨ Funcionalidades

- **🕐 Relógio em Tempo Real**: Sincronização automática via NTP
- **📅 Data Atualizada**: Exibição da data atual
- **📋 Eventos do Calendário**: Integração com Outlook/Google Calendar via MQTT
- **🎨 Interface Personalizada**: Fonte bitmap otimizada para LCD
- **🌐 Conectividade WiFi**: Conexão automática com reconexão inteligente
- **🔧 Configuração Flexível**: Sistema de configuração centralizado
- **🐛 Debug Avançado**: Sistema completo de logs e diagnósticos
- **⚡ Otimizado**: Gerenciamento de memória e performance

## 🛠️ Hardware Necessário

### Componentes Principais
- **Raspberry Pi Pico W** (com WiFi)
- **Display LCD Shield** compatível com interface paralela 8-bit
- **Conexões**:
  - Pinos de dados: D0-D7 (GPIO 0-7)
  - Reset (RST): GPIO 16
  - Chip Select (CS): GPIO 17
  - Register Select (RS/DC): GPIO 15
  - Write (WR): GPIO 19
  - Read (RD): GPIO 18

### Esquema de Conexões
```
Raspberry Pi Pico    LCD Display Shield
GPIO 0-7       <-->  D0-D7 (Data Bus)
GPIO 15        <-->  RS (Register Select)
GPIO 16        <-->  RST (Reset)
GPIO 17        <-->  CS (Chip Select)  
GPIO 18        <-->  RD (Read)
GPIO 19        <-->  WR (Write)
3.3V          <-->  VCC
GND           <-->  GND
```

## 📁 Estrutura do Projeto

```
magic-mirror/
├── main.py          # Aplicação principal
├── config.py        # Configurações do sistema
├── font.py          # Sistema de fontes bitmap
├── README.md        # Este arquivo
└── examples/        # Exemplos e testes
    ├── test_display.py
    ├── test_font.py
    └── demo_mode.py
```

## 🚀 Instalação e Configuração

### 1. Preparação do Hardware
1. Monte o display LCD shield no Raspberry Pi Pico
2. Verifique todas as conexões conforme o esquema
3. Conecte alimentação adequada (recomendado: fonte externa para o display)

### 2. Instalação do MicroPython
```bash
# Baixe e instale o MicroPython no Pico W
# Use Thonny IDE ou rshell para transferir os arquivos
```

### 3. Configuração do Sistema
Edite o arquivo `config.py` com suas configurações:

```python
# Identificação única do seu dispositivo
REGISTRATION_ID = "MIRROR_SALA_JOAO"  # ⚠️ ALTERE AQUI

# Configurações de rede WiFi
WIFI_SSID = "MinhaRedeWiFi"           # ⚠️ ALTERE AQUI  
WIFI_PASSWORD = "MinhaSenhaWiFi"      # ⚠️ ALTERE AQUI

# Fuso horário (Brasil = -3)
TIMEZONE_OFFSET = -3
```

### 4. Upload dos Arquivos
Transfira todos os arquivos Python para o Raspberry Pi Pico:
- `main.py`
- `config.py`
- `font.py`

### 5. Instalação de Dependências (se necessário)
```python
# No MicroPython, instale via upip se disponível:
import upip
upip.install('umqtt.simple')
```

## ▶️ Execução

### Modo Normal
```python
# No terminal do Pico ou reinicie o dispositivo
exec(open('main.py').read())
```

### Modos Especiais

#### Modo Demonstração (sem WiFi)
```python
exec(open('examples/demo_mode.py').read())
```

#### Teste do Display
```python
exec(open('examples/test_display.py').read())
```

#### Teste das Fontes
```python
exec(open('examples/test_font.py').read())
```

## 📊 Interface do Display

### Layout da Tela (480x320)

```
┌─────────────────────────────────────────────┐
│                                             │
│           🕐 15:30:42                       │ ← Relógio
│                                             │
│           📅 25/12/2024                     │ ← Data
│                                             │
│         📋 EVENTOS HOJE                     │ ← Título
│                                             │
│         09:00 - Reunião de equipe           │ ← Eventos
│         12:30 - Almoço com cliente          │
│         15:00 - Apresentação projeto        │
│         17:30 - Call internacional          │
│                                             │
│                                             │
│         Status: Sistema ativo               │ ← Status
└─────────────────────────────────────────────┘
```

### Cores Utilizadas
- **Fundo**: Preto (0x0000)
- **Relógio**: Branco (0xFFFF)
- **Data**: Cyan (0x07FF)
- **Eventos**: Branco (0xFFFF)
- **Status**: Amarelo (0xFFE0)
- **Erro**: Vermelho (0xF800)

## 🔧 Configurações Avançadas

### Personalização Visual
```python
# Em config.py, modifique:
COLORS = {
    'background': 0x0000,  # Preto
    'time': 0xFFFF,        # Branco  
    'date': 0x07FF,        # Cyan
    'events': 0xFFFF,      # Branco
    'status': 0xFFE0,      # Amarelo
}

LAYOUT = {
    'clock': {'x': 160, 'y': 40, 'size': 4},
    'date': {'y': 100, 'size': 2, 'centered': True},
    'events': {'y_start': 140, 'line_height': 20},
}
```

### Economia de Energia
```python
# Ativar modo econômico noturno
POWER_SAVE_ENABLED = True
POWER_SAVE_HOURS = {
    'start': '23:00',
    'end': '06:00', 
    'brightness': 30
}
```

### Configurações de Rede
```python
# Múltiplos brokers MQTT para redundância
MQTT_BACKUP_BROKERS = [
    "broker.hivemq.com",
    "mqtt.eclipseprojects.io",
    "broker.emqx.io"
]

# Servidores NTP brasileiros
NTP_SERVERS = [
    "pool.ntp.br",
    "a.ntp.br",
    "time.google.com"
]
```

## 📱 Integração com Calendários

### Configuração MQTT
O sistema usa MQTT público para receber eventos de calendário de um servidor backend.

1. **Descoberta Automática**: O dispositivo se registra automaticamente
2. **Aprovação**: Aguarda aprovação do servidor backend  
3. **Sincronização**: Recebe eventos em tempo real

### Formato de Eventos
```json
{
  "events": [
    {
      "title": "Reunião de equipe",
      "time": "09:00",
      "duration": 60,
      "location": "Sala de reuniões"
    }
  ]
}
```

## 🔍 Solução de Problemas

### Display não Inicializa
```
Sintomas: Tela preta, sem resposta
Soluções:
1. Verificar todas as conexões de hardware
2. Testar alimentação (5V para LCD, 3.3V para Pico)
3. Executar teste isolado: test_display.py
4. Verificar compatibilidade do display
```

### WiFi não Conecta
```  
Sintomas: "WiFi falhou" na tela
Soluções:
1. Verificar SSID e senha no config.py
2. Confirmar que rede é 2.4GHz (Pico W não suporta 5GHz)
3. Verificar força do sinal
4. Testar com hotspot móvel
```

### Horário Incorreto
```
Sintomas: Horário errado exibido
Soluções:  
1. Verificar TIMEZONE_OFFSET no config.py
2. Aguardar sincronização NTP (pode demorar alguns minutos)
3. Verificar conectividade de internet
4. Manualmente definir horário para teste
```

### Caracteres Estranhos
```
Sintomas: Caracteres não exibem corretamente
Soluções:
1. Verificar se caracteres estão na fonte (font.py)
2. Texto será normalizado automaticamente
3. Testar com test_font.py
4. Usar apenas caracteres ASCII se houver problemas
```

### MQTT não Conecta
```
Sintomas: "MQTT falhou", sem eventos
Soluções:
1. Sistema funciona sem MQTT (apenas relógio)
2. Verificar firewall/proxy de rede
3. Tentar brokers alternativos
4. Aguardar - broker público pode estar temporariamente indisponível
```

## 📈 Monitoramento e Debug

### Logs de Debug
```python
# Ativar debug detalhado no config.py
DEBUG_ENABLED = True
DEBUG_LEVEL = 3  # 1=básico, 2=médio, 3=detalhado
```

### Informações do Sistema
```python
# Status de memória
import gc
print(f"Memória livre: {gc.mem_free()} bytes")

# Status de conectividade  
print(f"WiFi: {wifi.is_connected()}")
print(f"MQTT: {mqtt.connected}")

# Informações do RTC
import machine
rtc = machine.RTC()
print(f"Horário atual: {rtc.datetime()}")
```

### Comandos de Diagnóstico
```python
# Teste completo do sistema
exec(open('main.py').read())

# Apenas teste de hardware
from main import test_display
test_display()

# Teste de fontes
from font import demonstrate_font_capabilities  
demonstrate_font_capabilities()
```

## 🔄 Atualizações e Manutenção

### Backup de Configuração
Sempre faça backup do seu `config.py` personalizado antes de atualizações.

### Atualização do Firmware
1. Baixe a versão mais recente
2. Faça backup das configurações  
3. Substitua os arquivos principais
4. Restaure suas configurações personalizadas
5. Teste funcionalidades básicas

### Manutenção Preventiva
- Reinicializar uma vez por semana
- Verificar conectividade de rede mensalmente  
- Limpar fisicamente o display conforme necessário
- Atualizar configurações de horário se necessário (horário de verão)

## 🤝 Contribuições

Contribuições são bem-vindas! Por favor:

1. Faça fork do projeto
2. Crie uma branch para sua feature
3. Faça commit das mudanças
4. Envie pull request
5. Documente alterações no código

### Áreas para Contribuição
- 🎨 Novos temas visuais
- 🌐 Suporte a mais idiomas
- 📱 Integração com outros serviços
- 🔧 Otimizações de performance
- 🐛 Correções de bugs

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.

## 👥 Suporte

- **Issues**: Reporte bugs via Issues do GitHub
- **Discussões**: Use Discussions para perguntas gerais
- **Wiki**: Documentação adicional na Wiki do projeto

## 📚 Recursos Adicionais

### Documentação Técnica
- [MicroPython Official Docs](https://docs.micropython.org/)
- [Raspberry Pi Pico W Datasheet](https://datasheets.raspberrypi.org/picow/pico-w-datasheet.pdf)
- [MQTT Protocol Specification](https://mqtt.org/mqtt-specification/)

### Comunidade
- [MicroPython Forum](https://forum.micropython.org/)
- [Raspberry Pi Community](https://www.raspberrypi.org/forums/)
- [Magic Mirror Community](https://forum.magicmirror.builders/)

---

## 🏆 Changelog

### v2.0.1 (2024-12-25)
- ✅ Sistema completo de fonte bitmap
- ✅ Otimizações de performance  
- ✅ Melhor tratamento de erros
- ✅ Documentação completa
- ✅ Modo demonstração

### v1.0.0 (2024-12-01)
- ✅ Implementação inicial
- ✅ Suporte básico a LCD
- ✅ Conectividade WiFi/MQTT
- ✅ Sincronização NTP

---

**🪞 Magic Mirror v2.0 - Transforme qualquer tela em um espelho inteligente!**