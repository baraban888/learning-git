from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "change-me"  # поставь свой секрет

@app.route("/mypage/me")
def me():
    return render_template("me.html")

@app.route("/mypage/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name","")
        email = request.form.get("email","")
        message = request.form.get("message","")
        print(f"Otrzymano wiadomość od {name} ({email}): {message}")
        flash(f"Dziękuję, {name}! Twoja wiadomość została wysłana.")
        return redirect(url_for("contact"))
    return render_template("contact.html")
