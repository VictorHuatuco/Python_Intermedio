def main():
    my_list = [1, "HELLO", True, 4.5]
    my_dict = {"firstname": "Victor", "lastname": "Huatuco"}

    super_list = [
        {"firstname": "Pervo", "lastname": "Golinea"},
        {"firstname": "Etrisco", "lastname": "Satrina"},
        {"firstname": "Abrey", "lastname": "Vertira"},
        {"firstname": "Sorbe", "lastname": "Gatche"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-14, -58, -2, 1, 2],
        "floting_nums": [1.42, 5.762, 2.62]
    }
    for key, value in super_dict.items():
        print(key, "-", value)
    
    for i in super_list:
        print(i.items())
    
    for i in super_list:
        for key, values in i.items():
            print(key,": ", values);

if __name__ == '__main__':
    main()