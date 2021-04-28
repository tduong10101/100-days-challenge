from flask import Flask, render_template
import requests
import post
app = Flask(__name__)
npoint = "https://api.npoint.io/5abcca6f4e39b4955965"
resp = requests.get(npoint)
posts = []
posts_data = resp.json()


for pt in posts_data:
    post_obj = post.Post(pt)
    posts.append(post_obj)

@app.route('/')
def home():
    return render_template("index.html",posts=posts)

@app.route('/blog/<int:num>')
def get_blog(num):
    post = [post for post in posts if post.id==num][0]
    return render_template("post.html",post=post)

if __name__ == "__main__":
    app.run(debug=True)
