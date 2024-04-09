import python_example as m
import numpy as np

def test_version():
    assert m.__version__ == '0.0.6'

# Test functions from other source files.
def test_multiple_source_files():
    assert m.add(1, 2) == 3
    assert m.sub(1, 2) == -1
    assert(m.sub() == 0) # Testing default values.
    print(m.add(i=1, j=2))

# Test class from other source file.
def test_class_from_other_source_file():
    p = m.Pet("Molly")
    assert p.getName() == "Molly"
    p.setName("Charly")
    assert p.getName() == "Charly"

# Test eigen matrix from other source file.
def test_eigen_default_constructor():
    a = m.VecWrapper()
    mat_from_eigen = a.get_matrix()  # flags.writeable = True,  flags.owndata = False
    v = a.view_matrix()  # flags.writeable = False, flags.owndata = False
    c = a.copy_matrix()
    assert c.flags.owndata == True
    assert c.flags.writeable == True
    assert v.flags.owndata == False
    assert v.flags.writeable == False
    assert mat_from_eigen.flags.owndata == False
    assert mat_from_eigen.flags.writeable == True
    assert type(mat_from_eigen) == np.ndarray

def test_eigen_constructor_with_numpy_vector():
    b = np.random.rand(10,)
    a = m.VecWrapper(b)
    mat_from_eigen = a.get_matrix()  # flags.writeable = True,  flags.owndata = False
    v = a.view_matrix()  # flags.writeable = False, flags.owndata = False
    c = a.copy_matrix()
    assert c.flags.owndata == True
    assert c.flags.writeable == True
    assert v.flags.owndata == False
    assert v.flags.writeable == False
    assert mat_from_eigen.flags.owndata == False
    assert mat_from_eigen.flags.writeable == True
    assert type(mat_from_eigen) == np.ndarray

def test_eigen_constructor_with_numpy_matrix():
    b = np.random.rand(10, 10)
    a = m.VecWrapper(b)
    mat_from_eigen = a.get_matrix()  # flags.writeable = True,  flags.owndata = False
    v = a.view_matrix()  # flags.writeable = False, flags.owndata = False
    c = a.copy_matrix()
    assert c.flags.owndata == True
    assert c.flags.writeable == True
    assert v.flags.owndata == False
    assert v.flags.writeable == False
    assert mat_from_eigen.flags.owndata == False
    assert mat_from_eigen.flags.writeable == True
    assert type(mat_from_eigen) == np.ndarray
    assert mat_from_eigen.flags['C_CONTIGUOUS'] == True

