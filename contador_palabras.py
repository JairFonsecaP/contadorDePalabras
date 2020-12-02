def contador(texto: str) -> dict:
    import pandas
    import re
    import string
    re.sub('[%s]' % re.escape(string.punctuation), '', texto)
    palabras = pandas.DataFrame(pandas.Series(texto.split(' ')).value_counts()).to_dict().get(0)
    return palabras

print(contador(str(input('ingrese el texto: '))))
