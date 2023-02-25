import urllib
import requests
from PIL import Image, ImageDraw, ImageFont

API_KEY = "k_y1o9mz55"


def ejercicio():
    # Cuantas serires de "Dragon Ball" hay registradas en IMDb

    filtro = "Dragon Ball"

    url = f"https://imdb-api.com/en/API/Search/{API_KEY}/{filtro}"

    response = requests.get(url)

    if not response.ok:
        print("La solicitud ha fallado con el error:", response.status_code)
        exit()

    data = response.json()
    num_items = len(data["results"])
    print(f"Hay {num_items} series de DragonBall")

    # La url del video del tráiler de la serie del año 1986

    filtro = "Dragon Ball 1986"

    urlBuscarSerie = f"https://imdb-api.com/en/API/Search/{API_KEY}/{filtro}"

    response = requests.get(urlBuscarSerie)

    if not response.ok:
        print("La solicitud ha fallado con el error:", response.status_code)
        exit()

    data = response.json()
    idSerie = data["results"][0]["id"]

    urlTrailer = f"https://imdb-api.com/en/API/Trailer/{API_KEY}/{idSerie}"

    responseTrailer = requests.get(urlTrailer)

    series_data = responseTrailer.json()
    trailer_url = series_data["linkEmbed"]
    print(f"Trailer: {trailer_url}")

    # El total de episodios que tiene la primera temporada

    temporada = 1

    urlTemporada = f"https://imdb-api.com/en/API/SeasonEpisodes/{API_KEY}/{idSerie}/{temporada}"

    responseTemporada = requests.get(urlTemporada)

    if not response.ok:
        print("La solicitud ha fallado con el error:", responseTemporada.status_code)
        exit()

    data = responseTemporada.json()
    num_items = len(data["episodes"])
    print(f"Hay {num_items} episodios en la temporada {temporada}")

    # En que día se emitió el ultimo episodio de esa temporada y su argumento.

    episodio = data["episodes"][len(data["episodes"]) - 1]
    fecha = episodio["released"]
    argumento = episodio["plot"]
    print(f"El último episodio salió el {fecha}")
    print(f"Su argumento: {argumento}")

    # Un archivo jpg con el cartel anunciador de la película Akira de Kutsuhiro Otomo (1988) con una resolución de
    # 2000x3000px y otro archivo jpg con un reporte completo con la información de la película

    filtro = "Akira 1988"
    url = f"https://imdb-api.com/en/API/SearchMovie/{API_KEY}/{filtro}"

    response = requests.get(url)

    if not response.ok:
        print("La solicitud ha fallado con el error:", response.status_code)
        exit()

    data = response.json()
    pelicula = data["results"][0]

    poster = pelicula["image"]
    poster_data = requests.get(poster).content

    with open('akira_poster.jpg', 'wb') as f:
        f.write(poster_data)

    poster_image = Image.open('akira_poster.jpg')
    poster_image = poster_image.resize((2000, 3000))
    poster_image.save('akira_poster_resized.jpg')

    idPelicula = pelicula["id"]

    url = f"https://imdb-api.com/en/API/Report/{API_KEY}/{idPelicula}"

    report = requests.get(url)

    with open('akira_report.jpg', 'wb') as f:
        f.write(report.content)
