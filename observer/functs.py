from subscriptions import Subscriptions


def registrate_user(user: str):
    print('*Performs registration*')
    Subscriptions.trigger('registrate_user', user)


def send_welcome_email(user):
    print(f'Thank you {user} for registering your account!')


def send_welcome_slack(user):
    print(f'Everyone give a warm welcome to {user}!')


def setup():
    Subscriptions.subscribe('registrate_user', send_welcome_email)
    Subscriptions.subscribe('registrate_user', send_welcome_slack)


setup()
registrate_user('gonza')
registrate_user('seba')
