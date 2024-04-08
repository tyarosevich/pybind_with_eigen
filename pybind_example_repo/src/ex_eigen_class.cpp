#include <pybind11/pybind11.h>
#include <Eigen/Dense>
#include "pybind11/eigen.h"

namespace py = pybind11;

class VecWrapper {
public:
    Eigen::MatrixXd small_vec;
    VecWrapper() {
        small_vec = Eigen::MatrixXd::Zero(10, 1);
    }
    VecWrapper(Eigen::Ref<Eigen::MatrixXd> v){
    small_vec = v;
    }
    Eigen::MatrixXd &getMatrix() { return small_vec; }
    const Eigen::MatrixXd &viewMatrix() { return small_vec; }
};

void init_ex_eigen_class(py::module_ &m) {
    py::class_<VecWrapper>(m, "VecWrapper")
        .def(py::init<>())
        .def(py::init<Eigen::Ref<Eigen::MatrixXd>>())
        .def("copy_matrix", &VecWrapper::getMatrix) // Makes a copy!
        .def("get_matrix", &VecWrapper::getMatrix, py::return_value_policy::reference_internal)
        .def("view_matrix", &VecWrapper::viewMatrix, py::return_value_policy::reference_internal)
        ;
};
