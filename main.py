from flask import Flask

app = Flask(__name__)

#main site

@app.route('/')
def index():
    return 'Hello from Flask!'

app.run(host='0.0.0.0', port=81)

#blog



#github intergration