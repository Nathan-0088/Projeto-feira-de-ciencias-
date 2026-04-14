import tkinter as tk
import serial
import re

# conexão com Arduino (ajuste a porta se precisar)
arduino = serial.Serial("COM3", 9600, timeout=1)

# janela principal
root = tk.Tk()
root.title("Dashboard IoT")
root.attributes("-fullscreen", True)
root.configure(bg="#0b1220")

# sair com ESC
root.bind("<Escape>", lambda e: root.destroy())

# área de desenho
canvas = tk.Canvas(root, bg="#0b1220", highlightthickness=0)
canvas.pack(fill="both", expand=True)

# valores
dist = 0
luz = 0.0
temp = 0.0

luz_target = 0
temp_target = 0


def gauge(cx, cy, r, valor, maximo, cor, nome):
    # círculo base
    canvas.create_oval(cx-r, cy-r, cx+r, cy+r, outline="#1f2a44", width=18)

    # progresso
    angulo = (valor / maximo) * 360
    canvas.create_arc(
        cx-r, cy-r, cx+r, cy+r,
        start=90,
        extent=-angulo,
        style="arc",
        outline=cor,
        width=18
    )

    # número no centro
    canvas.create_text(cx, cy, text=int(valor), fill="white",
                       font=("Arial", 30, "bold"))

    # nome
    canvas.create_text(cx, cy+60, text=nome,
                       fill="#94a3b8", font=("Arial", 14))


def status_box(x, y, nome, ativo):
    cor = "#22c55e" if ativo else "#ef4444"
    texto = "ON" if ativo else "OFF"

    canvas.create_rectangle(
        x, y, x+260, y+80,
        fill="#111b2e",
        outline="#1f2a44",
        width=2
    )

    # indicador
    canvas.create_oval(x+20, y+30, x+40, y+50, fill=cor, outline=cor)

    canvas.create_text(x+80, y+40, text=nome,
                       fill="white", font=("Arial", 14, "bold"), anchor="w")

    canvas.create_text(x+220, y+40, text=texto,
                       fill=cor, font=("Arial", 16, "bold"))


def animate():
    global luz, temp

    # suavização
    luz += (luz_target - luz) * 0.08
    temp += (temp_target - temp) * 0.08

    canvas.delete("all")

    # título
    canvas.create_text(
        root.winfo_width() / 2, 50,
        text="SMART IOT DASHBOARD",
        fill="white",
        font=("Arial", 30, "bold")
    )

    # medidores
    gauge(400, 250, 120, luz, 100, "#facc15", "Luminosidade")
    gauge(900, 250, 120, temp, 50, "#38bdf8", "Temperatura")

    # status dos dispositivos
    status_box(1200, 150, "BOMBA", dist < 10)
    status_box(1200, 260, "VENTILADOR", temp > 30)
    status_box(1200, 370, "LED", luz < 60)

    root.after(30, animate)


def read_serial():
    global dist, luz_target, temp_target

    try:
        linha = arduino.readline().decode(errors="ignore").strip()

        if linha:
            if "cm" in linha:
                dist = float(re.findall(r"[\d.]+", linha)[0])

            elif "% de luz" in linha:
                luz_target = float(re.findall(r"\d+", linha)[0])

            elif "°C" in linha:
                temp_target = float(re.findall(r"[\d.]+", linha)[0])

    except:
        pass

    root.after(100, read_serial)


read_serial()
animate()
root.mainloop()
