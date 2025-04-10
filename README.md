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
→ siehe Screenshots unten

## ▶️ Demo-Video
https://drive.google.com/drive/folders/19sxTEfdCkhwktAYUBsZ23fFq9lttW4iJ

## 📁 Dateien
- `app.py`: Flask-App für GPIO-Steuerung
- `templates/index.html`: Webinterface
