"""Módulo propio: consulta la cotización del dólar y hace la conversión."""

import requests

URL_API = "https://dolarapi.com/v1/dolares"
CASAS = ("oficial", "blue")


def obtener_cotizaciones() -> list[dict]:
    """Descarga las cotizaciones del dólar desde la API pública.

    Returns:
        La lista de cotizaciones que devuelve la API. Cada cotización es un
        diccionario con las claves "casa", "nombre", "compra" y "venta".
    """
    respuesta = requests.get(URL_API, timeout=10)
    respuesta.raise_for_status()
    return respuesta.json()


def convertir(monto_ars: float, venta: float) -> float:
    """Convierte un monto en pesos a dólares usando el precio de venta.

    Args:
        monto_ars: Monto en pesos argentinos.
        venta: Precio de venta del dólar.

    Returns:
        El monto equivalente en dólares.
    """
    return monto_ars / venta


def armar_resultados(cotizaciones: list[dict], monto_ars: float) -> list[dict]:
    """Se queda con el dólar oficial y el blue y les calcula el total.

    Args:
        cotizaciones: Lista de cotizaciones que devolvió la API.
        monto_ars: Monto en pesos argentinos a convertir.

    Returns:
        Una lista de diccionarios con el nombre de la cotización, su precio
        de compra, su precio de venta y el total convertido a dólares.
    """
    resultados = []

    for cotizacion in cotizaciones:
        if cotizacion["casa"] in CASAS:
            venta = float(cotizacion["venta"])
            resultados.append(
                {
                    "nombre": cotizacion["nombre"],
                    "compra": float(cotizacion["compra"]),
                    "venta": venta,
                    "total_usd": convertir(monto_ars, venta),
                }
            )

    return resultados
