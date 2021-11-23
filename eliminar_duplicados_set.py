random_list = [1, 1, 2, 6, 8, 5, 5, 4, 4]

def delete_duplicated(some_list):
    #print(some_list | some_list)
    print(list(set(some_list)))
    return list(set(some_list))
if __name__ == '__main__':
    delete_duplicated(random_list)