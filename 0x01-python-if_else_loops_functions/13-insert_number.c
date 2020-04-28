#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - check the code for Holberton School students.
 * @head: linked list
 * @number: nbr
 * Return: Always 0.
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *loop = *head, *new = malloc(sizeof(listint_t));

if (!new)
return (NULL);

new->n = number;
new->next = NULL;

if (!loop || loop->n > new->n)
{
new->next = loop;
*head = new;
return (*head);
}


while (loop)
{
if (!loop->next || new->n < loop->next->n)
{
new->next = loop->next;
loop->next = new;
return (loop);
}

loop = loop->next;
}

return (NULL);
}
