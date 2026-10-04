#include<pybind11/pybind11.h>
#include<pybind11/stl.h>
#include<cmath>
#include<stdexcept>
#include<string>
namespace py = pybind11;
constexpr double PI = 3.14159265358979323846;
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
double cosine(double x) {
    return std::cos(x);
}
double hyperbolic_cosine(double x) {
    return std::cosh(x);
}
double Deg(double x) {
    return x*180/PI;
}
double dist(const std::vector<double>& p1, const std::vector<double>& p2) {
    size_t l1 = p1.size();
    size_t l2 = p2.size();
    if (l1!=l2) {
        throw std::invalid_argument("both points must have the same number of dimensions");
    }
    double s = 0.0;
    for (size_t i = 0;i<p1.size();i++) {
        double d = p1[i]-p2[i];
        s+=d*d;
    }
    return std::sqrt(s);
}
double error_function(double x) {
    return std::erf(x);
}
double complementary_error_function(double x) {
    return std::erfc(x);
}
double exponential_function(double x) {
    return std::exp(x);
}
double base_2_exponential_function(double x) {
    return std::exp2(x);
}
double exponential_minus_one(double x) {
    return std::expm1(x);
}
float float_abs(float x) {
    return std::fabs(x);
}
PYBIND11_MODULE(MATH, m) {
    m.doc() = "math module for bracket-lang";
    m.attr("e") = 2.718281828459045;
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
    m.def("cos", &cosine, py::arg("x"), "cosine in trigonometric functions");
    m.def("cosh", &hyperbolic_cosine, py::arg("x"), "inverse cosine");
    m.def("degrees", &Deg, py::arg("x"), "radius to degrees");
    m.def("dist", &dist, py::arg("p1"), py::arg("p2"), "Euclidean distance");
    m.def("erf", &error_function, py::arg("x"), "error function");
    m.def("erfc", &complementary_error_function, py::arg("x"), "complementary error function");
    m.def("exp", &exponential_function, py::arg("x"), "exponential function");
    m.def("exp2", &base_2_exponential_function, py::arg("x"), "base-2 exponential function");
    m.def("expm1", &exponential_minus_one, py::arg("x"), "exp(x)-1");
    n.def("fabs", &float_abs, py::arg("x"), "abs for floating point numbers")
    py::register_exception<std::domain_error>(m, "DomainError");
}
