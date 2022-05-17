from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Diva'}
    posts = [
        {
            'author': {'username': 'Ratna'},
            'body': 'Wow! Diva you are beautiful<3'
        },
        {
            'author': {'username': 'Ardellia'},
            'body': 'Doctor Stranger movie is worth the hype!'
        }
    ]
    return render_template('index.html', title='Home', user=user)