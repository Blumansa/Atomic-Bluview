from flask import Flask, request, jsonify
from PIL import Image
import io

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'screenshot' not in request.files:
        return jsonify({'error': 'No image received'}), 400

    file = request.files['screenshot']
    image = Image.open(file.stream)

    # 🧠 Analyse simulée (version IA complète bientôt intégrée ici)
    result = {
        'structure': 'MSS baissier confirmé',
        'cisd': 'Displacement observé en Killzone NY',
        'liquidity': 'Sweep Equal Lows + Resting liquidity détectée',
        'ob': 'OB H1 détecté à 2331.40 – 2331.90',
        'volume': 'HVN confirmé à 2331.60',
        'probabilité': '96 %'
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
