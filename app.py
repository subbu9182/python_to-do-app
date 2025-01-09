from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        selected_items = request.form.getlist("sports")
        if selected_items:
            return redirect(url_for("ready_to_go"))
    return render_template("index.html")

@app.route("/ready")
def ready_to_go():
    return "<h1>READY TO GO!</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

