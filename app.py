from flask import Flask, render_template, redirect, url_for
import RPi.GPIO as GPIO

RELAY_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)
GPIO.output(RELAY_PIN, GPIO.HIGH)

app = Flask(__name__)
lamp_state = False

@app.route('/')
def index():
    return render_template('index.html', lamp_on=lamp_state)

@app.route('/on')
def turn_on():
    global lamp_state
    GPIO.output(RELAY_PIN, GPIO.LOW)
    lamp_state = True
    return redirect(url_for('index'))

@app.route('/off')
def turn_off():
    global lamp_state
    GPIO.output(RELAY_PIN, GPIO.HIGH)
    lamp_state = False
    return redirect(url_for('index'))

@app.route('/toggle')
def toggle():
    global lamp_state
    if lamp_state:
        GPIO.output(RELAY_PIN, GPIO.HIGH)
        lamp_state = False
    else:
        GPIO.output(RELAY_PIN, GPIO.LOW)
        lamp_state = True
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
