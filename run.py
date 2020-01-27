from flask_blog import app

posts = [
    {
        'author': "Gaurav Menezes",
        'title': "Blog Post 1",
        "content": "First Post Content",
        "date_posted": "November 11, 1994"
    },
    {
        'author': "Shashwat Gupta",
        'title': "Blog Post 2",
        "content": "Second Post Content",
        "date_posted": "November 02, 1998"
    },
]

#Routes methods

if __name__ == '__main__':
    app.run(debug=True)