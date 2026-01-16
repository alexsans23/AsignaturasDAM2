# Ejercicio 2 - ENUNCIADO (comentado)
# ----------------------------------
# Validar un número de teléfono
# Ejemplo válido: 91345566
#
# A partir del enunciado:
# - Nos dan un ejemplo: '91345566' — que es una cadena de 8 dígitos.
# - El enunciado no menciona prefijos, espacios ni guiones, así que seguiremos el
#   formato más simple: un teléfono consta de exactamente 8 dígitos seguidos.
# - Si en el examen pidieran también formatos con espacios o guiones habría que
#   adaptar la expresión, pero aquí asumimos exactamente 8 dígitos contiguos.
#
# Objetivo:
# - Implementar una función que reciba una cadena y devuelva True si es un número
#   de teléfono en el formato especificado (8 dígitos), False si no.
# - Explicar con mucho detalle por qué se usan ciertas partes de la regex y qué
#   significan los símbolos usados.

import re

def validar_telefono(s: str) -> bool:
    """
    Valida un número de teléfono en el formato simple indicado:
    - Exactamente 8 caracteres.
    - Todos dígitos (0-9).
    - Sin espacios, guiones ni otros símbolos.
    Ejemplo válido: '91345566'
    Devuelve True si válido, False si no.
    """

    # ================================================================
    # EXPLICACIÓN EXTENSA (símbolo a símbolo y razonamiento)
    # ================================================================
    #
    # 1) ¿Por qué usar expresiones regulares?
    #    - Las regex permiten describir "patrones" de texto de forma compacta.
    #    - Aquí el patrón es simple: "ocho dígitos seguidos".
    #
    # 2) ¿Por qué import re?
    #    - En Python el módulo 're' contiene funciones para regex (match, search, sub...).
    #
    # 3) ¿Qué función usar? -> re.fullmatch
    #    - re.fullmatch(patron, texto) devuelve un objeto Match si **toda** la cadena
    #      coincide exactamente con el patrón. Si hay cualquier carácter extra o falta
    #      alguno, devuelve None.
    #    - Esto es ideal para validaciones estrictas de formato (como la del examen).
    #
    # 4) Raw string r"..."
    #    - Usamos r"..." para que Python no interprete las barras invertidas `\` como
    #      escapes de cadena (por ejemplo '\n'). Queremos que `\d` llegue tal cual al motor.
    #
    # 5) Patrón propuesto: r"^\d{8}$"
    #
    #    Desglose detallado:
    #    - ^  (acento circunflejo) -> ANCLAJE DE INICIO
    #         * Significa "el inicio de la cadena".
    #         * Garantiza que lo que sigue empiece justo desde el primer carácter.
    #         * Si no se usara y se usara re.search, podríamos coincidir con una subcadena
    #           dentro de una cadena más larga. Con fullmatch es redundante, pero es
    #           habitual escribir ^ y $ para dejarlo explícito.
    #
    #    - \d -> CLASE PREDEFINIDA "dígito"
    #         * Representa cualquier carácter decimal equivalente a [0-9].
    #         * Es más legible que escribir [0-9] y es estándar en regex.
    #
    #    - {8} -> CUANTIFICADOR EXACTO
    #         * Indica "exactamente 8 repeticiones" de lo que está antes (aquí \d).
    #         * Por tanto \d{8} significa "ocho dígitos consecutivos".
    #
    #    - $  -> ANCLAJE DE FIN
    #         * Significa "final de la cadena".
    #         * Garantiza que no haya más caracteres después de los 8 dígitos.
    #
    #    Combinando: ^\d{8}$ significa "desde el inicio hasta el final de la cadena
    #    hay exactamente 8 dígitos".
    #
    # 6) ¿Por qué no usar +, * o ? en este caso?
    #    - + significaría "una o más repeticiones", * "cero o más", ? "cero o una".
    #    - Estas no servirían para limitar exactamente a 8 caracteres: permitirían
    #      longitudes variables. Para una longitud fija usamos {8}.
    #
    # 7) Alternativa con [0-9]:
    #    - r"^[0-9]{8}$" es equivalente funcionalmente a r"^\d{8}$".
    #    - [0-9] es explícito y no depende de clases predefinidas; \d es más corto.
    #
    # 8) Casos que rechazamos con este patrón (según el enunciado):
    #    - Cadenas con menos de 8 dígitos (ej. "9134556")
    #    - Cadenas con más de 8 dígitos (ej. "913455661")
    #    - Cadenas con espacios o guiones (ej. "9134 5566" o "9134-5566")
    #    - Cadenas con letras o caracteres especiales.
    #
    # 9) Qué hacer si el examen pide formatos con separadores:
    #    - Si se permitieran espacios o guiones entre bloques podríamos usar:
    #         r"^\d{4}[- ]?\d{4}$"
    #      que acepta "12345678", "1234 5678" o "1234-5678".
    #    - Si se aceptaran varios separadores opcionales entre cualquier grupo:
    #         r"^(?:\d{2}[- ]?){3}\d{2}$"  (más complejo y depende del patrón exacto)
    #    - Pero **ojo**: no implementes formatos alternativos si el enunciado no los pide.
    #
    # 10) Por qué no hacemos strip() automáticamente
    #    - El enunciado exige el formato; aceptar espacios podría ocultar errores en entrada.
    #    - Si quieres una versión "tolerante" puedes aplicar s = s.strip() y luego validar.
    #
    # ================================================================
    # FIN DE LA EXPLICACIÓN EXTENSA
    # ================================================================

    pattern = r"^\d{8}$"  # 8 dígitos exactos, del inicio al final

    # Usamos re.fullmatch para comprobar la coincidencia exacta;
    # equivaldría en este caso a re.match con ^ y $ pero fullmatch expresa la intención.
    return re.fullmatch(pattern, s) is not None


# -----------------------
# EJEMPLOS / PRUEBAS
# -----------------------
if __name__ == "__main__":
    casos = [
        ("91345566", True),   # ejemplo del enunciado - válido
        ("12345678", True),   # válido: 8 dígitos
        ("01234567", True),   # válido: 8 dígitos (empieza por 0 es aceptable si no se especifica lo contrario)
        ("9134556", False),   # no válido: 7 dígitos
        ("913455661", False), # no válido: 9 dígitos
        ("9134 5566", False), # no válido: contiene espacio
        ("9134-5566", False), # no válido: contiene guion
        ("91A45566", False),  # no válido: contiene letra
        (" 91345566", False), # no válido: espacio inicial
        ("91345566\n", False) # no válido: salto de línea al final
    ]

    for valor, esperado in casos:
        resultado = validar_telefono(valor)
        print(f"'{valor}' -> {resultado} (esperado: {esperado})")
        assert resultado == esperado, f"Fallo en el caso {valor}: esperado {esperado}"

    print("Todas las pruebas del ejercicio 2 pasaron correctamente.")
