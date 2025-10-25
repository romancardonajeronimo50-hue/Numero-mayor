# numero_mayor.py

def numero_mayor(a, b):
    """
    Retorna el mayor entre a y b.
    Entradas: a (número), b (número)
    Salida: mayor de los dos (número)
    """
    # Si a es mayor que b,devuelve a; en cualquier otro caso (b>= a), devuelve b.
    return a if a > b else b


# --- Programa principal| ---
if __name__ == "__main__":
    print("=== COMPARAR DOS NÚMEROS ===")
    
    #pedimos los datos al usuario
    try:
        a = float(input("ingrese el primer número: "))
        b = float(input("ingrese el segundo número: "))
    except ValueError:
        print("⚠️ Error: ingrese valores numéricos validos (ej: 10, 3.5).")
        raise SystemExit(1)
    
    #LLamamos a la función
    mayor = numero_mayor(a,b)
    
    #mensaje especial si son iguales
    if a == b:
        print("Los numeros son iguales:", a)
    else:
        print("El mayor es:", mayor)