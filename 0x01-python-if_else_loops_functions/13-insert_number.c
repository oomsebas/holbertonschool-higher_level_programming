#include "lists.h"

/**
 *insert_node - insert a node on ordered linked list
 *@head: pointer to the head of the list
 *@number: number to order in the list
 *Return: pointer to the head of the created list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *next;
	listint_t *new;

	current = *head;
/*	if (number < current->n)
	{
		add_nodeint(head, number);
		return (*head);
		}*/
	for (; current->next != NULL; current = current->next)
	{
		next = current->next;
		if ((number > current->n) & (number < next->n))
		{
			new =  malloc(sizeof(listint_t));
			if (new == NULL)
				return (NULL);
			new->n = number;
			new->next = next;
			current->next = new;
			return (*head);
		}
	}
	add_nodeint_end(head, number);
	return (*head);
}
