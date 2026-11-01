"""Módulo propio: muestra los resultados en una tabla con tabulate."""

from tabulate import tabulate


def mostrar_tabla(resultados: list[dict], monto_ars: float) -> None:
    """Muestra las cotizaciones y el total convertido en una tabla.

    Args:
        resultados: Lista de diccionarios con el nombre, la compra, la venta
            y el total en dólares de cada cotización.
        monto_ars: Monto en pesos argentinos que se convirtió.
    """
    filas = []

    for resultado in resultados:
        filas.append(
            [
                resultado["nombre"],
                resultado["compra"],
                resultado["venta"],
                resultado["total_usd"],
            ]
        )

    encabezados = ["Cotización", "Compra (ARS)", "Venta (ARS)", "Total (USD)"]

    print(f"\n💱 Convertimos {monto_ars:.2f} pesos a dólares\n")
    print(tabulate(filas, headers=encabezados, tablefmt="fancy_grid",
                   floatfmt=".2f"))
    print("\nEl total se calcula con el precio de venta.\n")
