from flask import Flask, render_template
import os
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', secret_message=os.getenv('MY_SECRET'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)