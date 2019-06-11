import numpy as np

# generating  a random vector of integers
ranarr = np.random.randint(1,20,15)
print('input  vector is : ' + str(ranarr))

# finding maximum value in vector
max_val = ranarr.max()
print('Maximum value is : ' +str(max_val))

result = np.where(ranarr == np.amax(ranarr))

for index in result:
    ranarr[index] = 0

print(ranarr)

# finding the index(position) of max value
# max_index = ranarr.argmax()

# making max value to 0
# ranarr[max_index] = 0
# print('output vector is : ' + str(ranarr))


