from flask import Flask, render_template

app = Flask(__name__)


@app.route("/favicon.ico")
def favicon():
    # No favicon yet; return 204 to avoid 404 log noise
    return ("", 204)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/results/")
def analytics_results():
    return render_template("analytics_results.html")


if __name__ == "__main__":
    # Debugger on, but disable auto-reloader to avoid double-registration of routes in some setups
    app.run(debug=True, use_reloader=False)
