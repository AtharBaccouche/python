from flask import Flask, render_template,session
app = Flask(__name__)
import random 

# our index route will handle rendering our 
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes
@app.route('/')
def rend():
    session['key']=random.randint(1, 100)
    print(session)
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run(debug=True)