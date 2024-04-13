import flask

bp = flask.Blueprint('app1', __name__)

app = flask.Flask(__name__)

@bp.route('/')
def index():
    return 'Hello, app1!'

app.register_blueprint(bp, url_prefix='/app1')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, )
