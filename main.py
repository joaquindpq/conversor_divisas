"""Conversor de divisas.

Pide un monto en pesos argentinos para después convertirlo a dólares.
"""


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
    print(f"Ingresaste {monto} pesos.")


if __name__ == "__main__":
    main()
