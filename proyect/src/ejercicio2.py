def whatItsSecuency(secuency:str)->str:
    """Dado que fruta es una variable de tipo cadena, ¿qué significa fruta[:]?

    Args:
        secuency (str): Secuency of string

    Returns:
        str: the solucion to the cuestion
    """
    return secuency[:]

if __name__=="__main__":
    fruta = "manzana"
    print(f"dado un string fruta -> {fruta} que es fruta[:]\nAquí tienes un ejemplo de lo que es fruta[:] -> {whatItsSecuency(fruta)}")