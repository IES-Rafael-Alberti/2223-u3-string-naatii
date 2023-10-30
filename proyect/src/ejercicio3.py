ERROR001 = "ERROR 001: Insert a string"

def letterCounter(word:str, letter)->int:
    """Tienes este código:

    palabra = 'banana'
    contador = 0
    for letra in palabra:
        if letra == 'a':
            contador = contador + 1
    print(contador)
    Encapsúlalo en una función llamada cuenta, y hazla genérica de tal modo que pueda aceptar una cadena y una letra como argumentos.

    Args:
        word (str): The word ingresed by user
        letter (_type_): letter to count introduce by user

    Raises:
        ValueError: Error because the input will be different a string

    Returns:
        int: Counter of letters in string
    """
    if type(word) != str and type(letter) != str:
        raise ValueError(ERROR001)
    counter = 0 
    for char in word:
        if char == letter:
            counter += 1
    return counter

if __name__=="__main__":
    try:
        word = input("Introduce a word: ")
        char = input("Introduce a char: ")
        print(letterCounter(word, char))
    except ValueError:
        print(ValueError(ERROR001))