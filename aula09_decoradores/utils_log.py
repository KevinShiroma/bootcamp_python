from loguru import logger


def log_decorator(func):
    @logger.catch
    def wrapper(*args, **kwargs):
        logger.info(f"Entrando na função '{func.__name__}' com argumentos {args} e {kwargs}")
        resultado = func(*args, **kwargs)
        logger.info(f"Saindo da função '{func.__name__}' com resultado: {resultado}")
        return resultado
    return wrapper