from decouple import config


# API_KEY = config('API_KEY')
mail_address = config("MAIL_ADDRESS")
mail_password = config("MAIL_PASSWORD")
app_password = config("APP_PASSWORD")
to_address = config("TO_ADDRESS")
api_username = config("API_USERNAME")
api_password = config("API_PASSWORD")


if __name__ == '__main__':
    print(mail_address, mail_password)
