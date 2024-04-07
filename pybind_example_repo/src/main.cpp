#include <pybind11/pybind11.h>
#include "pybind11/eigen.h"
namespace py = pybind11;

#define STRINGIFY(x) #x
#define MACRO_STRINGIFY(x) STRINGIFY(x)

void init_ex1(py::module_ &);
void init_ex2(py::module_ &);
void init_ex1_class(py::module_ &);
void init_ex_eigen_class(py::module_ &);

/* ... */

PYBIND11_MODULE(python_example, m) {
    m.doc() = R"pbdoc(
        Pybind11 example plugin
        -----------------------

        .. currentmodule:: python_example

        .. autosummary::
           :toctree: _generate

           add
           subtract
    )pbdoc";

    init_ex1(m);
    init_ex2(m);
    init_ex1_class(m);
    init_ex_eigen_class(m);

//    m.def("add", &add, R"pbdoc(
//        Add two numbers
//
//        Some other explanation about the add function.
//    )pbdoc");
//
//    m.def("subtract", [](int i, int j) { return i - j; }, R"pbdoc(
//        Subtract two numbers
//
//        Some other explanation about the subtract function.
//    )pbdoc");
//
//    m.def("multiply", [](float i, float j) { return i * j; }, R"pbdoc(
//        multiply two numbers
//
//        Some other explanation about the subtract function.
//    )pbdoc");

#ifdef VERSION_INFO
    m.attr("__version__") = MACRO_STRINGIFY(VERSION_INFO);
#else
    m.attr("__version__") = "dev";
#endif
}
