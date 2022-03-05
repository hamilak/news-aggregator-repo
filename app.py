import requests
from flask import Flask, request, json
from werkzeug.utils import redirect
from services.services import FeedlyClient
from datetime import datetime
from models.tables import db, Articles, Categories

app = Flask(__name__)


myfeedid = "user/bedb0992-50cc-45a1-9ab1-695746cac476/category/388f38cc-19e4-42fc-b2af-652c4bee80b1"
myurl = "http://cloud.feedly.com/v3/streams/contents?streamId=user/bedb0992-50cc-45a1-9ab1-695746cac476/category" \
        "/388f38cc-19e4-42fc-b2af-652c4bee80b1 "
headers = {'Authorization': 'OAuth ' + "Ay9NP0Hn12AnSomqA9fED2h-OxLMEZkQCBUsQvR1TQYIJGL0kGiTaZ"
                                       "-U4a1UgUvcMPGUbU1XPM_DduWyMTEEXI8pLJ7zQ2UD_4ns5FmNTM-1IgyFqF"
                                       "-kUM5Ie6OXjFipkNY8ZeF859F2pGrhrppYWi_ooqS8fUb8sDnmfbbdYx8mOrI7SSAFvasY8GlIXxQ9cxiDPhrgAKZUq2Mr-OCvWgMrbtb0gY6FhX-L28SEnAGP5AejQoGM3_yQ5S8:feedlydev"}
res = requests.get(url=myurl, headers=headers)
con = res.json()
print(json.dumps(con, indent=4))


@app.route('/', methods=['POST'])
def fetch_data():
    pass


if __name__ == '__main__':
    db.init_app(app)
    db.create_all()
    app.run(debug=True)