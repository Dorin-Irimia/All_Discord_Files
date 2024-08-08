
from flask import Flask, render_template, request, jsonify
import requests


app = Flask(__name__)

ESP8266_IP = ESP8266_IP = "http://<ESP8266_IP>"  # voi inlocui IP ul cu cel la care este ESP ul 

@app.route('/')
def index():
    return render_template('index.html')

# Starea becului (False pentru oprit, True pentru pornit)
owl_state = False
bedroom_light_state = False
bedroom_color_light_state = False
bedroom_color_light_color = '#FFFFFF'
desk_light_state = False
desk_color_light_state = False
desk_color_light_color = '#FFFFFF'
led_strip_state = False

# Rutele API-ului pentru obținerea și setarea stării becurilor
@app.route('/api/owl', methods=['GET', 'POST'])
def owl():
    global owl_state
    if request.method == 'POST':
        data = request.json
        owl_state = data.get('state', False)
        return jsonify({'success': True, 'state': owl_state})
    return jsonify({'state': owl_state})

@app.route('/api/bedroom_light', methods=['GET', 'POST'])
def bedroom_light():
    global bedroom_light_state
    if request.method == 'POST':
        data = request.json
        bedroom_light_state = data.get('state', False)
        return jsonify({'success': True, 'state': bedroom_light_state})
    return jsonify({'state': bedroom_light_state})

@app.route('/api/bedroom_color_light', methods=['GET', 'POST'])
def bedroom_color_light():
    global bedroom_color_light_state, bedroom_color_light_color
    if request.method == 'POST':
        data = request.json
        bedroom_color_light_state = data.get('state', bedroom_color_light_state)
        bedroom_color_light_color = data.get('color', bedroom_color_light_color)
        return jsonify({'success': True, 'state': bedroom_color_light_state, 'color': bedroom_color_light_color})
    return jsonify({'state': bedroom_color_light_state, 'color': bedroom_color_light_color})

@app.route('/api/desk_light', methods=['GET', 'POST'])
def desk_light():
    global desk_light_state
    if request.method == 'POST':
        data = request.json
        desk_light_state = data.get('state', False)
        return jsonify({'success': True, 'state': desk_light_state})
    return jsonify({'state': desk_light_state})

@app.route('/api/desk_color_light', methods=['GET', 'POST'])
def desk_color_light():
    global desk_color_light_state, desk_color_light_color
    if request.method == 'POST':
        data = request.json
        desk_color_light_state = data.get('state', desk_color_light_state)
        desk_color_light_color = data.get('color', desk_color_light_color)
        return jsonify({'success': True, 'state': desk_color_light_state, 'color': desk_color_light_color})
    return jsonify({'state': desk_color_light_state, 'color': desk_color_light_color})

@app.route('/api/led_strip', methods=['GET', 'POST'])
def led_strip():
    global led_strip_state
    if request.method == 'POST':
        data = request.json
        led_strip_state = data.get('state', False)
        return jsonify({'success': True, 'state': led_strip_state})
    return jsonify({'state': led_strip_state})

@app.route('/api/toggle_light', methods=['POST'])
def toggle_light():
    light_id = request.json.get('light_id')
    action = request.json.get('action')

    try:
        # Trimitere comanda către ESP8266
        response = requests.get(f"{ESP8266_IP}/{light_id}/{action}")
        if response.status_code == 200:
            return jsonify({'status': 'success', 'message': f'{action.capitalize()} successfully'})
        else:
            return jsonify({'status': 'error', 'message': 'Failed to communicate with ESP8266'}), 500
    except requests.exceptions.RequestException as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


if __name__ == '__main__':
    app.run(debug = True)    # host='0.0.0.0', port=5000)
 