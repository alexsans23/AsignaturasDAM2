import re

# 1) Código postal de Madrid: cinco números, los dos primeros siempre '28'
def validar_cp_madrid(s: str) -> bool:
    """
    Valida códigos postales de Madrid: deben tener 5 dígitos y empezar por '28'.
    Ejemplo válido: '28032'
    """
    pattern = r"^28\d{3}$"  # '28' + exactamente 3 dígitos más (total 5)
    return re.fullmatch(pattern, s) is not None


# 2) Número de teléfono (genérico): asumimos 8 dígitos seguidos (según ejemplo)
def validar_telefono(s: str) -> bool:
    """
    Valida un número de teléfono con 8 dígitos seguidos (ejemplo: '91345566').
    Si tu examen requiere otro formato (por ejemplo con prefijos o espacios),
    habría que adaptarlo.
    """
    pattern = r"^\d{8}$"  # exactamente 8 dígitos
    return re.fullmatch(pattern, s) is not None


# 3) Teléfono móvil: debe empezar por 6, 7 u 8 y tener 9 dígitos (ejemplo: '655776655')
def validar_movil(s: str) -> bool:
    """
    Valida móviles españoles típicos: 9 dígitos y primer dígito 6,7 u 8.
    """
    pattern = r"^[678]\d{8}$"  # primer dígito 6/7/8 + 8 dígitos más (total 9)
    return re.fullmatch(pattern, s) is not None


# 4) Teléfono con prefijo internacional: '+' + 2 dígitos + espacio + número (ejemplo: '+34 912233444')
def validar_telefono_internacional(s: str) -> bool:
    """
    Valida formato: +CC NNNNNNNNN where CC = dos dígitos de código país,
    y N... es el número local de 9 dígitos (según ejemplo).
    """
    pattern = r"^\+\d{2} \d{9}$"  # + + 2 dígitos + espacio + 9 dígitos
    return re.fullmatch(pattern, s) is not None


# 5) Dos palabras separadas por único espacio, sin números, ambas empiezan por mayúscula
def validar_dos_palabras(s: str) -> bool:
    """
    Valida dos palabras separadas por un único espacio.
    Cada palabra debe empezar por letra mayúscula y contener solo letras (añadimos acentos y ñ).
    Permitimos que la palabra tenga solo 1 letra (por eso usamos * para el resto).
    """
    # Nota: incluimos letras acentuadas y Ñ/ñ para español.
    letters = "A-Za-zÁÉÍÓÚáéíóúÑñ"
    pattern = rf"^[A-ZÁÉÍÓÚÑ][{letters}]* [A-ZÁÉÍÓÚÑ][{letters}]*$"
    return re.fullmatch(pattern, s) is not None

"""
El * significa “cero o más repeticiones”.
 Así, después de la primera mayúscula, pueden venir letras
minúsculas o mayúsculas, o incluso ninguna (lo que permitiría
 una palabra de una sola letra como “A”). No se permiten
números porque el conjunto solo incluye letras.
"""


# 6) Clave con formato XX00-xxX-00 (X mayúscula, x minúscula, 0 dígito)
def validar_clave_personal(s: str) -> bool:
    """
    Formato exacto: 2 mayúsculas, 2 dígitos, '-', 2 minúsculas, 1 mayúscula, '-', 2 dígitos.
    Ejemplo: 'AB12-xyZ-75'
    """
    pattern = r"^[A-Z]{2}\d{2}-[a-z]{2}[A-Z]-\d{2}$"
    return re.fullmatch(pattern, s) is not None


# 7) Tarjeta de crédito: cuatro grupos de cuatro números separados por espacio, espacio, MM/YY (mes 01-12)
def validar_tarjeta_credito(s: str) -> bool:
    """
    Valida '1234 5678 9012 3456 03/25' con mes entre 01 y 12.
    """
    # (?:\d{4} ){3}\d{4}  -> 4 grupos de 4 dígitos separados por espacio
    # (0[1-9]|1[0-2])\/\d{2} -> mes válido MM/YY
    pattern = r"^(?:\d{4} ){3}\d{4} (0[1-9]|1[0-2])\/\d{2}$"
    return re.fullmatch(pattern, s) is not None


# 8) IBAN español: empieza por 'ES' y luego 22 dígitos (aceptamos espacios intercalados)
def validar_iban_es(s: str) -> bool:
    """
    Valida un IBAN español sencillo:
    - Debe empezar por 'ES'
    - Debe contener 22 dígitos después de 'ES' (las separaciones por espacio son permitidas)
    Ejemplo: 'ES61 1234 3456 42 0456323532'
    """
    import re

    def validar_iban_es(s: str) -> bool:
        pattern = r"^ES\d{2} \d{4} \d{4} \d{2} \d{10}$"
        return re.fullmatch(pattern, s) is not None

    # Primero comprobamos que empieza por ES (mayúsculas) y sólo contiene dígitos y espacios después
    if not s.startswith("ES"):
        return False
    resto = s[2:]  # parte después de 'ES'
    # Eliminamos espacios para contar dígitos
    digits_only = resto.replace(" ", "")
    # Debe ser exactamente 22 dígitos
    if not (digits_only.isdigit() and len(digits_only) == 22):
        return False
    # Opcional: podríamos validar más (checksum IBAN) pero el enunciado solo pide formato y 'ES' inicial.
    return True


# 9) Número que tenga como mínimo 4 cifras y máximo 8 cifras
def validar_numero_4_8(s: str) -> bool:
    """
    Valida cadenas que sean solo dígitos y tengan entre 4 y 8 cifras.
    """
    pattern = r"^\d{4,8}$"
    return re.fullmatch(pattern, s) is not None


# 10) Dirección IP pública de clase C: cuatro bytes separados por punto; los dos primeros siempre 192.168.
def validar_ip_clase_c(s: str) -> bool:
    """
    Valida una IP de clase C donde los dos primeros bytes deben ser 192.168
    y los dos últimos bytes pueden valer de 0 a 255.
    Ejemplo: '192.168.30.30'
    """
    # patrón para un byte (0-255)
    byte = r"(?:25[0-5]|2[0-4]\d|1?\d{1,2})"
    pattern = rf"^192\.168\.{byte}\.{byte}$"
    return re.fullmatch(pattern, s) is not None


# --- PRUEBAS RÁPIDAS con los ejemplos del enunciado ---
if __name__ == "__main__":
    ejemplos = {
        "cp": ("28032", validar_cp_madrid),
        "tel": ("91345566", validar_telefono),
        "movil": ("655776655", validar_movil),
        "internac": ("+34 912233444", validar_telefono_internacional),
        "dos_pal": ("Hola Mundo", validar_dos_palabras),
        "clave": ("AB12-xyZ-75", validar_clave_personal),
        "tarjeta": ("1234 5678 9012 3456 03/25", validar_tarjeta_credito),
        "iban": ("ES61 1234 3456 42 0456323532", validar_iban_es),
        "num": ("12345", validar_numero_4_8),
        "ip": ("192.168.30.30", validar_ip_clase_c),
    }

    for nombre, (ej, func) in ejemplos.items():
        print(f"{nombre}: {ej} -> {func(ej)}")
