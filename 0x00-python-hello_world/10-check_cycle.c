#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_style - check the code for Holberton School students.
 * @list: linked list
 * Return: Always .
 */
int check_cycle(listint_t *list)
{
listint_t *one = list, *two = list;
if (!list)
return (0);
while (two && two->next)
{
two = two->next->next;
one = one->next;
if (one == two)
return (1);
}
return (0);
}
