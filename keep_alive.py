from flask import Flask, request, jsonify
from threading import Thread
from sarah.core import get_sarah_response

app = Flask('')


@app.route('/')
def home():
  return "I'm alive"


# Nova rota que recebe a pergunta e retorna a resposta da Sarah
@app.route('/respond', methods=['POST'])
def respond():
  if not request.is_json:
    return jsonify(
        {"reply": "Nenhuma pergunta foi enviada (erro de formato JSON)."}), 400

  data = request.get_json(silent=True)
  if not data or "question" not in data:
    return jsonify({"reply": "Nenhuma pergunta foi enviada."}), 400

  question = data["question"]
  answer = get_sarah_response(question)
  return jsonify({"reply": answer})


def run():
  app.run(host='0.0.0.0', port=8080)


def keep_alive():
  t = Thread(target=run)
  t.start()
