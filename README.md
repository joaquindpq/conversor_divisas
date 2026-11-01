# Conversor de Divisas (cotización en vivo)

Proyecto del **Ejercicio Avanzado 1** (Grupo 1, Unidad 11). Convierte un
monto en pesos argentinos a dólares usando la cotización **en vivo** del
dólar oficial y del dólar blue, y muestra el resultado en una tabla por
consola.

## ¿Qué hace?

1. Le pide al usuario un monto en pesos argentinos (ARS).
2. Consulta la cotización actual del dólar en la API pública
   [dolarapi.com](https://dolarapi.com/v1/dolares).
3. Convierte ese monto con el precio de **venta** de cada cotización, que es
   el precio al que se compran dólares con pesos:

   ```python
   total_usd = monto_ars / venta
   ```

4. Muestra una tabla con el nombre de la cotización, su precio de compra, su
   precio de venta y el total convertido a dólares.

### Ejemplo de uso

```text
💵 Ingresá un monto en pesos argentinos (ARS): 150000

💱 Convertimos 150000.00 pesos a dólares

╒══════════════╤════════════════╤═══════════════╤═══════════════╕
│ Cotización   │   Compra (ARS) │   Venta (ARS) │   Total (USD) │
╞══════════════╪════════════════╪═══════════════╪═══════════════╡
│ Oficial      │        1510.00 │       1560.00 │         96.15 │
├──────────────┼────────────────┼───────────────┼───────────────┤
│ Blue         │        1545.00 │       1565.00 │         95.85 │
╘══════════════╧════════════════╧═══════════════╧═══════════════╛

El total se calcula con el precio de venta.
```

## Librerías de terceros usadas

- [Requests](https://requests.readthedocs.io/) → hace la petición HTTP a la
  API de cotizaciones.
- [tabulate](https://pypi.org/project/tabulate/) → imprime los resultados en
  formato de tabla.

## Estructura

```text
conversor_divisas/
├── .venv/              # entorno virtual (NO se sube a Git)
├── .gitignore          # ignora .venv/ y __pycache__/
├── assets/             # logo de la institución
├── main.py             # punto de entrada: pide el monto y maneja errores
├── cotizaciones.py     # módulo propio: consulta la API y convierte
├── vista.py            # módulo propio: muestra la tabla con tabulate
├── requirements.txt    # dependencias congeladas con pip freeze
└── README.md
```

## Requisitos

- Python 3.9 o superior.
- Conexión a internet (la cotización se consulta en vivo).

## Cómo crear el entorno virtual e instalar las dependencias

```bash
# 1. Entrar a la carpeta del proyecto
cd conversor_divisas

# 2. Crear el entorno virtual
python -m venv .venv

# 3. Activarlo
#    Linux / Mac:
source .venv/bin/activate
#    Windows:
.venv\Scripts\activate

# 4. Instalar las dependencias
pip install -r requirements.txt
```

Si preferís instalarlas a mano: `pip install requests tabulate`.

## Cómo ejecutarlo

```bash
python main.py
```

Cuando te pregunte, ingresá por ejemplo `150000` y vas a ver la tabla con las
dos cotizaciones y el total en dólares.

## Manejo de errores

El programa avisa con un mensaje claro en lugar de cortarse cuando:

- El monto no es un número → `❌ 'hola' no es un número.`
- El monto es cero o negativo → `❌ El monto tiene que ser mayor que cero.`
- No hay internet o la API está caída → `❌ No se pudo consultar la API: ...`
- La API no trae el oficial y el blue →
  `❌ La API no devolvió el dólar oficial y el blue.`
- A la API le falta un dato → `❌ A la API le faltó el dato 'venta'.`
- La cotización viene en cero →
  `❌ La cotización vino en cero, no se puede dividir.`

## Detalles técnicos

- Manejo de errores con `try` / `except` y excepciones **específicas**
  (`ValueError`, `requests.RequestException`, `KeyError`,
  `ZeroDivisionError`), nunca un `except:` vacío.
- Todas las funciones documentadas con **docstrings**.
- **Anotación de tipos** en los parámetros y en los valores de retorno.
- Código siguiendo **PEP8** (`snake_case`, 4 espacios, imports arriba,
  líneas de hasta 79 caracteres).
- Código dividido en **módulos propios** (`cotizaciones.py` y `vista.py`)
  además de `main.py`.
- `requirements.txt` generado con `pip freeze > requirements.txt`.

## Integrantes

- Joaquín Pereyra
