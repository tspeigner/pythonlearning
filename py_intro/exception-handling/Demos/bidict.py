def bidict(d):
    d2 = d.copy()
    for k,v in d.items():
        d2[v] = k
    return d2

translator = bidict({'hola':'hi', 'adios':'bye'})
print(translator['hola'])
print(translator['hi'])

translator2 = bidict({'hola':'hi', 'adios':'bye', 'chao':'bye'})
print(translator2)