from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
def root():
    return "<h1>Миссия Колонизация Марса</h1>"


@app.route("/index")
def index():
    return "И на Марсе будут яблони цвести!"


@app.route("/promotion")
def promotion():
    contents = """Человечество вырастает из детства.<br>
                Человечеству мала одна планета.<br>
                Мы сделаем обитаемыми безжизненные пока планеты.<br>
                И начнем с Марса!<br>
                Присоединяйся!<br>"""
    return contents


@app.route("/image_mars")
def image_mars():
    content = """
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Привет, Марс!</title>
    </head>
    <body>
        <h1>Жди нас, Марс!</h1>
        <img src="https://i.ibb.co/f4XDB2c/mars.png" alt="Фото Марса улетело"
        height=500 width=500>
        <br>Вот она какая, красная планета.
    </body>
</html>"""
    return content


@app.route("/promotion_image")
def promotion_image():
    content = f"""
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
        integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
        crossorigin="anonymous">
        <link rel="stylesheet" href="{url_for("static", filename="css/style.css")}">
        <title>Привет, Марс!</title>
    </head>
    <body>
        <h1>Жди нас, Марс!</h1>
        <img src="{url_for("static", filename="img/mars.png")}"
        alt="Фото Марса было съедено инопришеленцами"
        height=500 width=500>
        <div class="alert alert-primary" role="alert">
            Человечество вырастает из детства.
        </div>
        <div class="alert alert-danger" role="alert">
            Человечеству мала одна планета.
        </div>
        <div class="alert alert-warning" role="alert">
            Мы сделаем обитаемыми безжизненные пока планеты.
        </div>
        <div class="alert alert-dark" role="alert">
            И начнем с Марса!
        </div>
        <div class="alert alert-success" role="alert">
            Присоединяся!
        </div>
    </body>
</html>"""
    return content


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")

