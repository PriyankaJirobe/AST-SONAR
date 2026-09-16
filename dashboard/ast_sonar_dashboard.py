import serial
import tkinter as tk
from tkinter import ttk

# =========================
# ESP32 CONNECTION
# =========================
PORT = "COM4"
BAUDRATE = 115200

ser = serial.Serial(PORT, BAUDRATE, timeout=0.05)

# =========================
# WINDOW
# =========================
root = tk.Tk()
root.title("AST - SONAR | Adaptive Sonar Transmission System")
root.geometry("950x680")
root.minsize(800, 600)
root.configure(bg="#08111f")

# =========================
# COLORS
# =========================
BG = "#08111f"
CARD = "#101d30"
TEXT = "#f2f7ff"
MUTED = "#8fa3bb"
CYAN = "#35d9ff"
GREEN = "#35e58b"
ORANGE = "#ffb84d"

# =========================
# HEADER
# =========================
tk.Label(
    root, text="AST — SONAR",
    font=("Segoe UI", 32, "bold"),
    fg=CYAN, bg=BG
).pack(pady=(25, 2))

tk.Label(
    root, text="Adaptive Sonar Transmission System",
    font=("Segoe UI", 13),
    fg=MUTED, bg=BG
).pack()

# =========================
# TRANSMISSION STATUS
# =========================
status_label = tk.Label(
    root, text="●  TRANSMISSION ACTIVE",
    font=("Segoe UI", 16, "bold"),
    fg=GREEN, bg=BG
)
status_label.pack(pady=18)

# =========================
# FREQUENCY CARD
# =========================
freq_card = tk.Frame(root, bg=CARD)
freq_card.pack(fill="x", padx=45, pady=8)

tk.Label(
    freq_card, text="FREQUENCY",
    font=("Segoe UI", 12, "bold"),
    fg=MUTED, bg=CARD
).pack(pady=(18, 2))

frequency_label = tk.Label(
    freq_card, text="---- Hz",
    font=("Segoe UI", 34, "bold"),
    fg=TEXT, bg=CARD
)
frequency_label.pack()

frequency_bar = ttk.Progressbar(
    freq_card, orient="horizontal",
    length=700, mode="determinate",
    maximum=5000
)
frequency_bar.pack(pady=(8, 20))

# =========================
# THREE CARDS
# =========================
cards = tk.Frame(root, bg=BG)
cards.pack(fill="x", padx=40, pady=10)

# POWER
power_card = tk.Frame(cards, bg=CARD, width=260, height=150)
power_card.pack(side="left", expand=True, fill="both", padx=7)

tk.Label(
    power_card, text="POWER",
    font=("Segoe UI", 12, "bold"),
    fg=MUTED, bg=CARD
).pack(pady=(18, 3))

power_label = tk.Label(
    power_card, text="-- %",
    font=("Segoe UI", 27, "bold"),
    fg=TEXT, bg=CARD
)
power_label.pack()

power_bar = ttk.Progressbar(
    power_card, orient="horizontal",
    length=190, mode="determinate",
    maximum=100
)
power_bar.pack(pady=10)

# MODE
mode_card = tk.Frame(cards, bg=CARD, width=260, height=150)
mode_card.pack(side="left", expand=True, fill="both", padx=7)

tk.Label(
    mode_card, text="OPERATING MODE",
    font=("Segoe UI", 12, "bold"),
    fg=MUTED, bg=CARD
).pack(pady=(18, 10))

mode_label = tk.Label(
    mode_card, text="----",
    font=("Segoe UI", 22, "bold"),
    fg=CYAN, bg=CARD
)
mode_label.pack()

# LINK
link_card = tk.Frame(cards, bg=CARD, width=260, height=150)
link_card.pack(side="left", expand=True, fill="both", padx=7)

tk.Label(
    link_card, text="SYSTEM LINK",
    font=("Segoe UI", 12, "bold"),
    fg=MUTED, bg=CARD
).pack(pady=(18, 10))

link_label = tk.Label(
    link_card, text="ESP32 ONLINE",
    font=("Segoe UI", 20, "bold"),
    fg=GREEN, bg=CARD
).pack()

tk.Label(
    link_card, text="COM4 • 115200 baud",
    font=("Segoe UI", 10),
    fg=MUTED, bg=CARD
).pack(pady=8)

# =========================
# FEEDBACK CARD
# =========================
feedback_card = tk.Frame(root, bg=CARD)
feedback_card.pack(fill="x", padx=45, pady=18)

tk.Label(
    feedback_card, text="SYSTEM FEEDBACK",
    font=("Segoe UI", 12, "bold"),
    fg=MUTED, bg=CARD
).pack(pady=(15, 5))

feedback_label = tk.Label(
    feedback_card, text="Waiting for system data...",
    font=("Segoe UI", 17, "bold"),
    fg=TEXT, bg=CARD
)
feedback_label.pack()

decision_label = tk.Label(
    feedback_card, text="",
    font=("Segoe UI", 12),
    fg=CYAN, bg=CARD
)
decision_label.pack(pady=(4, 15))

# =========================
# SERIAL DATA PROCESSING
# Matches the working Arduino output:
# Frequency : 3102 Hz
# Power     : 50 %
# Mode      : NORMAL
# TX Status : READY
# =========================
def process_line(line):
    line = line.strip()

    if "Frequency" in line:
        try:
            value = line.split(":", 1)[1].strip()
            frequency_label.config(text=value)
            number = int(value.replace("Hz", "").strip())
            frequency_bar["value"] = max(0, min(number, 5000))
        except (ValueError, IndexError):
            pass

    elif "Power" in line:
        try:
            value = line.split(":", 1)[1].strip()
            power_label.config(text=value)
            number = int(value.replace("%", "").strip())
            power_bar["value"] = max(0, min(number, 100))
        except (ValueError, IndexError):
            pass

    elif "Mode" in line:
        try:
            mode = line.split(":", 1)[1].strip()
            mode_label.config(text=mode)

            if mode == "NORMAL":
                mode_label.config(fg=CYAN)
                feedback_label.config(
                    text="USER CONTROL ACTIVE", fg=TEXT
                )
                decision_label.config(
                    text="Frequency follows user selection"
                )

            elif mode == "ADAPTIVE":
                mode_label.config(fg=GREEN)
                feedback_label.config(
                    text="ENVIRONMENT CHECK", fg=GREEN
                )
                decision_label.config(
                    text="Adaptive operating mode selected"
                )

            elif mode == "LOW POWER":
                mode_label.config(fg=ORANGE)
                feedback_label.config(
                    text="POWER LIMITED", fg=ORANGE
                )
                decision_label.config(
                    text="Energy-saving transmission mode"
                )
        except (ValueError, IndexError):
            pass

    elif "TX Status" in line or "TX STATUS" in line:
        try:
            status = line.split(":", 1)[1].strip()

            # Your working Arduino sends READY.
            # READY is displayed as active on the dashboard.
            if status in ("READY", "ACTIVE"):
                status_label.config(
                    text="●  TRANSMISSION ACTIVE", fg=GREEN
                )
                link_label.config(
                    text="ESP32 ONLINE", fg=GREEN
                )
            else:
                status_label.config(
                    text="●  TRANSMISSION STANDBY", fg=ORANGE
                )
        except (ValueError, IndexError):
            pass

# =========================
# SERIAL READER
# =========================
def read_serial():
    try:
        while ser.in_waiting:
            line = ser.readline().decode(
                "utf-8", errors="ignore"
            )
            process_line(line)
    except (serial.SerialException, OSError):
        link_label.config(
            text="ESP32 DISCONNECTED", fg=ORANGE
        )

    root.after(50, read_serial)

# =========================
# START
# =========================
root.after(100, read_serial)

try:
    root.mainloop()
finally:
    if ser.is_open:
        ser.close()
