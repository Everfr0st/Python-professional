

def remove_duplicates(some_list):
    whitout_duplicate = []
    for i in some_list:
        if i not in whitout_duplicate:
            whitout_duplicate.append(i)
    return whitout_duplicate

def run ():
    random_list = [1, 1, 2, 6, 8, 5, 5, 4, 4]
    print(remove_duplicates(random_list))

if __name__ == '__main__':
    run()