from flask import Flask, render_template, request

from student_manager import (
    calculate_average,
    get_mention,
    is_admitted,
    validate_grades,
)

app = Flask(__name__)


def parse_grades(raw):
    """Transforme '12,15,18' en [12.0, 15.0, 18.0]. Lève ValueError si invalide."""
    parts = [p.strip() for p in raw.split(",") if p.strip() != ""]
    return [float(p.replace(",", ".")) for p in parts]


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        raw = request.form.get("grades", "").strip()
        if not raw:
            error = "Erreur : veuillez saisir au moins une note."
        else:
            try:
                grades = parse_grades(raw)
            except ValueError:
                grades = None
                error = "Erreur : les notes doivent être des nombres séparés par des virgules."

            if grades is not None:
                if not validate_grades(grades):
                    error = "Erreur : les notes doivent être comprises entre 0 et 20."
                else:
                    average = calculate_average(grades)
                    result = {
                        "average": f"{average:g}",
                        "mention": get_mention(average),
                        "admitted": "Admis" if is_admitted(average) else "Non admis",
                    }

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
