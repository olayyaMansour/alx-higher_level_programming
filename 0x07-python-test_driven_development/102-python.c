#include "Python.h"

/**
 * print_python_string - Prints data about Python strings.
 * @python_string: string object.
 */
void print_python_string(PyObject *python_string)
{
    long int string_length;

    fflush(stdout);

    printf("[.] string object info\n");
    if (strcmp(python_string->ob_type->tp_name, "str") != 0)
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    string_length = ((PyASCIIObject *)(python_string))->length;

    if (PyUnicode_IS_COMPACT_ASCII(python_string))
        printf("  type: compact ascii\n");
    else
        printf("  type: compact unicode object\n");
    printf("  length: %ld\n", string_length);
    printf("  value: %ls\n", PyUnicode_AsWideCharString(python_string, &string_length));
}
