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
	printf("----------------\n");
	print_listint(cpy);
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
