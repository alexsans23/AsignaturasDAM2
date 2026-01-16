import re

def validar_telefono_internacional(s: str) -> bool:
    """
    Valida un número de teléfono con prefijo internacional y formato específico.

    Formato válido según el enunciado:
        +34 912233444
    Es decir:
        +  -> signo más literal
        34 -> dos dígitos de prefijo (en este caso España)
        (espacio obligatorio)
        912233444 -> número de teléfono (9 dígitos)
    """
    pattern = r"^\+\d{2} \d{9}$"
    return re.fullmatch(pattern, s) is not None


# Pruebas
if __name__ == "__main__":
    pruebas = [
        ("+34 912233444", True),   # ✅ válido
        ("+34 655776655", True),   # ✅ válido
        ("34 912233444", False),   # ❌ falta el signo +
        ("+34912233444", False),   # ❌ falta el espacio después del prefijo
        ("+345 912233444", False), # ❌ prefijo con 3 dígitos
        ("+12 91223344", False),   # ❌ 8 dígitos (falta uno)
        ("+12 9122334444", False), # ❌ 10 dígitos (uno de más)
        ("+34 91a233444", False),  # ❌ letra dentro del número
        (" +34 912233444", False), # ❌ espacio al inicio
    ]
    for valor, esperado in pruebas:
        print(f"{valor!r}: {validar_telefono_internacional(valor)} (esperado: {esperado})")


"""
───────────────────────────────────────────────────────────────────────────────
🧩 EXPLICACIÓN DETALLADA DE LA EXPRESIÓN REGULAR: r"^\+\d{2} \d{9}$"
───────────────────────────────────────────────────────────────────────────────

| Fragmento | Significado | Comentario |
|------------|--------------|-------------|
| ^ | **Inicio de cadena** | Asegura que no haya nada antes (por ejemplo, espacios o texto extra). |
| \+ | **Signo + literal** | El `+` normalmente significa “una o más repeticiones”, pero aquí queremos el carácter `+` tal cual. Por eso lo escapamos con `\`. Si no lo escapáramos, `+` se interpretaría como un operador de repetición. |
| \d{2} | **Dos dígitos exactos** | `\d` representa un número (0–9). `{2}` significa “exactamente 2 veces”. Así obtenemos el prefijo internacional de dos cifras (por ejemplo, `34`). |
| (espacio literal) | **Espacio obligatorio** | Hay un espacio justo después del prefijo. Si falta, la validación falla (`+34912233444` sería incorrecto). |
| \d{9} | **Nueve dígitos exactos** | Representa el número de teléfono propiamente dicho. En España los números fijos/móviles suelen tener 9 dígitos. |
| $ | **Fin de cadena** | Asegura que la cadena termina justo después del último dígito (sin espacios o caracteres adicionales). |

🔎 En resumen visual:
^        → empieza la cadena  
\+       → debe tener un signo +  
\d{2}    → luego dos dígitos (prefijo internacional)  
(espacio)→ luego un espacio literal  
\d{9}    → luego nueve dígitos (teléfono)  
$        → y ahí termina la cadena  

✅ Ejemplo que cumple:  +34 912233444  
❌ Ejemplo que NO cumple:  +34912233444  (porque falta el espacio)
─
"""