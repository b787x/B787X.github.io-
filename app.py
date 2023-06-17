from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/run_python')
def run_python():
    import subprocess
    result = subprocess.run(
        ['python', '/path/to/your/python/script.py'], stdout=subprocess.PIPE)
    return jsonify({'output': result.stdout.decode('utf-8')})
