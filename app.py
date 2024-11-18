from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the uploads folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        # Get form data
        name = request.form.get("name")
        age = request.form.get("age")
        file = request.files.get("file")

        # Validate form data
        if not name or not age or not file:
            flash("All fields are required!", "error")
            return redirect(url_for("form"))

        # Save the uploaded file
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # Success message
        flash(f"Data submitted successfully! Name: {name}, Age: {age}", "success")
        return redirect(url_for("form"))

    return render_template("form.html")


if __name__ == "__main__":
    app.run(debug=True)
