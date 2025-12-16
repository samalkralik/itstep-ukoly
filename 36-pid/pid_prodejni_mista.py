import json
from urllib import request

json_path = "python/36/pid_prodejni_mista.json"


def download_data():
    url = "https://data.pid.cz/pointsOfSale/json/pointsOfSale.json"

    with request.urlopen(url) as response:
        data = json.load(response)

        with open(json_path, mode="w", encoding="utf-8") as file:
            json.dump(data, file)


def read_data():
    with open(json_path, mode="r", encoding="utf-8") as file:
        return json.load(file)


def generate_page(item):
    opening_hours = ", ".join([oh["hours"] for oh in item["openingHours"]])

    html = f"""
    <html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        <style>
           body {{
                font-family: sans-serif;
                background-color: #f4f4f9;
                margin: 0;
                padding: 20px;
            }}
        </style>
    </head>
    <body>
        <h1>{item['name']}</h1>
        <p>{item['address']}</p>
        <p>{opening_hours}</p>
        <p>{item['lat']}</p>
        <p>{item['lon']}</p>
    </body>
    </html>
    """

    with open(
        f"python/36/html-pages/{item['id']}.html", mode="w", encoding="utf-8"
    ) as file:
        file.write(html)


def generate():
    data = read_data()

    for item in data:
        generate_page(item)


generate()

generate_page(
    {
        "id": "dp2",
        "type": "ticketMachine",
        "name": "Grand Hotel International",
        "address": "Koulova 1501/15, Dejvice, Praha 6",
        "openingHours": [{"from": 0, "to": 6, "hours": "5:00-24:00"}],
        "lat": 50.1093445,
        "lon": 14.3935671,
        "services": 196608,
        "payMethods": 1,
    }
)
