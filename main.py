import os
from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.fileadmin import FileAdmin

app = Flask(__name__)
app.secret_key = 'randomsecretkey'  # Needed for Flask-Admin

# Where you want FileAdmin to operate (change as needed)
file_path = os.path.join(os.path.dirname(__file__), 'files')
os.makedirs(file_path, exist_ok=True)  # Ensure directory exists

admin = Admin(app, name='FileAdmin Demo', template_mode='bootstrap3')
admin.add_view(FileAdmin(file_path, '/files/', name='Files'))

@app.route('/')
def index():
    return '<a href="/admin/">Go to FileAdmin</a>'

if __name__ == '__main__':
    app.run(debug=True)
