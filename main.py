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

from cotizaciones import armar_resultados, obtener_cotizaciones
from vista import mostrar_tabla


def pedir_monto() -> float:
    """Le pide al usuario un monto en pesos argentinos.

    Returns:
        El monto ingresado por el usuario como número.
    """
    entrada = input("💵 Ingresá un monto en pesos argentinos (ARS): ")
    return float(entrada)


def main() -> None:
    """Punto de entrada del programa."""
    monto = pedir_monto()
    cotizaciones = obtener_cotizaciones()
    resultados = armar_resultados(cotizaciones, monto)
    mostrar_tabla(resultados, monto)


if __name__ == "__main__":
    main()
