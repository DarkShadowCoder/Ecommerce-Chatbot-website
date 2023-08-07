from flask import Flask , jsonify

app = Flask(__name__)
app.config.from_object('project.config.DevelopmentConfig')


@app.route('/' , methods =['GET'])
def ping_pong():
    return jsonify({
        'status':'success',
        'message':'pong!',
    })


if __name__ == '__main__':
    app.run()