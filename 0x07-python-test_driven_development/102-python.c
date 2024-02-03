#include <stdio.h>
#include <Python.h>

void print_python_string(PyObject *p)
{
    PyASCIIObject *py_ascii_obj;

    printf("[.] string object info\n");
    if (!PyUnicode_Check(p))
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }
