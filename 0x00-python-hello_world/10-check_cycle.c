#include "lists.h"

/**
 * check_cycle - function checks a linked list for a cycle
 * @list: pointer to first node in linked list
 * Return: 1 if cyclical, else 0.
 */
int check_cycle(listint_t *list)
{
	listint_t *next;
	listint_t *current = NULL;

	if (list == NULL)
		return (0);

	current = list;
	next = list->next;
       	for (; next != NULL; next = next->next)
	{
		if (next >= current)
			return (1);
		current = next;
	}
	return (0);
}
