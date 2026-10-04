#include<pybind11/pybind11.h>
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
long long ceiling_function(double x) {
    return static_cast<long long>(std::ceil(x));
}
long long comb(int n, int k) {
    if (k<0 || k>n) {
        return 0;
    }
    if (k>n-k) {
        k = n-k;
    }
    long long r = 1;
    for (int i = 0; i < k; ++i) {
        r = r*(n-i)/(i+1);
    }
    return r;
}
double copy_sign(double x, double y) {
    return std::copysign(x, y);
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
    m.def("ceil", &ceiling_function, py::arg("x"), "ceiling function");
    m.def("comb", &comb, py::arg("n"), py::arg("k"), "combination number");
    m.def("copysign", &copy_sign, py::arg("x"), py::arg("y"), "copy sign");
    py::register_exception<std::domain_error>(m, "DomainError");
}
