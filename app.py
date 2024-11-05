from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    rm = None
    unit = "lbs"

    if request.method == "POST":
        try:
            weight = float(request.form.get("weight", 0))
            reps = int(request.form.get("reps", 1))
            unit = request.form.get("unit", "lbs")
            
            # Convert weight to pounds if kg is selected
            if unit == "kg":
                weight *= 2.20462
            
            # Calculate 1RM using Brzycki’s formula
            rm = weight / (1.0278 - 0.0278 * reps)
            
            # Convert back to kg for display if kg is selected
            if unit == "kg":
                rm /= 2.20462

            rm = round(rm, 2)
        except (ValueError, TypeError):
            rm = "Invalid input"

    return render_template("index.html", rm=rm, unit=unit)

if __name__ == "__main__":
    app.run(debug=True)
