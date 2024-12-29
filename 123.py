value = 10

def outer_function(value):
    value = 20

    def inner_function(value):
        value += 30
        print(f'inner_function value: {value}')  # Печатаем value.

    inner_function(value)
    print(f'outer_function value: {value}')  # Печатаем value.

    
outer_function(value)

print(f'global value: {value}')  # Печатаем value