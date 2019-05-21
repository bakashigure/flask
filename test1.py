from flask import Flask
import os
t=os.getcwd()

app = Flask(__name__,static_url_path='',root_path=t)    
@app.route('/')
def index():
    return app.send_static_file('pathetic.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8081)