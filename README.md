# Projeto-feira-de-ciencias
# 🌱 Arduino Smart Automation System

![Arduino](https://img.shields.io/badge/Arduino-Uno-blue?logo=arduino)
![Status](https://img.shields.io/badge/status-active-success)
![License](https://img.shields.io/badge/license-MIT-green)
![Made by](https://img.shields.io/badge/made%20by-Nathaniel-blue)

> Sistema automatizado com sensores para controle de ambiente utilizando Arduino.

---

## 📌 Sobre o projeto

Este projeto implementa um sistema inteligente capaz de monitorar e controlar:

- 📏 Nível/distância (sensor ultrassônico)
- 💡 Luminosidade (LDR)
- 🌡️ Temperatura ambiente (NTC)

Com base nesses dados, o sistema atua automaticamente em:

- 🚿 Bomba de água  
- 🌬️ Ventilador  
- 💡 Iluminação (LED)  

---

## 🎯 Funcionalidades

| Sensor | Condição | Ação |
|------|--------|------|
| Ultrassônico | Distância < 10 cm | Liga bomba |
| Ultrassônico | Distância ≥ 10 cm | Desliga bomba |
| LDR | Luz < 60% | Liga LED |
| LDR | Luz ≥ 60% | Desliga LED |
| NTC | Temp > 30°C | Liga ventilador |
| NTC | Temp ≤ 30°C | Desliga ventilador |

---

## 🔌 Hardware utilizado

- Arduino Uno / Nano
- Sensor ultrassônico HC-SR04
- LDR (fotoresistor)
- Termistor NTC 10k
- Resistores (10k recomendado)
- Jumpers
- (Opcional) Módulo relé

---

## 🧩 Pinagem

| Componente        | Pino |
|------------------|------|
| Trig (HC-SR04)   | 2    |
| Echo (HC-SR04)   | 3    |
| Bomba            | 7    |
| Ventilador       | 8    |
| LED              | 13   |
| LDR              | A5   |
| NTC              | A0   |

---

## ⚙️ Funcionamento

O sistema executa continuamente:

1. Mede a distância com o sensor ultrassônico  
2. Lê a luminosidade com o LDR  
3. Calcula a temperatura com o NTC  
4. Toma decisões automáticas com base nos valores  
5. Exibe tudo no Serial Monitor  

---

## 🧮 Cálculo da Temperatura

Utiliza a equação Beta do termistor:


T = 1 / ((1/T0) + (1/B) * ln(R/R0))


Onde:

- `T0 = 298.15K (25°C)`
- `B = 3950`
- `R0 = 10kΩ`

---

## 📟 Exemplo de saída


12.5 cm
45% de luz
28.3 °C
//////////////////


---

## 🚀 Melhorias futuras

- 📺 Display LCD/OLED
- 🌐 Integração com Web (ESP8266 / ESP32)
- 📱 Controle via aplicativo
- ⚙️ Configuração dinâmica de limites
- ☁️ Monitoramento em nuvem

---

## 📂 Estrutura do projeto


📁 arduino-smart-system
├── codigo.ino
└── README.md


---

## 🛠️ Como usar

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/seu-repo.git
Abra o código na Arduino IDE
Conecte os componentes conforme a pinagem
Faça upload para o Arduino
Abra o Serial Monitor (9600 baud)
👨‍💻 Autor

Nathaniel Alves Ribeiro
📧 nathanielalves08@gmail.com

📄 Licença

Este projeto está sob a licença MIT.
Sinta-se livre para usar e modificar.
