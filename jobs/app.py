from flask import Flask
from flask import render_template

app = Flask(__name__)
#app.config.from_object(os.environ['APP_SETTINGS'])

@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')
