


class Subscriptions:

    options = {}
    
    def subscribe(option: str, subscriber):
        if option not in Subscriptions.options:
            Subscriptions.options[option] = []
        Subscriptions.options[option].append(subscriber)

    def trigger(option, *args, **kwargs):
        if option not in Subscriptions.options:
            return
        for subscriber in Subscriptions.options[option]:
            subscriber(*args, **kwargs)
