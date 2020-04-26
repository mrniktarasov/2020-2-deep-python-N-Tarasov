import cProfile
from loguru import logger


def profile(func):
    def wrapper(*args, **kwargs):
        profiler = cProfile.Profile()
        result = profiler.runcall(func, *args, **kwargs)
        profiler.print_stats()
        return result
    return wrapper


@logger.catch
@profile
def matrix(array):
    logger.add('matrix_logger.log', format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}")
    logger.info('Function started')
    answer = []
    if type(array) is not list:
        logger.error('Input value must be list')
        raise ValueError('Input value must be list')
    l_n = len(array)
    for i in range(0, l_n):
        mul = 1
        for j in range(0, l_n):
            logger.info('Cycle for {} started'.format(array[i]))
            if i != j:
                logger.info('Multiple {mul} with {arr} to gain {result}'.format(
                    mul=mul,
                    arr=array[j],
                    result=mul*array[j])
                )
                mul *= array[j]
            logger.info('Cycle for {} ended'.format(array[i]))
        answer.append(mul)
    logger.info('End of Function')
    return answer


if __name__ == '__main__':
    arr = [3]*40
    matrix(arr)
