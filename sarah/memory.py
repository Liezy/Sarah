import json
import os


def load_memory(file_path="sarah/memory.json"):
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            # Se estiver vazio ou inválido, retorna memória limpa
            return {"context": ""}
    return {"context": ""}


def save_memory(memory, file_path="sarah/memory.json"):
    with open(file_path, "w") as file:
        json.dump(memory, file)
