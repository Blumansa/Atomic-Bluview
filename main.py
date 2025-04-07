from flask import Flask, request, jsonify
from PIL import Image
import io

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'screenshot' not in request.files:
        return jsonify({'error': 'No image received'}), 400

    # Détection du mode BLU COT
    cot_mode = request.args.get('cot', 'false').lower() == 'true'

    # Simule une analyse IA + COT si activé
    result = {
        'structure': 'MSS baissier confirmé',
        'cisd': 'Displacement observé en Killzone NY',
        'liquidity': 'Sweep Equal Lows + Resting liquidity détectée',
        'ob': 'OB H1 détecté à 2331.40 – 2331.90',
        'volume': 'HVN confirmé à 2331.60',
        'order_type': 'Sell Limit',
        'entry_zone': '2331.40 – 2331.90',
        'sl': '2332.60',
        'tp': '2323.20',
        'justification': 'MSS + OB H1 + Sweep + HVN Volume + Killzone NY',
        'probabilité': '96 %'
    }

    # Ajoute le bloc COT si le mode est activé
    if cot_mode:
        result['blu_cot'] = {
            'alignement': True,
            'commentaire': '✅ Aligné avec les Non-Commerciaux (COT SELL dominant)'
        }

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
