# Raspberry Pi Lamp Control 💡

Ein kleines Projekt zur webbasierten Steuerung einer 230V-LED-Lampe mithilfe eines Raspberry Pi 5, einem Solid-State-Relais und einem Flask-Webinterface.

## 🔧 Verwendete Komponenten
- Raspberry Pi 5 (ohne GUI, headless)
- Solid State Relay (SSR, 5V, low-level trigger)
- 230V LED-Lampe
- Python 3 + Flask
- HTML für Benutzeroberfläche

## 🌐 Funktionen
- Einschalten / Ausschalten / Umschalten über Webinterface
- Steuerung auch über Smartphone im lokalen Netzwerk
- GPIO-Ausgabe zur Relaissteuerung
- Sicherer Aufbau (Phasentrennung über SSR)

## 📸 Bilder
![components_overview](https://github.com/user-attachments/assets/c1d05f55-dc61-4079-8388-5d32f870c4cc)
![raspberry_pi_5](https://github.com/user-attachments/assets/9da3c768-6e35-4bf9-8839-75aa6b0416a8)
![ssr_closeup](https://github.com/user-attachments/assets/ee2129a7-49ab-424f-88ee-429f3f8e9882)
![cable_end](https://github.com/user-attachments/assets/7f3f8638-5ccf-4f7a-ae80-17bc5aaf8890)
![ssr_connected](https://github.com/user-attachments/assets/bb0f0387-e494-4cfc-a2d9-48666d5c319b)
![system_overview](https://github.com/user-attachments/assets/9194eda5-cca2-457b-a3b1-89174a5fb850)

## ▶️ Video-Demonstration
https://drive.google.com/drive/folders/19sxTEfdCkhwktAYUBsZ23fFq9lttW4iJ

## 📁 Dateien
- `app.py`: Flask-App für GPIO-Steuerung
- `templates/index.html`: Webinterface
