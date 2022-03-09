import re
import requests
from flask import Flask, request, json
from werkzeug.utils import redirect
from services.services import FeedlyClient
from datetime import datetime
from models.tables import db, Articles, Categories

app = Flask(__name__)
myurl = "http://cloud.feedly.com/v3/streams/contents?streamId=user/bedb0992-50cc-45a1-9ab1-695746cac476/category/global.all"
headers = {'Authorization': 'OAuth ' + "Ay9NP0Hn12AnSomqA9fED2h-OxLMEZkQCBUsQvR1TQYIJGL0kGiTaZ-U4a1UgUvcMPGUbU1XPM_DduWyMTEEXI8pLJ7zQ2UD_4ns5FmNTM-1IgyFqF-kUM5Ie6OXjFipkNY8ZeF859F2pGrhrppYWi_ooqS8fUb8sDnmfbbdYx8mOrI7SSAFvasY8GlIXxQ9cxiDPhrgAKZUq2Mr-OCvWgMrbtb0gY6FhX-L28SEnAGP5AejQoGM3_yQ5S8:feedlydev"}
params = dict(count=10)
res = requests.get(url=myurl, headers=headers, params=params)
con = res.json()
print(json.dumps(con, indent=4))
"9kvTSXJ/FoV0tKjA81ehh0HicK5d+u3ZYbKAl6iUAKY=_17f6f94add3:cf0698:c8b06589"


data = con["items"]
for item in data:
    news_title = item["title"]
    url = item["alternate"][0]["href"]
    pub = int(round((data[0]["published"] / 1000), 10))
    published_at = datetime.fromtimestamp(pub)
    category_id = []
    news_content = []
    summary = item.get('summary')
    content = item.get('content')
    if summary:
        news_content = item["summary"]["content"][:100]
    elif content:
        news_content = item["content"]["content"][:100]
    elif not summary or not content:
        news_content = "null"
    if item["categories"][0]["label"] == "technology":
        category_id = 1
    elif item["categories"][0]["label"] == "business":
        category_id = 2
    elif item["categories"][0]["label"] == "sports":
        category_id = 3
    new_article = Articles(news_title=str(re.sub('[^A-Za-z0-9]+', ' ', news_title)),
                           url=str(url),
                           published_at=published_at,
                           news_content=str(news_content),
                           category_id=category_id)
    db.session.add(new_article)
    db.session.commit()


@app.route('/', methods=['POST'])
def fetch_data():
    pass


if __name__ == '__main__':
    db.init_app(app)
    db.create_all()
    app.run(debug=True)