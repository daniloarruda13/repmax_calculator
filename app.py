from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    rm = None
    unit = "lbs"
    percentages = []

    if request.method == "POST":
        try:
            weight = float(request.form.get("weight"))
            reps = int(request.form.get("reps"))
            unit = request.form.get("unit", "lbs")

            if unit == "kg":
                weight *= 2.20462

            rm = weight / (1.0278 - 0.0278 * reps)

            if unit == "kg":
                rm /= 2.20462

            rm = round(rm, 2)
            percentages = [(p, round(rm * (p / 100), 2)) for p in range(100, 45, -5)]

        except Exception as e:
            print("Error:", e)
            rm = "Invalid input"

    return render_template("index.html", rm=rm, unit=unit, percentages=percentages)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000, ssl_context=(
 "/etc/letsencrypt/live/traininglab.online/fullchain.pem",
        "/etc/letsencrypt/live/traininglab.online/privkey.pem"))
