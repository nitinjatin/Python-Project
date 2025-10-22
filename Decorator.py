def deco_datatype(func):
    def wrap(x):
        result = x
        if not isinstance(result , int):
            print("warning...")
        return result
    return wrap

#comment

@deco_datatype
def input_number(x):
    return type(x)


print(input_number("hola"))