//#####################the wrapping

#define PY_SSIZE_T_CLEAN
#include <Python.h>

// Declare the function implemented in hello.cpp
void hello_cpp();

// Python-facing wrapper
static PyObject* py_hello_cpp(PyObject* self, PyObject* args)
{
    hello_cpp();

    Py_RETURN_NONE;
}

// Register the function
static PyMethodDef HelloMethods[] = {
    {"hello_cpp", py_hello_cpp, METH_NOARGS,
     "Call the C++ hello function."},
    {NULL, NULL, 0, NULL}
};

// Define the module
static PyModuleDef hellomodule = {
    PyModuleDef_HEAD_INIT,
    "hello",
    "A C++ extension module.",
    -1,
    HelloMethods
};

// Initialise the module
PyMODINIT_FUNC PyInit_hello(void)
{
    return PyModule_Create(&hellomodule);
}