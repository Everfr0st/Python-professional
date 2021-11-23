### Este código cuenta el tiempo que pasa entre el inicio de una ejecución y el final de la misma

from datetime import datetime
from typing import final

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        finaltime = datetime.now()
        time_elapsed = finaltime - initial_time
        print(f'Pasaron {time_elapsed.total_seconds()} segundos')
    return wrapper

@execution_time
def random_func():
    for _ in range(1, 100000000):
        pass


# random_func()