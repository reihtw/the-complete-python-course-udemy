from flask import Flask, render_template


app = Flask(__name__)
posts = {
    0: {
        'title': 'Hello, World!',
        'content': 'This is my first blog post!'
    },

    1: {
        'title': 'Milimalist life',
        'content': 'Less is more!'
    },
}


@app.route('/')
def home():
    return 'Hello, world!'


@app.route('/post/<int:post_id>') # for example: /post/0
def post(post_id):
    post_ = posts.get(post_id)
    if not post_:
        return render_template('404.html', message=f'A post with id {post_id} was not found.')
    return render_template('post.html', post=post_)


if __name__ == '__main__':
    app.run(debug=True)