#include "lists.h"

/**
 * check_cycle - function checks a linked list for a cycle
 * @list: pointer to first node in linked list
 * Return: 1 if cyclical, else 0.
 */
int check_cycle(listint_t *list)
{
	listint_t *head_value;
	listint_t *current = NULL;

	if (list == NULL)
		return (0);

	head_value = list;
	current = list->next;
	for (; current != NULL; current = current->next)
	{
		if (current == head_value)
			return (1);
	}
	return (0);
}
