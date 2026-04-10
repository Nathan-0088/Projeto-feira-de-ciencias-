import tkinter as tk
import serial
import re

# =========================
# SERIAL (Arduino)
# =========================
arduino = serial.Serial("COM3", 9600, timeout=1)  # troque a porta se necessário

# =========================
# JANELA FULLSCREEN
# =========================
root = tk.Tk()
root.title("🌱 IoT Dashboard")
root.attributes("-fullscreen", True)
root.configure(bg="#0b1220")

# ESC sai do fullscreen
root.bind("<Escape>", lambda e: root.destroy())

# =========================
# CANVAS
# =========================
canvas = tk.Canvas(root, bg="#0b1220", highlightthickness=0)
canvas.pack(fill="both", expand=True)

# =========================
# VARIÁVEIS
# =========================
dist = 0
luz_target = 0
temp_target = 0

luz = 0.0
temp = 0.0

# =========================
# GAUGE (ANEL MODERNO)
# =========================
def gauge(cx, cy, r, val, max_val, color, label):
    # fundo
    canvas.create_oval(cx-r, cy-r, cx+r, cy+r, outline="#1f2a44", width=18)

    # progresso
    angle = (val / max_val) * 360
    canvas.create_arc(
        cx-r, cy-r, cx+r, cy+r,
        start=90,
        extent=-angle,
        style="arc",
        outline=color,
        width=18
    )

    # texto
    canvas.create_text(cx, cy, text=f"{int(val)}", fill="white", font=("Arial", 30, "bold"))
    canvas.create_text(cx, cy+60, text=label, fill="#94a3b8", font=("Arial", 14))

# =========================
# STATUS PROFISSIONAL (CORRIGIDO)
# =========================
def status_box(x, y, name, active):
    color = "#22c55e" if active else "#ef4444"
    state = "ON" if active else "OFF"

    # card
    canvas.create_rectangle(
        x, y, x+260, y+80,
        fill="#111b2e",
        outline="#1f2a44",
        width=2
    )

    # bolinha (ANTES do texto visual)
    canvas.create_oval(
        x+20, y+30, x+40, y+50,
        fill=color,
        outline=color
    )

    # nome do sistema
    canvas.create_text(
        x+80, y+40,
        text=name,
        fill="white",
        font=("Arial", 14, "bold"),
        anchor="w"
    )

    # status ON/OFF
    canvas.create_text(
        x+220, y+40,
        text=state,
        fill=color,
        font=("Arial", 16, "bold")
    )

# =========================
# ANIMAÇÃO SUAVE
# =========================
def animate():
    global luz, temp

    luz += (luz_target - luz) * 0.08
    temp += (temp_target - temp) * 0.08

    canvas.delete("all")

    # título
    canvas.create_text(
        root.winfo_width()/2, 50,
        text="🌱 SMART IOT DASHBOARD",
        fill="white",
        font=("Arial", 30, "bold")
    )

    # GAUGES
    gauge(400, 250, 120, luz, 100, "#facc15", "Luminosidade")
    gauge(900, 250, 120, temp, 50, "#38bdf8", "Temperatura")

    # STATUS
    status_box(1200, 150, "BOMBA", dist < 10)
    status_box(1200, 260, "VENTILADOR", temp > 30)
    status_box(1200, 370, "LED", luz < 60)

    root.after(30, animate)

# =========================
# LEITURA SERIAL
# =========================
def read_serial():
    global dist, luz_target, temp_target

    try:
        line = arduino.readline().decode(errors="ignore").strip()

        if line:
            if "cm" in line:
                dist = float(re.findall(r"[\d.]+", line)[0])

            elif "% de luz" in line:
                luz_target = float(re.findall(r"\d+", line)[0])

            elif "°C" in line:
                temp_target = float(re.findall(r"[\d.]+", line)[0])

    except:
        pass

    root.after(100, read_serial)

# =========================
# START
# =========================
read_serial()
animate()
root.mainloop()