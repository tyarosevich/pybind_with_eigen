#include <pybind11/pybind11.h>
#include <Eigen/Dense>
#include "pybind11/eigen.h"

namespace py = pybind11;
// This is a way to define a row-major matrix in order to pass numpy arrays without making them col major first,
// and maintain contiguous memory in Eigen. This does NOT enable numpy style slicing of the object on the python side,
// which requires simply using Eigen::DRef. This, however, results in non-optimized, non-contiguous memory.
using RowMatrixXd = Eigen::Matrix<double, Eigen::Dynamic, Eigen::Dynamic, Eigen::RowMajor>;

class VecWrapper {
public:
    RowMatrixXd small_vec;
    VecWrapper() {
        small_vec = RowMatrixXd::Zero(10, 1);
    }
    VecWrapper(Eigen::Ref<RowMatrixXd> v){
    small_vec = v;
    }
    RowMatrixXd &getMatrix() { return small_vec; }
    const RowMatrixXd &viewMatrix() { return small_vec; }
};

void init_ex_eigen_class(py::module_ &m) {
    py::class_<VecWrapper>(m, "VecWrapper")
        .def(py::init<>())
        // Note that normally we'd pass a ref to a constructor with &, but this is not necessary - the Eigen::Ref
        // class handles that. Also note, py::arg().noconvert() forces a failure if the referenced numpy array is
        // copied for any reason (e.g. a row-major type is passed to a column-major Eigen matrix).
        .def(py::init<Eigen::Ref<RowMatrixXd>>(), py::arg().noconvert())
        .def("copy_matrix", &VecWrapper::getMatrix) // Makes a copy!
        .def("get_matrix", &VecWrapper::getMatrix, py::return_value_policy::reference_internal)
        .def("view_matrix", &VecWrapper::viewMatrix, py::return_value_policy::reference_internal);
};
