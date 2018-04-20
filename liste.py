bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#stampa un elemento specifico della lista
print(bicycles[0])

#si possono richiamare gli stessi metodi che venivano usati per le stringhe normali
print(bicycles[0].title())

#ritorna l'ultimo elemento della lista
print("ultimo elemento: ",bicycles[-1])

#come si compone un messaggio usando un valore specifico

message = "My first bicyle was a "+bicycles[0].title() + "."

print(message)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#modificare l'elemento di una lista
motorcycles[0] = 'ducati'
print(motorcycles[0])
