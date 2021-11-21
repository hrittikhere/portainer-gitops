from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('complete.html')


# start the application on port 3111
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='3111')