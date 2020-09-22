#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
        lenght = []
        for idx in range(list_length):
            try:
                lenght.append(my_list_1[idx] / my_list_2[idx])
            except (ValueError, TypeError):
                print("wrong type")
            except ZeroDivisionError:
                print("division by 0")
            except IndexError:
                print("out of range")
            finally:
                lenght.append(0)
        return(lenght)
