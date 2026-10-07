#include<pybind11/pybind11.h>
#include<pybind11/stl.h>
#include<cmath>
#include<stdexcept>
#include<string>
#include<numeric>
#include<limits>
#include<algorithm>
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
double float_abs(double x) {
    return std::fabs(x);
}
long long factorial(size_t x) {
    long long fac = 1;
    for (size_t i = 2;i<=x;i++) {
        fac*=i;
    }
    return fac;
}
long long floor_function(double x) {
    return static_cast<long long>(std::floor(x));
}
double float_mod(double x, double y) {
    return std::fmod(x, y);
}
py::tuple frexp_py(double x) {
    int e;
    double m = std::frexp(x, &e);
    return py::make_tuple(m, e);
}
double ldexp_py(double m, int e) {
    return std::ldexp(m, e);
}
double kahan_sum(const std::vector<double>& v) {
    double s = 0.0, c = 0.0;
    for (double x : v) {
        double y = x-c;
        double t = s+y;
        c = (t-s)-y;
        s = t;
    }
    return s;
}
double gamma(double x) {
    return std::tgamma(x);
}
long long greatest_common_divisor(long long a, long long b) {
    return std::gcd(a, b);
}
double hypotenuse(const std::vector<double>& p) {
    double s = 0.0;
    for (size_t i = 0;i<p.size();i++) {
        s+=p[i]*p[i];
    }
    return std::sqrt(s);
}
bool isclose(double a, double b, double rel_tol = 1e-9, double abs_tol = 0.0) {
    if (a == b) {
        return true;
    }
    double diff = std::abs(a-b);
    return diff<=std::max(rel_tol*std::max(std::abs(a), std::abs(b)), abs_tol);
}
bool is_finite(double x) {
    return std::isfinite(x);
}
bool is_inf(double x) {
    return std::isinf(x);
}
bool is_nan(double x) {
    return std::isnan(x);
}
long long isqrt(long long n) {
    long long r = static_cast<long long>(std::sqrt(n));
    while (r * r > n) --r;
    while ((r + 1) * (r + 1) <= n) ++r;
    return r;
}
long long least_common_multiple(long long a, long long b) {
    return std::lcm(a, b);
}
double ln_gamma(double x) {
    return std::lgamma(x);
}
double ln(double x) {
    return std::log(x);
}
double log_10(double x) {
    return std::log10(x);
}
double log_2(double x) {
    return std::log2(x);
}
double logarithm_of_1_plus_x(double x) {
    return std::log1p(x);
}
py::tuple modf_py(double x) {
    double i;
    double f = std::modf(x, &i);
    return py::make_tuple(f, i);
}
PYBIND11_MODULE(MATH, m) {
    m.doc() = "math module for bracket-lang";
    m.attr("e") = 2.718281828459045;
    m.attr("inf") = std::numeric_limits<double>::infinity();
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
    m.def("fabs", &float_abs, py::arg("x"), "abs for floating point numbers");
    m.def("factorial", &factorial, py::arg("x"), "positive integer factorial");
    m.def("floor", &floor_function, py::arg("x"), "floor function");
    m.def("fmod", &float_mod, py::arg("x"), py::arg("y"), "mod for floating point numbers");
    m.def("frexp", &frexp_py, py::arg("x"), "x=m·2^e");
    m.def("ldexp", &ldexp_py, py::arg("m"), py::arg("e"), "m·2^e");
    m.def("fsum", &kahan_sum, py::arg("v"), "sum for floating point numbers");
    m.def("gamma", &gamma, py::arg("x"), "Gamma function");
    m.def("gcd", &greatest_common_divisor, py::arg("a"), py::arg("b"), "greatest common divisor");
    m.def("hypot", &hypotenuse, py::arg("p"), "hypotenuse");
    m.def("isclose", &isclose, py::arg("a"), py::arg("b"), py::arg("rel_tol") = 1e-9, py::arg("abs_tol") = 0.0, "check whether a number is close to another number");
    m.def("isfinite", &is_finite, py::arg("x"), "is finite");
    m.def("isinf", &is_inf, py::arg("x"), "is inf");
    m.def("isnan", &is_nan, py::arg("x"), "is nan");
    m.def("isqrt", &isqrt, py::arg("n"), "integer square root");
    m.def("lcm", &least_common_multiple, py::arg("a"), py::arg("b"), "least common multiple");
    m.def("lgamma", &ln_gamma, py::arg("x"), "ln|gamma(x)|");
    m.def("log", &ln, py::arg("x"), "ln(x)");
    m.def("log10", &log_10, py::arg("x"), "log base 10");
    m.def("log2", &log_2, py::arg("x"), "log base 2");
    m.def("log1p", &logarithm_of_1_plus_x, py::arg("x"), "ln(x+1)");
    m.def("modf", &modf_py, py::arg("x"), "split a decimal into integer part and decimal part");
    py::register_exception<std::domain_error>(m, "DomainError");
}
