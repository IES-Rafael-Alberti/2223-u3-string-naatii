ERROR001 = "ERROR 001: Insert a string"
def invertedString(input:str)->str:
    """Escribe un bucle while que comience con el último carácter en la cadena y haga un recorrido hacia atrás hasta el primer carácter en la cadena, imprimiendo cada letra en una línea independiente.

    Args:
        input (str): Ingresed input by user

    Returns:
        str: Inverted string.
    """
    if type(input) != str:
        raise ValueError(ERROR001)
    counter = len(input)
    reverseString = ""
    while counter != 0:
        reverseString += input[counter-1]
        counter -= 1
    return reverseString
if __name__=="__main__":
    try:
        stringInput = input("Insert a string: ")
        for caracter in invertedString(stringInput):
            print(caracter)
    except ValueError:
        print(ValueError(ERROR001))