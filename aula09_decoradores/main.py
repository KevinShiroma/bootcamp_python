from loguru import logger
# Você recebe logs de execução usando o loguru

import sentry_sdk

sentry_sdk.init(
    dsn="https://ad896477d4f01a3603f0a0dd6e077d61@o4507833130942464.ingest.us.sentry.io/4507833132253184",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for tracing.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

logger.add("aula09_decoradores/meu_app.log")

def soma(x, y):
    try:
        soma = x + y
        logger.info(soma)
        return soma
    except:
        logger.critical("Digite um numero válido")
        return x + y

print(soma(2, "3"))
