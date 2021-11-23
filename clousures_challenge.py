def make_division(x: int):

    # También se puede hacer como 
    # return lambda x: y/x
    def division(y):
        return y/x
    return division

def run():

    division_by_3 = make_division(3)
    print(division_by_3(18))

    division_by_5 = make_division(5)
    print(division_by_5(100))

    division_by_18 = make_division(18)
    print(division_by_18(54))


if __name__ == "__main__":
    run()