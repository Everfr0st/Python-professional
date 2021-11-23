def is_palindrome(string: str) -> bool:
    string = string.replace(" ","").lower() #Reemplazar espacios vacíos por cadenas vacías
    return string == string[::-1]
    

def run():
    print(is_palindrome(1000))

if __name__ == '__main__':
    run()
    