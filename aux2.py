cores = set(['azul', 'verde', 'amarelo'])

print(cores)

cores1 = {'azul', 'verde', 'amarelo'}
cores2 = {'vermelho', 'roxo', 'amarelo', 'verde', 'amarelo', 'salmao'}

inter = cores1.intersecton(cores2)
cores1.intersection_update(cores2)

print(cores1)
print(cores2)
print (inter)