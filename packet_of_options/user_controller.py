from .user_logic import options_choiсe,OPTIONS




def main():                        # отвечает за обработку
    options_point = 10000000 # неважно какое число, главное,чтоб цикл while работал
    while options_point:
        options_point = options_choiсe()
        OPTIONS[options_point][1]()  # 1 символ?





