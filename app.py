from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Menggunakan Emergent Universal LLM Key
client = openai.OpenAI(
    api_key="sk-emergent-0Bc13CdEe776eDa793",
    base_url="https://integrations.emergentagent.com/llm"
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
            model="gpt-4o-mini",
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