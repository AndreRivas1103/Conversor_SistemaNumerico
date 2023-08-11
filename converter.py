def decimal_to_other_bases(number):
    decimal = int(number)
    hexadecimal = hex(decimal)
    binary = bin(decimal)
    octal = oct(decimal)
    return hexadecimal, binary, octal

def other_bases_to_decimal(number, base):
    if base == "hex":
        return int(number, 16)
    elif base == "bin":
        return int(number, 2)
    elif base == "oct":
        return int(number, 8)

if __name__ == "__main__":
    input_number = input("Ingrese un número: ")
    input_base = input("Ingrese la base del número (hex/bin/oct): ")
    output_base = input("Ingrese la base de salida (hex/bin/oct): ")

    if input_base == "dec":
        converted_number = decimal_to_other_bases(input_number)
        print(f"Resultado: {converted_number[{'hex': 0, 'bin': 1, 'oct': 2}[output_base]]}")
    else:
        decimal_number = other_bases_to_decimal(input_number, input_base)
        if output_base == "dec":
            print(f"Resultado: {decimal_number}")
        else:
            converted_number = decimal_to_other_bases(decimal_number)
            print(f"Resultado: {converted_number[{'hex': 0, 'bin': 1, 'oct': 2}[output_base]]}")
