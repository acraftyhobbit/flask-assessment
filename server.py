from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


@app.route("/")
def index():
    """Return homepage."""

    return render_template("index.html")

@app.route("/application-form")
def app_form():
    """Return homepage."""

    jobs = {"software-engineer" : "Software Engineer", "qa-engineer": "QA Engineer", "product-manager": "Product Manager"}

    return render_template("application-form.html",jobs=jobs)

@app.route('/application-success', methods=["POST"])
def app_confirmation():
    """Return a confirmation the app was submited."""

    first_name = request.form.get("first-name")
    last_name = request.form.get("last-name")
    job_postion = request.form.get("job-postion")
    salary = request.form.get("salary")
    
    

    return render_template("application-response.html",
                           first_name=first_name,
                           last_name=last_name,
                           salary="$" + '{:20,.2f}'.format(float(salary)),
                           job_postion=job_postion)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
