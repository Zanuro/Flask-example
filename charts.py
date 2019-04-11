from io import BytesIO
import matplotlib.pyplot as plt
from user_database import data, MONTHS, get_city_temperature, get_city_humidity, CITIES


def get_main_image():
    """Rendering the scatter chart"""
    yearly_temp = []
    yearly_hum = []

    for city in data:
        yearly_temp.append(sum(get_city_temperature(city))/12)
        yearly_hum.append(sum(get_city_humidity(city))/12)

    plt.clf()
    plt.scatter(yearly_hum, yearly_temp, alpha=0.5)
    plt.title('Yearly Average Temperature/Humidity')
    plt.xlim(70, 95)
    plt.ylabel('Yearly Average Temperature')
    plt.xlabel('Yearly Average Relative Humidity')
    for i, txt in enumerate(CITIES):
        plt.annotate(txt, (yearly_hum[i], yearly_temp[i]))

    img = BytesIO()
    plt.savefig(img)
    img.seek(0)
    return img

