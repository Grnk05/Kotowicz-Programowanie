# from KiK_Lab02 import my_list


def my_first_function():
    '''
    Funkcja testująca operacje arytmetyczne przy danych x = 5 i y = 6.

    '''
    x = 5
    print(f'zmiennej x przypisano wartość {x}.')
    y = 6
    print(f'Zmiennej y przypisano wartość {y}.')
    s = x + y
    print(f'Suma obydwu zmiennych wynosi {s}.')
    r = y - x
    print(f'Różnica obydwu zmiennych wynosi {r}')
    m = x * y
    print(f'Wynik mnożenia obydwu zmiennych to {m}')
    d = y / x
    print(f'Wynik podzielenia zmiennej y przez zmienną x to {d}')
    p1 = x ** y
    p2 = y ** x
    print(f'Podniesienie x do potęgi y daje {p1}, a podniesienie y do potęgi x daje {p2}')
    RzD = 2024 % y
    print(f'Reszta z podzielenia liczby 2024 przez zmienną y wynosi {RzD}')
    DC = 2024 // x
    print(f'Wynik dzielenia całkowitego liczby 2024 przez zmienną x to {DC}')


def my_function02():
    x=100.2
    y=100
    r= y - x
    print(f'Wynik różnicy zmiennych y i x wynosi {r}')


def my_function03():
    x=2
    y=10000
    p=x**y
    print(f'Wynik spotęgowania zmiennej x do zmiennej y wynosi {p}')


def my_function03a():
    pass
    # x=2
    # y=1000000
    # p=x**y
    # print(f'Wynik spotęgowania zmiennej x do zmiennej y wynosi {p}')

def print_list():
    my_list = list((21, 30-21, 2//24, 'Filip', 'Strzymiński'))
    print(f'{my_list}')
    print(f'{my_list[0]}')
    print(f'{my_list[4]}')
    print(f'{my_list[-1]}')
    print(f'{my_list[1]}')
    print(f'{my_list[-4]}')
    my_list1 = my_list
    print(f'{my_list1}')

def print_tuple():
    my_tuple = (21, 30-21, 2 / 24, 'Filip', 'Strzymiński', 1)
    print(f'{my_tuple}')
    print(type (my_tuple))
    my_tuple_bez_nawiasow = 21, 30-21, 2/24, 'Filip', 'Strzymiński'
    print(f'{my_tuple_bez_nawiasow}')
    my_tuple2 = my_tuple + ([21, 2],)
    print(f'{my_tuple2}')
    my_tuple2[-1][1] +=1
    print(f'{my_tuple2}')


def print_dict():
    '''
    Funkcja używające słowników, wywołująca klucze, wartości, pary, oraz
    "update", eksplorująca podstawowe operacje na "dict"
    '''
    my_dict = {'age': 21, 'name': 'Filip', 'fname': 'Strzymiński', 'sex': 'Mężczyzna' }
    print(f'Słownik zawierający mój wiek, imię i nazwisko:{my_dict}')
    # my_dict_with_tuples = dict([('age', 21), ('name', 'Filip'), ('fname', 'Strzymiński') ])
    # print(f'Słownik z krotkami, te same info:{my_dict_with_tuples}')
    print(f'Mój wiek: {my_dict['age']}')
    print(f'Wszystkie klucze: {my_dict.keys()}')
    print(f'Wszystie wartości: {my_dict.values()}')
    print(f'Wszystkie pary (wartości i ich klucze obok siebie): {my_dict.items()}')
    # Poniżej są dwie wersje tego samego działania, jedne z operatorem a drugie z "update".
    my_dict['age'] += 1
    print(f'Mój wiek, ale wczoraj miałem urodziny i muszę go zmienić - wersja 1: {my_dict['age']}')
    my_dict.update({'age': 22})
    print(f'Mój wiek, ale wczoraj miałem urodziny i muszę go zmienić - wersja 2: {my_dict['age']}')



if __name__ == '__main__':
    print_dict()
    # print_tuple()
    # print_list()
    # my_function03a()
    # my_function03()
    # my_function02()
    # my_first_function()







