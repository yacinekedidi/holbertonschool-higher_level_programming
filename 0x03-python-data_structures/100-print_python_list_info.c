#include <stdio.h>
#include <stdlib.h>
#include <Python.h>


/**
 * print_python_list_info - prints info about python lists
 * @p: pyobject struct
 */
void print_python_list_info(PyObject *p)
{
	int i;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", 0);
		for (i = 0 ; i < Py_SIZE(p) ; i++)
			printf("Element %lu: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);

}
