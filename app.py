from flask import Flask, render_template, request, jsonify
import time
import random
from explainers import CodeExplainer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/explain', methods=['POST'])
def explain_code():
    try:
        data = request.json
        code = data.get('code', '').strip()
        
        if not code:
            return jsonify({
                'error': True,
                'message': '🏁 No code detected on the track! Please paste your code to begin the race analysis.'
            })
        
        # Simulate processing time with realistic delay
        time.sleep(random.uniform(2.0, 3.5))
        
        # Get explanation from our AI explainer
        explainer = CodeExplainer()
        explanation = explainer.explain_code(code)
        
        return jsonify({
            'error': False,
            'explanation': explanation
        })
        
    except Exception as e:
        return jsonify({
            'error': True,
            'message': f'🚨 Pit stop required! Error in race analysis: {str(e)}'
        })

@app.route('/health')
def health_check():
    return jsonify({'status': 'Engine running at full throttle! 🏎️'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)