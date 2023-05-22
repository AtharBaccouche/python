from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World atharr!'  # Return the string 'Hello World!' as a response

@app.route('/sucess/<someVar>')          # The "@" decorator associates this route with the function immediately following
def hello(someVar):
    return f"athar nice job: {someVar}" # Return the string 'Hello World!' as a response


@app.route('/exemple')          # The "@" decorator associates this route with the function immediately following
def exemple():
    return render_template('exemple.html')

@app.route('/stu')
def index():
    return render_template("exemple.html", phrase="hello", times=5)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.ccd