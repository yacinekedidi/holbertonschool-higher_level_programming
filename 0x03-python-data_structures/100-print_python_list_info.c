#include <stdio.h>
#include <stdlib.h>
#include <Python.h>



void print_python_list_info(PyObject *p)
{
	unsigned int i, allocation = 0;
	Py_ssize_t size = Py_SIZE(p);
	printf("[*] Size of the Python List = %lu\n", size);
	printf("[*] Allocated = %lu\n", allocation);

		for (i = 0 ; i < size ; i++)
		{
			printf("Element %lu : %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
		}

}
