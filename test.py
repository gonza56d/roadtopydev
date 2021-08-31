
def fun(*args):
    for arg in args:
        print(arg)


dicc = {'color': 'purpura', 'numero': 4}
fun(*dicc.values())
