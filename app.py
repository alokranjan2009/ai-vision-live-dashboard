from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

STATE_FILE = "state.json"

def load_state():
    with open(STATE_FILE, "r") as f:
        return json.load(f)

def save_state(data):
    with open(STATE_FILE, "w") as f:
        json.dump(data, f, indent=2)

@app.route("/")
def dashboard():
    return render_template("index.html")

@app.route("/state")
def get_state():
    return jsonify(load_state())

@app.route("/command", methods=["POST"])
def command():
    cmd = request.json.get("command")
    state = load_state()

    if cmd == "awaken":
        state["state"] = "AWAKENED"
        state["video"] = "awakening.mp4"

    elif cmd == "reset":
        state["state"] = "RESETTING"
        state["video"] = "matrix_reset.mp4"

    save_state(state)
    return jsonify(state)

if __name__ == "__main__":
    app.run(debug=True)
