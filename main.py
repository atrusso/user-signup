from flask import Flask, request, render_template

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/signup", methods=['POST', 'GET'])
def signup():
    username = request.form['username']
    password = request.form['password']
    verify_pass = request.form['verify-password']
    email = request.form['email']
    
    user_error = ""
    pass_error = ""
    verify_pass_error = ""
    email_error = ""

    #Username validation
    if username == "":
        user_error = "Username was left blank"
    elif len(username) < 3 or len(username) > 20:
        user_error = "Username is invalid - length allowed 3-20 characters"
        username = ""
    elif " " in username:
        user_error = "Username is invalid - contains a space"
        username = ""

    #Password validation
    if password == "":
        pass_error = "Password was left blank"
    elif len(password) < 3 or len(password) > 20:
        pass_error = "Password is invalid - length allowed 3-20 characters"
        password = ""
    elif " " in password:
        pass_error = "Password is invalid - contains a space"
        password = ""

    #Verify Password validation
    if verify_pass == "":
        verify_pass_error = "Verify Password was left blank"
    elif len(verify_pass) < 3 or len(verify_pass) > 20:
        verify_pass_error = "Verify Password is invalid - length allowed 3-20 characters"
        verify_pass = ""
    elif " " in verify_pass:
        verify_pass_error = "Verify Password is invalid - contains a space"
        verify_pass = ""

    #Password/Verify match validation
    if password != verify_pass:
        pass_error = "Password and Verify Password values don't match"
        password = ""
        verify_pass = ""

    #Email validation
    if email != "":
        if " " in email:
            email_error = "Email is invalid - contains a space"
            email = ""
        elif len(email) < 3 or len(email) > 20:
            email_error = "Email is invalid - length allowed 3-20 characters"
            email = ""
        elif email.count(".") < 1:
            email_error = "Email is invalid - does not contain a '.'"
            email = ""
        elif email.count(".") > 1:
            email_error = "Email is invalid - contains too many '.'"
            email = ""
        elif email.count("@") < 1:
            email_error = "Email is invalid - does not contain '@'"
            email = ""
        elif email.count("@") > 1:
            email_error = "Email is invalid - contains too many '@'"
            email = ""

    if not user_error and not pass_error and not verify_pass_error and not email_error:
        return render_template('welcome.html', username=username)
    else:
        return render_template("index.html", username=username, email=email, user_error=user_error, pass_error=pass_error, 
        verify_pass_error=verify_pass_error, email_error=email_error)

@app.route("/")
def index():
    return render_template('index.html')

app.run()