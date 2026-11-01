"""Módulo propio: consulta la cotización del dólar."""

import requests

URL_API = "https://dolarapi.com/v1/dolares"


def obtener_cotizaciones() -> list[dict]:
    """Descarga las cotizaciones del dólar desde la API pública.

    Returns:
        La lista de cotizaciones que devuelve la API. Cada cotización es un
        diccionario con las claves "casa", "nombre", "compra" y "venta".
    """
    respuesta = requests.get(URL_API, timeout=10)
    respuesta.raise_for_status()
    return respuesta.json()
