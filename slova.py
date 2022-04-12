import random   # # import pro výběr náhodného prvku
def vyber_slova():
    seznam_slov = ["čokoláda", "tramvaj", "parník", "popelník", "lokomotiva", "trávník", "pekařství", "zahradnictví", "papírnictví" ]
    slovo = random.choice(seznam_slov)
    return slovo 