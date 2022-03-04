from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect
from services.services import FeedlyClient



app = Flask(__name__)
db_name = 'database.db'
app.config['SECRET_KEY'] = 'potato'
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

FEEDLY_REDIRECT_URI = "http://fabreadly.com/auth_callback"
FEEDLY_CLIENT_ID = "sandbox"
FEEDLY_CLIENT_SECRET = "7x7xWjaq0u6Jguw4weEeCM9tyVsLwTPc"


def get_feedly_client(token=None):
    if token:
        return FeedlyClient(token=token, sandbox=True)
    else:
        return FeedlyClient(
            client_id=FEEDLY_CLIENT_ID,
            client_secret=FEEDLY_CLIENT_SECRET,
            sandbox=True
        )


def auth(request):
    feedly = get_feedly_client()
    code_url = feedly.get_code_url(FEEDLY_REDIRECT_URI)
    return redirect(code_url)

@app.route('/', methods=['POST'])
def fetch_data():
    news_source = request.json['news_source']
    URL = request.json['URL']
    news_content = request.json['news_content']
    updated_at = request.json['updated_at']
    # category_id = request.json[]


if __name__ == '__main__':
    app.run(debug=True)