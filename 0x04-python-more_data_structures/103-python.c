#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Print basic information about Python bytes objects
 * @p: PyObject pointer (Python bytes object)
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("	[ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("	size: %ld\n", size);
	printf("	trying string: %s\n", str);

	printf("	first 10 bytes: ");
	for (i = 0; i < size && i < 10; ++i)
	{
		printf("%02x", (unsigned char)str[i]);
		if (i + 1 < size && i + 1 < 10)
			printf(" ");
	}
	printf("\n");
}

/**
 * print_python_list - Print basic information about Python lists
 * @p: PyObject pointer (Python list object)
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, allocated, i;
	PyObject *item;

	printf("[*] Python list info\n");

	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < size; ++i)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);

		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}
