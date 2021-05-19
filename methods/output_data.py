def output_data(filename, value):
    with open(filename, 'w') as file:
        file.write(str(value))
