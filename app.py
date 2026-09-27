from flask import Flask, render_template
import os

app = Flask(__name__)

LINPEAS_FILE = "linpeas_output.txt"
ACCESS_LOG_FILE = "access_log.txt"
DECOYS = [".env", "id_rsa", "credentials"]

def check_linpeas_mentions(decoy_name):
    if not os.path.exists(LINPEAS_FILE):
        return False
    with open(LINPEAS_FILE, "rb") as f:
        content = f.read().decode("utf-8", errors="ignore")
    return decoy_name in content

def check_access_log(decoy_name):
    if not os.path.exists(ACCESS_LOG_FILE):
        return False
    with open(ACCESS_LOG_FILE, "r") as f:
        content = f.read()
    return decoy_name in content

def get_verdict(flagged, touched):
    if flagged and touched:
        return "Good bait", "good"
    elif flagged and not touched:
        return "Partially good", "partial"
    elif not flagged and touched:
        return "Weak signal", "partial"
    else:
        return "Bad bait", "bad"

@app.route("/")
def index():
    results = []
    for decoy in DECOYS:
        flagged = check_linpeas_mentions(decoy)
        touched = check_access_log(decoy)
        verdict, css_class = get_verdict(flagged, touched)
        results.append({
            "decoy": decoy,
            "flagged": flagged,
            "touched": touched,
            "verdict": verdict,
            "css_class": css_class
        })
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)