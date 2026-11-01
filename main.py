"""Conversor de divisas con cotización en vivo.

Le pide al usuario un monto en pesos argentinos, consulta la cotización
actual del dólar en una API pública y calcula cuántos dólares equivalen
según el dólar oficial y el dólar blue.
"""

from cotizaciones import armar_resultados, obtener_cotizaciones


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

    for resultado in resultados:
        print(resultado["nombre"], resultado["total_usd"])


if __name__ == "__main__":
    main()
