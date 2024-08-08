
from flask import Flask, render_template, request, jsonify
'''
for HomeAssistant code is belw:

import requests

home_assistant_url = "http://IP_ADRESA_HOME_ASSISTANT:8123/api/services/light/turn_on"
headers = {
    "Authorization": "Bearer YOUR_LONG_LIVED_ACCESS_TOKEN",
    "Content-Type": "application/json",
}

data = {
    "entity_id": "light.lidl_light",
    "brightness": 255,
    "rgb_color": [255, 87, 51],  # Exemplu de culoare
}

response = requests.post(home_assistant_url, headers=headers, json=data)
print(response.json())
'''

app = Flask(__name__)


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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
    '''
@app.rute('/')
def home():
    return render_template('index.html')

@app.route('/api/owl', methods=['GET'])
def get_owl_state():
    """
    Obține starea curentă a becului.
    """
    return jsonify({'state': owl_state})

@app.route('/api/bedroom_light', methods=['GET'])
def get_bedroom_light_state():
    """
    Obține starea curentă a becului.
    """
    return jsonify({'state': bedroom_light})

@app.route('/api/bedroom_color_light', methods=['GET'])
def get_bedroom_color_light_state():
    """
    Obține starea curentă a becului.
    """
    return jsonify({'state': bedroom_color_light})

@app.route('/api/desk_light', methods=['GET'])
def get_desk_light_state():
    """
    Obține starea curentă a becului.
    """
    return jsonify({'state': desk_light})

@app.route('/api/desk_color_light', methods=['GET'])
def get_desk_color_light_state():
    """
    Obține starea curentă a becului.
    """
    return jsonify({'state': desk_color_light})

@app.route('/api/led_strip', methods=['GET'])
def get_led_strip_state():
    """
    Obține starea curentă a becului.
    """
    return jsonify({'state': led_strip})



@app.route('/api/owl', methods=['POST'])
def set_owl_state():
    """
    Setează starea becului.
    """
    global owl_state
    data = request.json
    owl_state = data.get('state', False)
    # Aici adaugă logica pentru a trimite comanda la ESP8266 sau Home Assistant
    return jsonify({'success': True, 'state': owl_state})

@app.route('/api/bedroom_light', methods=['POST'])
def set_bedroom_light_state():
    """
    Setează starea becului.
    """
    global bedroom_light_state
    data = request.json
    bedroom_light_state = data.get('state', False)
    # Aici adaugă logica pentru a trimite comanda la ESP8266 sau Home Assistant
    return jsonify({'success': True, 'state': bedroom_light_state})

@app.route('/api/bedroom_color_light', methods=['POST'])
def set_bedroom_color_light_state():
    """
    Setează starea becului.
    """
    global bedroom_color_light_state
    data = request.json
    bedroom_color_light_state = data.get('state', False)
    # Aici adaugă logica pentru a trimite comanda la ESP8266 sau Home Assistant
    return jsonify({'success': True, 'state': bedroom_color_light_state})

@app.route('/api/desk_light', methods=['POST'])
def set_desk_light_state():
    """
    Setează starea becului.
    """
    global desk_light_state
    data = request.json
    desk_light_state = data.get('state', False)
    # Aici adaugă logica pentru a trimite comanda la ESP8266 sau Home Assistant
    return jsonify({'success': True, 'state': desk_light_state})

@app.route('/api/desk_color_light', methods=['POST'])
def set_desk_color_light_state():
    """
    Setează starea becului.
    """
    global desk_color_light_state
    data = request.json
    desk_color_light_state = data.get('state', False)
    # Aici adaugă logica pentru a trimite comanda la ESP8266 sau Home Assistant
    return jsonify({'success': True, 'state': desk_color_light_state})

@app.route('/api/led_strip', methods=['POST'])
def set_desk_color_light_state():
    """
    Setează starea becului.
    """
    global led_strip_state
    data = request.json
    led_strip_state = data.get('state', False)
    # Aici adaugă logica pentru a trimite comanda la ESP8266 sau Home Assistant
    return jsonify({'success': True, 'state': led_strip_state})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
'''