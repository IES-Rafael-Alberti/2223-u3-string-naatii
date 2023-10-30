ERROR001 = "ERROR 001: Insert a string"

def letterCounterWithCount(letter:str)->int:
    word = "banana"
    if type(letter) != str:
        raise ValueError(ERROR001)
    return word.count(letter)

if __name__=="__main__":
    try:
        char = input("Introduce a char: ")
        print(letterCounterWithCount(char))
    except ValueError:
        print(ValueError(ERROR001))