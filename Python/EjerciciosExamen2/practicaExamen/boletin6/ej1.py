# Ejercicio 1 - ENUNCIADO (comentado)
# ----------------------------------
# Validar un código postal de Madrid. Cinco números, los dos primeros siempre son el 28
# Ejemplo válido: 28032
#
# Lo que nos pide el enunciado:
# - La cadena debe consistir exactamente en 5 caracteres.
# - Todos esos caracteres deben ser dígitos (0-9).
# - Los dos primeros dígitos deben ser '2' seguido de '8' (es decir, la cadena empieza por '28').
#
# Objetivo del ejercicio:
# - Crear una función en Python que reciba una cadena y devuelva True si la cadena cumple
#   exactamente con el formato descrito, y False en caso contrario.
# - Acompañar la solución con una explicación completa de la expresión regular y de por qué
#   se usan ciertas funciones de Python para validación.

import re

def validar_cp_madrid(codigo: str) -> bool:
    """
    Valida códigos postales de Madrid tal y como pide el enunciado:
    - Deben ser exactamente 5 caracteres.
    - Todos dígitos.
    - Los dos primeros caracteres deben ser '28'.
    Devuelve True si válido, False si no.
    """

    # ================================================================
    # EXPLICACIÓN EXTENSA DE LA ESTRATEGIA Y DEL PATRÓN UTILIZADO
    # ================================================================
    #
    # ¿Por qué usamos expresiones regulares?
    # - Las expresiones regulares (regex) permiten describir patrones en cadenas de texto
    #   de forma precisa y concisa. Son especialmente útiles para validaciones de formato.
    #
    # ¿Qué es `import re` y por qué lo necesitamos?
    # - En Python, las funciones para trabajar con expresiones regulares están en el módulo estándar
    #   llamado 're'. Por eso antes de usar regex hacemos 'import re'.
    #
    # ¿Por qué usamos r"..." (raw string) para el patrón?
    # - En las expresiones regulares solemos escribir secuencias con la barra invertida `\`,
    #   por ejemplo `\d` para "dígito". En las cadenas normales de Python, `\` introduce secuencias
    #   de escape (por ejemplo '\n' salto de línea). Para evitar que Python interprete esas barras
    #   invertidas y que el patrón llegue tal cual al motor de regex, usamos raw strings:
    #       r"\d{3}"  en lugar de  "\\d{3}"
    #   Raw string significa "cadena cruda": Python no procesa las secuencias \n, \t, etc.
    #
    # ¿Qué función de `re` usamos y por qué?
    # - Usamos re.fullmatch(pattern, string). Esta función devuelve un objeto Match si **toda**
    #   la cadena corresponde exactamente al patrón, o None si no hay coincidencia completa.
    #   Es perfecta para validaciones donde no queremos aceptar parte de la cadena: queremos
    #   que toda la cadena cumpla la regla.
    #
    # Patrón que vamos a usar y explicación símbolo por símbolo:
    # ---------------------------------------------------------
    # pattern = r"^28\d{3}$"
    #
    # Desglose:
    # 1. ^  -> ANCLAJE de inicio:
    #    - Significa "inicio de la cadena".
    #    - Asegura que lo que siga a continuación aparezca justo desde el principio.
    #    - Si no pusiéramos ^ y usáramos re.search, podríamos coincidir en una subcadena
    #      dentro de una cadena más larga (por eso usamos fullmatch y además ^ para claridad).
    #
    # 2. 28 -> literales '2' y '8':
    #    - Estos son caracteres exactos, no expresiones. Indican que los dos primeros dígitos
    #      tienen que ser '2' y '8' en ese orden. No se permiten alternativas aquí.
    #
    # 3. \d -> clase de dígito:
    #    - \d representa cualquier carácter decimal en el rango 0-9 (es decir, un dígito).
    #    - Es equivalente a [0-9].
    #    - Se usa mucho porque es más corto y claro.
    #
    # 4. {3} -> cuantificador exacto:
    #    - Indica "exactamente 3 repeticiones" de lo que precede (aquí, de \d).
    #    - Por tanto \d{3} significa "tres dígitos exactamente".
    #
    # 5. $  -> ANCLAJE de fin:
    #    - Significa "final de la cadena".
    #    - Asegura que no haya caracteres extra después de los que hemos descrito.
    #
    # ¿Qué consigue la combinación ^28\d{3}$ ?
    # - Empieza en el inicio (^) -> '2' y '8' -> después exactamente 3 dígitos más (\d{3})
    #   -> final de la cadena ($).
    # - Total de caracteres = 2 (por '28') + 3 (por \d{3}) = 5 caracteres, todos dígitos,
    #   y los dos primeros exactamente 28.
    #
    # Alternativa equivalente:
    # - pattern_alt = r"^28[0-9]{3}$"
    #   Esto usa la clase explícita [0-9] en lugar de \d. Son equivalentes para dígitos ASCII.
    #
    # Posibles errores comunes que evita este patrón:
    # - No permitimos letras ni símbolos.
    # - No permitimos más o menos de 5 caracteres.
    # - No permitimos que la cadena empiece por algo distinto a '28'.
    #
    # ¿Y si la cadena tuviera espacios al principio o al final?
    # - re.fullmatch exige coincidencia completa; un espacio extra rompería la coincidencia.
    # - Si quisieras aceptar espacios y limpiarlos primero, convendría hacer: codigo.strip()
    #   antes de validar. Pero el enunciado pide explícitamente "cinco números", por tanto no
    #   deberíamos aceptar espacios.
    #
    # ================================================================
    # FIN DE LA EXPLICACIÓN EXTENSA
    # ================================================================

    # Patrón regex explicado arriba:
    pattern = r"^28\d{3}$"

    # Usamos re.fullmatch para forzar que toda la cadena coincida con el patrón.
    # re.fullmatch devuelve un objeto match si hay coincidencia total, o None si no.
    match = re.fullmatch(pattern, codigo)

    # Devolvemos True si match no es None (coincidió), en caso contrario False.
    return match is not None


# -----------------------
# EJEMPLOS / PRUEBAS
# -----------------------
if __name__ == "__main__":
    casos = [
        ("28032", True),   # ejemplo del enunciado - válido
        ("28000", True),   # válido: empieza por 28 y tiene 5 dígitos
        ("28123", True),   # válido
        ("27000", False),  # no válido: no empieza por 28
        ("28a32", False),  # no válido: contiene letra
        ("2803", False),   # no válido: solo 4 caracteres
        ("028032", False), # no válido: 6 caracteres
        ("28 032", False), # no válido: contiene espacio
        (" 28032", False), # no válido: espacio inicial
        ("28032\n", False) # no válido: salto de línea extra
    ]

    for valor, esperado in casos:
        resultado = validar_cp_madrid(valor)
        print(f"'{valor}' -> {resultado} (esperado: {esperado})")
        assert resultado == esperado, f"Fallo en el caso {valor}: esperado {esperado}"

    print("Todas las pruebas pasaron correctamente.")
