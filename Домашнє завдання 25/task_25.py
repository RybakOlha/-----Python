def analyze_input(input_str):
    input_str = input_str.replace(',', '.')
    if input_str.isdigit():
        return f"Ви ввели {'нуль' if input_str == '0' else 'додатне ціле число: ' + input_str.lstrip('0')}"
    elif input_str.count('.') == 1 and input_str.replace('.', '').replace('0', '') == '':
        return 'Ви ввели нуль'
    elif input_str.count('.') == 1 and input_str.replace('.', '').isdigit():
        return f"Ви ввели дробове додатне число: {float(input_str)}"
    elif input_str.startswith('-'):
        input_var = input_str[1:]
        if input_var.isdigit():
            return f"Ви ввели ціле відʼємне число: -{input_var.lstrip('0')}"
        if input_var.count('.') == 1 and input_var.replace('.', '').isdigit():
            return f"Ви ввели відʼємне дробове число: -{float(input_var)}"
    return f"Ви ввели некоректне число: {input_str}"


if __name__ == '__main__':
    while True:
        input_str = input('Уведіть число або exit (вихід, в, quit, e, q) для виходу: ')
        if input_str.lower() in ['вихід', 'в', 'exit', 'quit', 'e', 'q']:
            break
        print(analyze_input(input_str))


