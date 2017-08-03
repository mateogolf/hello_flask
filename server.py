from flask import Flask, render_template  # Import Flask to allow us to create our app.
app = Flask(__name__) 

@app.route('/')
def hello_world():
  return render_template('index.html')   # Return the string 'Hello World!' as a response.

app.run(debug=True)