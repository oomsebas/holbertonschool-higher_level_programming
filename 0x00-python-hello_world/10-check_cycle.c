#include "lists.h"


int check_cycle(listint_t *list)
{
	listint_t *head_value;
	listint_t *current = NULL;

	head_value = list;
	current = list;
	for (; current != NULL; current = current->next)
	{
		if (current->next == head_value)
			return (1);
	}
	return (0);
}
