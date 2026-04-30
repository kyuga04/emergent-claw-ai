from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

# Mengambil konfigurasi dari Environment Variables (Lebih Aman)
API_KEY = os.environ.get('AI_API_KEY', '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')
BASE_URL = os.environ.get('AI_BASE_URL', 'https://api.openai.com/v1')

client = openai.OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/ai', methods=['POST'])
def ai_response():
    data = request.json
    user_msg = data.get('message')
    system_prompt = data.get('system', 'Anda adalah asisten AI yang sangat cerdas.')

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", # Menggunakan model yang lebih umum
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_msg}
            ]
        )
        return jsonify({"result": response.choices[0].message.content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
