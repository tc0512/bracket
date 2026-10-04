#include<pybind11/pybind11.h> //WARNING: PyBind11 only support C++14+
#include<pybind11/stl.h>
#include<cmath>
#include<stdexcept>
#include<string>
namespace py = pybind11;
double arccos(double x) {
    if (-1<=x && x<=1) {
        return std::acos(x);
    }
    throw std::domain_error("input must be between -1 and 1,got "+std::to_string(x));
}
double arcosh(double x) {
    if (x<1) {
        throw std::domain_error("input must be at least 1,got "+std::to_string(x));
    }
    return std::acosh(x);
}
double arcsin(double x) {
    if (-1<=x && x<=1) {
        return std::asin(x);
    }
    throw std::domain_error("input must be between -1 and 1,got "+std::to_string(x));
}
double arsinh(double x) {
    return std::asinh(x);
}
double arctan(double x) {
    return std::atan(x);
}
double arctan2(double y, double x) {
    if (y==0 && x==0) {
        throw std::domain_error("input cannot be (0,0)");
    }
    return std::atan2(y, x);
}
double artanh(double x) {
    if (-1 < x && x < 1) {
        return std::atanh(x);
    }
    throw std::domain_error("artanh: input must be between -1 and 1, got " + std::to_string(x));
}
double cube_root(double x) {
    return std::cbrt(x);
}
double ceiling_function(double x) {
    return std::ceil(x);
}
PYBIND11_MODULE(MATH, m) {
    m.doc() = "math module for bracket-lang";
    m.def("acos", &arccos, py::arg("x"), "inverse cosine");
    m.def("acosh", &arcosh, py::arg("x"), "inverse hyperbolic cosine");
    m.def("asin", &arcsin, py::arg("x"), "inverse sine");
    m.def("asinh", &arsinh, py::arg("x"), "inverse hyperbolic sine");
    m.def("atan",  &arctan, py::arg("x"), "inverse tangent");
    m.def("atan2", &arctan2, py::arg("y"), py::arg("x"), "two-argument inverse tangent");
    m.def("atanh", &artanh, py::arg("x"), "inverse hyperbolic tangent");
    m.def("cbrt",  &cube_root, py::arg("x"), "cube root");
    m.def("ceil", &ceiling_function, py::arg("x"), "ceiling function")
    py::register_exception<std::domain_error>(m, "DomainError");
}
