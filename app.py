from flask import Flask, render_template, send_file

from charts import get_main_image, get_city_image
from user_database import data

app = Flask(__name__)


@app.route('/')
def main():
    """Entry point; the view for the main page"""
    cities = [(record.city_id, record.city_name) for record in data]
    return render_template('main.html', cities=cities)


@app.route('/main.png')
def main_plot():
    """The view for rendering the scatter chart"""
    img = get_main_image()
    return send_file(img, mimetype='image/png', cache_timeout=0)

@app.route('/city/<int:city_id>')
def city(city_id):
    """Views for the city details"""
    city_record = data.get(city_id)
    return render_template('city.html', city_name=city_record.city_name, city_id=city_id,
                           city_climate=city_record.city_climate)


@app.route('/city<int:city_id>.png')
def city_plot(city_id):
    """Views for rendering city specific charts"""
    img = get_city_image(city_id)
    return send_file(img, mimetype='image/png', cache_timeout=0,)

def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
