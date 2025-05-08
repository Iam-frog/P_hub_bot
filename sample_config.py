HEROKU = True  #

# 
if HEROKU:
    from os import environ

    Bot_token = environ["Bot_token"]
    ARQ_API_KEY = environ["ARQ_API_KEY"]

# 
if not HEROKU:
    Bot_token = "7266490468:AAEsPDnsQ3bWdWNCX4rFMqJXNacnf6zKqlY"
    ARQ_API_KEY = "BOCULW-SEMUAC-MGWSPF-RYCMCB-ARQ"
