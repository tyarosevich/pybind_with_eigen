#include <pybind11/pybind11.h>
namespace py = pybind11;

void init_ex1(py::module_ &m) {
    m.def("add", [](int a, int b) { return a + b; });
}