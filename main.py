from flask import Flask, request
import tweepy

app = Flask(__name__)

# Twitter APIキーを設定
consumer_key = os.environ["CONSUMER_KEY"]
consumer_secret = os.environ["CONSUMER_SECRET"]

html_form = """
<form action="/tweet" method="post">
    <textarea name="tweet" cols="60" rows="5"></textarea><br>
    <input type="submit" value="Tweet">
</form>
"""
@app.route("/")
def index():
    # Twitterログインボタンを表示
    twitter_login_url = auth.get_authorization_url()
    return '<a href="{}"><img src="https://g.twimg.com/dev/sites/default/files/images_documentation/sign-in-with-twitter-gray.png" alt="Sign in with Twitter"/></a>'.format(twitter_login_url)

@app.route("/callback")
def callback():
    # リクエストトークンからアクセストークンを取得
    auth.request_token = session['request_token']
    verifier = request.args.get('oauth_verifier')
    auth.get_access_token(verifier)

    # ツイート投稿用のHTMLフォームを表示
    html_form = """
    <form action="/tweet" method="post">
        <textarea name="tweet" cols="60" rows="5"></textarea><br>
        <input type="submit" value="Tweet">
    </form>
    """
    return html_form

@app.route("/tweet", methods=["POST"])
def tweet():

# Tweepyライブラリを初期化
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# ツイート内容を取得
tweet = request.form["tweet"]

# Twitter APIを使用してツイートを投稿
api.update_status(tweet)

return "<p style="color: red;">ツイートしました: {}</p>{}".format(tweet, html_form)
