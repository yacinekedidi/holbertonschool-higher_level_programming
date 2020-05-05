#include "lists.h"
/**
 * reverse - check the code for Holberton School students.
 * @head: linked list
 * Return: Always .
 */

listint_t *reverse(listint_t *head)
{
listint_t *step, *tmp = head;

while (tmp->next)
{
step = tmp->next;
tmp->next = step->next;
step->next = head;
head = step;
}
return (head);
}

/**
 * is_palindrome - check the code for Holberton School students.
 * @head: linked list
 * Return: Always .
 */

int is_palindrome(listint_t **head)
{
listint_t *tmp = *head;
int *tab;
int i = 0;

if (!*head || !(*head)->next)
return (1);

while (tmp)
{
tmp = tmp->next;
i++;
}

 tab = malloc(sizeof(int) * i);

tmp = *head;
i = 0;
while (tmp)
{
tab[i] = tmp->n;
tmp = tmp->next;
i++;
}

*head = reverse(*head);

i = 0;
while (*head)
{
if (tab[i] == (*head)->n)
{
i++, *head = (*head)->next;
}
else
{
free(tab);
return (0);
}
} *head = reverse(*head), free(tab);
return (1);
}
