
#define PY_SSIZE_T_CLEAN
#include <Python.h>

/* The actual C calculation */
static long long add_numbers(long long a, long long b)
{
    return a + b;
}

/* Python-facing wrapper */
static PyObject *py_add_numbers(PyObject *self, PyObject *args)
{
    long long a;
    long long b;

    /* Extract two integers supplied by Python */
    if (!PyArg_ParseTuple(args, "LL", &a, &b)) {
        return NULL;
    }

    /* Call the native C function */
    long long result = add_numbers(a, b);

    /* Convert the result into a Python integer */
    return PyLong_FromLongLong(result);
}

/* Register the function with Python */
static PyMethodDef AdderMethods[] = {
    {
        "add_numbers",
        py_add_numbers,
        METH_VARARGS,
        "Add two integers using C."
    },
    {NULL, NULL, 0, NULL}
};

/* Define the module */
static struct PyModuleDef addermodule = {
    PyModuleDef_HEAD_INIT,
    "adder",
    "A simple C extension.",
    -1,
    AdderMethods
};

/* Initialise the module when Python imports it */
PyMODINIT_FUNC PyInit_adder(void)
{
    return PyModule_Create(&addermodule);
}