"""Conversor de divisas con cotización en vivo.

Le pide al usuario un monto en pesos argentinos, consulta la cotización
actual del dólar en una API pública y muestra en una tabla cuántos dólares
equivalen según el dólar oficial y el dólar blue.

El código está dividido en módulos propios:
    - cotizaciones.py: consulta la API y hace la conversión.
    - vista.py: muestra los resultados en una tabla.

Ejecución:
    python main.py
"""

import requests

from cotizaciones import armar_resultados, obtener_cotizaciones
from vista import mostrar_tabla


def pedir_monto() -> float:
    """Le pide al usuario un monto en pesos argentinos.

    Returns:
        El monto ingresado por el usuario como número.

    Raises:
        ValueError: Si lo ingresado no es un número o no es mayor que cero.
    """
    entrada = input("Ingresá un monto en pesos argentinos (ARS): ")

    try:
        monto = float(entrada)
    except ValueError:
        raise ValueError(f"'{entrada}' no es un número.")

    if monto <= 0:
        raise ValueError("El monto tiene que ser mayor que cero.")

    return monto


def main() -> None:
    """Punto de entrada del programa."""
    try:
        monto = pedir_monto()
        cotizaciones = obtener_cotizaciones()
        resultados = armar_resultados(cotizaciones, monto)
        mostrar_tabla(resultados, monto)
    except ValueError as error:
        print(f"Error: {error}")
    except requests.RequestException as error:
        print(f"Error: no se pudo consultar la API: {error}")
    except KeyError as error:
        print(f"Error: a la API le faltó el dato {error}.")
    except ZeroDivisionError:
        print("Error: la cotización vino en cero, no se puede dividir.")


if __name__ == "__main__":
    main()
