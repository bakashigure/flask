from flask import Flask

app = Flask(__name__,static_url_path='',root_path='/home/bakashigure/flask')    
@app.route('/')
def index():
    return app.send_static_file('pathetic.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8081,debug=False)
