from django.apps import AppConfig

class UsersConfig(AppConfig):
    name = 'users'

    def ready(self): #Ky funksion ekzekutohet kur django startohet
        import users.signals
