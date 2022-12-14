from flask import Flask, render_template

from post import Post

app = Flask(__name__)
blog_posts = Post().get_posts()


@app.route("/")
def home():
    return render_template("index.html", blog_posts=blog_posts)


@app.route("/post/<post_id>")
def get_blog(post_id):
    print(post_id)
    return render_template("post.html", post_id=int(post_id), blog_posts=blog_posts)


if __name__ == "__main__":
    app.run(debug=True)
