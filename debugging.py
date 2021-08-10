def palindrome(string):
    try:
        if len(string) == 0:
            raise ValueError("Vacio")
            return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False

try:
    print(palindrome(""))
except TypeError:
    print("Solo strings")
else:
    print("Correcto")
finally:
    print("fin")