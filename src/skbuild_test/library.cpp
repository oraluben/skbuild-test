#include "Python.h"

static PyMethodDef methods[] = {
        {NULL, NULL, 0, NULL},
};


static struct PyModuleDef module = {
        PyModuleDef_HEAD_INIT,
        "skbuild_test",
        NULL,
        -1,
        methods
};

PyMODINIT_FUNC
PyInit_skbuild_test(void) {
    PyObject *m;

    m = PyModule_Create(&module);

    return m;
}