"""Versión web del conversor de divisas.

Levanta un servidor local con Flask y muestra en el navegador la misma
conversión que main.py hace por consola. Reutiliza el módulo propio
cotizaciones.py sin modificarlo.

Esto es un agregado: la versión de consola sigue funcionando con
`python main.py`.

La página y los estilos están separados del código:
    - templates/index.html: el HTML.
    - static/estilos.css: los estilos.

Ejecución:
    python app.py

Después abrir http://127.0.0.1:5000 en el navegador.
"""

import requests
from flask import Flask, render_template, request

from cotizaciones import armar_resultados, obtener_cotizaciones

app = Flask(__name__)


def convertir(entrada: str) -> dict:
    """Valida el monto ingresado y calcula las conversiones.

    Args:
        entrada: Monto en pesos argentinos tal como lo escribió el usuario.

    Returns:
        Un diccionario con la clave "resultados" (la lista de cotizaciones
        convertidas) y la clave "error" (el mensaje a mostrar). Si la
        conversión salió bien el error está vacío; si falló, la lista está
        vacía.
    """
    try:
        monto = float(entrada)
    except ValueError:
        return {"resultados": [], "error": "Lo ingresado no es un número."}

    if monto <= 0:
        return {
            "resultados": [],
            "error": "El monto tiene que ser mayor que cero.",
        }

    try:
        resultados = armar_resultados(obtener_cotizaciones(), monto)
    except requests.RequestException:
        return {
            "resultados": [],
            "error": "No se pudo consultar la cotización. ¿Hay internet?",
        }
    except ValueError as error:
        return {"resultados": [], "error": str(error)}
    except KeyError as error:
        return {
            "resultados": [],
            "error": f"A la API le faltó el dato {error}.",
        }
    except ZeroDivisionError:
        return {
            "resultados": [],
            "error": "La cotización vino en cero, no se puede dividir.",
        }

    return {"resultados": resultados, "error": ""}


@app.route("/")
def inicio() -> str:
    """Muestra el formulario y, si se ingresó un monto, la conversión.

    Returns:
        La página HTML renderizada.
    """
    entrada = request.args.get("monto", "")
    datos = {"resultados": [], "error": ""}

    if entrada:
        datos = convertir(entrada)

    return render_template(
        "index.html",
        monto=entrada,
        resultados=datos["resultados"],
        error=datos["error"],
    )


if __name__ == "__main__":
    app.run(debug=True)
