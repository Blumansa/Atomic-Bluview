from flask import Flask, request, jsonify
from PIL import Image
import pytesseract
import io

app = Flask(__name__)

# Mots-clés à rechercher
PAIRES = ['XAUUSD', 'NAS100', 'NASDAQ', 'US30', 'EURUSD', 'GBPUSD', 'BTCUSD']
TIMEFRAMES = ['M15', 'M30', 'H1', 'H4', 'D1', 'W1']
SIGNALS = ['BUY', 'SELL']

def nettoyer_texte(text):
    text = text.upper().replace(' ', '')
    corrections = {
        'XAUVSD': 'XAUUSD',
        'XAUSUD': 'XAUUSD',
        'NAS10O': 'NAS100',
        'EURUSO': 'EURUSD',
        'BUYY': 'BUY',
        'SELLL': 'SELL'
    }
    for err, cor in corrections.items():
        text = text.replace(err, cor)
    return text

def detecter_infos(image):
    text = pytesseract.image_to_string(image)
    text = nettoyer_texte(text)

    paire = next((p for p in PAIRES if p in text), "Non détectée")
    timeframe = next((tf for tf in TIMEFRAMES if tf in text), "Non détecté")
    signal = next((s for s in SIGNALS if s in text), "Non détecté")

    return paire, timeframe, signal

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'screenshot' not in request.files:
        return jsonify({'error': 'No image received'}), 400

    file = request.files['screenshot']
    image = Image.open(file.stream)

    # 🔍 OCR : lecture visuelle de l’image
    paire, timeframe, signal_visible = detecter_infos(image)

    # 🔁 Simule une analyse IA enrichie
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
        'probabilité': '96 %',
        'paire_detectee': paire,
        'timeframe_detecte': timeframe,
        'signal_visuel': signal_visible
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

