from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        # For demonstration, accept any non-empty username and password
        if username and password:
            return f"Login successful! Welcome, {username}."
        else:
            return "Login failed! Please provide both username and password."
    
    return render_template("login_form.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000)
