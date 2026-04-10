# 🌱 Smart IoT Dashboard

## 📌 Sobre o projeto

Este projeto implementa um sistema inteligente capaz de **monitorar e controlar variáveis ambientais em tempo real** utilizando sensores e atuadores.

Além do sistema físico com Arduino, o projeto inclui uma **interface gráfica em Python**, proporcionando uma visualização moderna, intuitiva e interativa.

![Arduino](https://img.shields.io/badge/Arduino-Uno-blue?logo=arduino)
![Status](https://img.shields.io/badge/status-active-success)
![License](https://img.shields.io/badge/license-MIT-green)
![Made by](https://img.shields.io/badge/made%20by-Nathaniel-blue)

---

## 🧠 Tecnologias utilizadas

### 🔌 Hardware

* Arduino Uno / Nano
* Sensor ultrassônico HC-SR04
* LDR (fotoresistor)
* Termistor NTC 10k
* Resistores (10k recomendado)
* Jumpers
* (Opcional) Módulo relé

### 💻 Software

* Arduino IDE (C/C++)
* Python 3
* Tkinter (interface gráfica)
* PySerial (comunicação serial)

---

## 🎯 Funcionalidades

| Sensor       | Condição          | Ação               |
| ------------ | ----------------- | ------------------ |
| Ultrassônico | Distância < 10 cm | Liga bomba         |
| Ultrassônico | Distância ≥ 10 cm | Desliga bomba      |
| LDR          | Luz < 60%         | Liga LED           |
| LDR          | Luz ≥ 60%         | Desliga LED        |
| NTC          | Temp > 30°C       | Liga ventilador    |
| NTC          | Temp ≤ 30°C       | Desliga ventilador |

---

## 🔌 Pinagem

| Componente     | Pino |
| -------------- | ---- |
| Trig (HC-SR04) | 2    |
| Echo (HC-SR04) | 3    |
| Bomba          | 7    |
| Ventilador     | 8    |
| LED            | 13   |
| LDR            | A5   |
| NTC            | A0   |

---

## ⚙️ Funcionamento do sistema

### 🔄 Arduino

O Arduino executa continuamente:

* Mede a distância com o sensor ultrassônico
* Lê a luminosidade com o LDR
* Calcula a temperatura com o NTC
* Toma decisões automáticas
* Envia os dados via Serial

### 🖥️ Computador

* Recebe os dados via Python
* Exibe tudo em tempo real no dashboard

---

## 🖥️ Interface Gráfica (Dashboard)

O dashboard foi desenvolvido com **Tkinter**, oferecendo uma visualização clara e profissional.

### 📊 Recursos

* Leitura em tempo real via Serial
* Gauges circulares animados
* Indicadores de status (ON/OFF)
* Interface em tela cheia
* Atualização suave dos dados

---

## 🔌 Comunicação com Arduino

```python
arduino = serial.Serial("COM3", 9600, timeout=1)
```

⚠️ Ajuste a porta conforme o seu sistema operacional.

---

## 📟 Exemplo de saída (Serial)

```
12.5 cm
45% de luz
28.3 °C
//////////////////
```

---

## 🧠 Lógica aplicada no dashboard

```
dist < 10   → Bomba ON
temp > 30   → Ventilador ON
luz < 60    → LED ON
```

---

## 🧮 Cálculo da Temperatura

Utiliza a equação Beta do termistor:

```
T = 1 / ((1/T0) + (1/B) * ln(R/R0))
```

Onde:

* T0 = 298.15K (25°C)
* B = 3950
* R0 = 10kΩ

---

## 📂 Estrutura do projeto

```
arduino-smart-system
├── codigo.ino
├── dashboard.py
└── README.md
```

---

## 🛠️ Como usar

1. Clone o repositório
2. Abra o código na Arduino IDE
3. Monte o circuito conforme a pinagem
4. Faça upload para o Arduino
5. Execute o script Python
6. Visualize os dados no dashboard

---

## 🚀 Melhorias futuras

* Display LCD/OLED
* Integração com ESP8266 / ESP32
* Aplicativo mobile
* Configuração dinâmica de limites
* Monitoramento em nuvem

---

## 👨‍💻 Autor

**Nathaniel Alves Ribeiro**

---

## 📄 Licença

Este projeto está sob a licença MIT.
Sinta-se livre para usar e modificar.
