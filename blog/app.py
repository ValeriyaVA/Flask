from flask import Flask

app = Flask(__name__)

count = 0


# Cоздайте базовый index view для обработки посещений на корень сайта.

@app.route("/")
def index():
    global count
    count += 1
    return f"Посещений на данный момент - {count}"

# обнулим счётчик
@app.route('/delete')
def delete_index():
    global count
    count = 0
    return f'Счетчик обнулен'
