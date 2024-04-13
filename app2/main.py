import flask

bp = flask.Blueprint('app2', __name__)

app = flask.Flask(__name__)

@bp.route('/')
def index():
    return 'Hello, app2!'

app.register_blueprint(bp, url_prefix='/app2')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, )
