#include <pybind11/pybind11.h>
namespace py = pybind11;

int sub(int a, int b) {
    return a - b;
}

void init_ex2(py::module_ &m) {
    m.def("sub", &sub, "Subtract two numbers",
          py::arg("a") = 0, py::arg("b") = 0); // Ex. of default arguments.
}