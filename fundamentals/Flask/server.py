from flask import Flask, render_template, request, redirect,session
app = Flask(__name__)
# our index route will handle rendering our 
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/form', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    session["name"]=request.form["name"]
    session["email"]=request.form["email"]
    # Never render a template on a POST request.
    # Instead we will redirect to our index route.
    return redirect('/result')

@app.route('/result')
def display():
    print("result")
    print(request.form)# NO INFORMATION WI NEED SESSION TO KHNOW ? EMPTY OBJECT IN THE TERMINAL IT  SHOW 
    # session["name"]=request.form["name"]
    return render_template("display.html")



if __name__ == "__main__":
    app.run(debug=True)

