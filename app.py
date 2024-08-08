from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

ESP8266_IP = "http://<ESP8266_IP>"  # Replace with your ESP8266 IP address

# Light state and color
bedroom_color_light_state = False
bedroom_color_light_color = '#FFFFFF'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/bedroom_color_light', methods=['GET', 'POST'])
def bedroom_color_light():
    global bedroom_color_light_state, bedroom_color_light_color
    if request.method == 'POST':
        data = request.json
        bedroom_color_light_state = data.get('state', bedroom_color_light_state)
        bedroom_color_light_color = data.get('color', bedroom_color_light_color)

        # Send the state and color to the ESP8266
        try:
            response = requests.post(f"{ESP8266_IP}/set_light", json={
                'state': bedroom_color_light_state,
                'color': bedroom_color_light_color
            })
            if response.status_code == 200:
                return jsonify({'success': True, 'state': bedroom_color_light_state, 'color': bedroom_color_light_color})
            else:
                return jsonify({'success': False, 'error': 'ESP8266 failed to respond'})
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})
    return jsonify({'state': bedroom_color_light_state, 'color': bedroom_color_light_color})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
