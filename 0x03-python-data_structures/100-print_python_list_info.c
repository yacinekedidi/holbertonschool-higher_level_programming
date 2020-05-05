#include <stdio.h>
#include <stdlib.h>
#include <Python.h>



void print_python_list_info(PyObject *p)
{
	unsigned int size, i, allocation;
	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %lu\n", size);
	printf("[*] Allocated = %lu\n", allocation);

		for (i = 0 ; i < size ; i++)
		{
			printf("Element %lu : %s", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
		}

}
