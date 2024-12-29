from flask import Flask

app = Flask(__name__) #creating an app instance



@app.route('/')
def home():
    return '<h2>Welcome to Python Flask Series</h2>'

if __name__ =='__main__':
    app.run(debug=True)