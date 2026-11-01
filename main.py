"""Conversor de divisas.

Pide un monto en pesos argentinos y consulta la cotización del dólar en una
API pública.
"""

from cotizaciones import obtener_cotizaciones


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

    print(f"Ingresaste {monto} pesos.")

    for cotizacion in cotizaciones:
        print(cotizacion["casa"], cotizacion["venta"])


if __name__ == "__main__":
    main()
