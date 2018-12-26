from app.views.app_views import create_app

app = create_app()
app.config['SECRET_KEY'] = 'ZOE'
# my_secret_key = app.config['SECRET_KEY']

if __name__ == '__main__':
    app.run(debug=True)