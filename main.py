from flask import Flask, request, render_template, redirect, session
from flask_session import Session
import helper as ffw

app = Flask(__name__)
# configure app to use sessions
app.config["SESSION_PERMANT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
# to set session variables --> session["varname"] = value
# to get session variables --> session.get("varname") or session["varname"]
# to "clear" session variables --> session["varname"] = None

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "GET": # they clicked the link/button
    return render_template("login.html")
  else: # filled out the login form
    # get the email from the form
    email = request.form.get("member_email")
    # load the current members
    index, member = ffw.get_member(email)
    if member: # there was a match for the email
      #set the logged_in session variable
      session["logged_in"] = True
      session["cur_member"] = member
      return redirect("/")
    else: # not match was found
      return render_template("join.html", email=email)

@app.route("/join", methods=["GET", "POST"])
def join():
  if request.method == "POST": # filled out the form
    # get all the data from the form
    member = {
      "email": request.form.get("email"),
      "first_name": request.form.get("first_name"),
      "last_name": request.form.get("last_name")
    }
    # now add the new member dict to the list of MEMBERS
    ffw.add_member(member)
    session["logged_in"] = True
    session["cur_member"] = member
    return redirect("/")
  return render_template("join.html")
    

@app.route("/logout")
def logout():
  # clear out all session variables and go back to the home page
  session["logged_in"] = None
  session["cur_member"] = None
  return redirect("/")

if __name__ == "__main__":
  app.run("0.0.0.0", debug=True)
