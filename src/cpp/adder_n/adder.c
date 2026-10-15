
#define PY_SSIZE_T_CLEAN
#include <Python.h>

/* Native C function: sum an array of integers */
static long long add_numbers(long long *numbers, Py_ssize_t n)
{
    long long result = 0;

    for (Py_ssize_t i = 0; i < n; ++i) {
        result += numbers[i];
    }

    return result;
}

/* Python-facing wrapper: accepts any number of arguments */
static PyObject *py_add_numbers(PyObject *self, PyObject *args)
{
    Py_ssize_t n = PyTuple_Size(args);

    long long *numbers = PyMem_Malloc(n * sizeof(long long));

    if (n > 0 && numbers == NULL) {
        return PyErr_NoMemory();
    }

    for (Py_ssize_t i = 0; i < n; ++i) {
        numbers[i] = PyLong_AsLongLong(PyTuple_GetItem(args, i));

        if (PyErr_Occurred()) {
            PyMem_Free(numbers);
            return NULL;
        }
    }

    long long result = add_numbers(numbers, n);

    PyMem_Free(numbers);

    return PyLong_FromLongLong(result);
}

/* Register the function */
static PyMethodDef AdderMethods[] = {
    {"add_numbers", py_add_numbers, METH_VARARGS,
     "Sum any number of integers."},
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

/* Initialise the module */
PyMODINIT_FUNC PyInit_adder(void)
{
    return PyModule_Create(&addermodule);
}