from flask import Flask, render_template, redirect, url_for
import controller

app = Flask(__name__)
led = controller.controller()
led.setup()

@app.route('/on', methods=["GET", 'POST'])
def on():
    led.set_on()
    return redirect(url_for('index'))

@app.route('/off', methods=["GET", "POST"])
def off():
    led.set_off()
    return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template('index.html')

def start():
    led.set_off()
    app.run(host="0.0.0.0", port=5000)
