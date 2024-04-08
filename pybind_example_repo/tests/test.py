import python_example as m
import numpy as np

assert m.__version__ == '0.0.6'

# Test functions from other source files.
assert m.add(1, 2) == 3
assert m.sub(1, 2) == -1
print(m.add(1, 2))

# Test class from other source file.
p = m.Pet("Molly")
print(p)
print(p.getName())
p.setName("Charly")
print(p.getName())

# Test eigen matrix from other source file.
print("Testing default initialization.")
a = m.VecWrapper()
mat_from_eigen = a.get_matrix()  # flags.writeable = True,  flags.owndata = False
v = a.view_matrix()  # flags.writeable = False, flags.owndata = False
c = a.copy_matrix()

print(mat_from_eigen)
print(type(mat_from_eigen))

print("Testing initialization with numpy array.")
b = np.random.rand(10,)
print("Numpy array:")
print(b)
print("Eigen matrix")
a = m.VecWrapper(b)
mat_from_eigen = a.get_matrix()  # flags.writeable = True,  flags.owndata = False
v = a.view_matrix()  # flags.writeable = False, flags.owndata = False
c = a.copy_matrix()
print(mat_from_eigen)
print(type(mat_from_eigen))
print(mat_from_eigen.flags.owndata)