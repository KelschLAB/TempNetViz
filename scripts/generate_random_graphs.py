import numpy as np

path = "..\\data\\random_graph\\"
size = 50
test = np.random.rand(size, size)
test = test - test.diagonal()

for i in range(1, 11):
    this_arr = np.random.rand(size, size)
    this_arr[:, :size//2] = 0
    test += this_arr*i
    test = test - test.diagonal()
    np.savetxt(path+f"rand_graph{i}.csv", test, delimiter=",")