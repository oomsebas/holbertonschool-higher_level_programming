#include "lists.h"

/**
 *is_palindrome - detect if a linked list is a palindrome
 *@head: head to the linked list
 *Return: 1 if is palindrome, 0 if isnot palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *rev;
	listint_t *cpy = NULL;

	if (*head == NULL)
		return (0);

	rev = *head;
	for (; rev != NULL; rev = rev->next)
	{
		add_nodeint(&cpy, rev->n);
	}
	rev = *head;
	while (rev != NULL)
	{
		if (rev->n == cpy->n)
		{
			rev = rev->next;
			cpy = cpy->next;
		}
		else
			return (0);
	}
	return (1);
}

/**
 *add_nodeint - function that creates a node at the beginning
 *@head: pointer to the first node;
 *@n: int to add to the new node;
 *Return: pointer to the first element of the list;
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

	return (*head);

}

