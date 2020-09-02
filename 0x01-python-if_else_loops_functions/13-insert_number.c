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
	listint_t *new = NULL;

	if (*head == NULL)
	{
		new = add_nodeint_end(head, number);
		return (new);
	}

	current = *head;

	if (number < current->n)
	{
		add_nodeint(head, number);
		return (*head);
	}
	for (; current->next != NULL; current = current->next)
	{
		next = current->next;
		if ((number >= current->n) & (number < next->n))
		{
			new =  malloc(sizeof(listint_t));
			if (new == NULL)
				return (NULL);
			new->n = number;
			new->next = next;
			current->next = new;
			return (new);
		}
	}
	if (number > current->n)
		add_nodeint_end(head, number);
	return (new);
}

/**
 * add_nodeint - adds a new node at the beginning of a listint_t list
 * @head: pointer to a pointer of the start of the list
 * @n: integer to be included in node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = *head;
	*head = new;

	return (new);
}
