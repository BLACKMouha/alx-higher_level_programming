#include "lists.h"

/**
 * listint_len - computes the number of node of a listint_t list
 * Prototype: size_t listint_len(const listint_t *h);
 * @h: points to the first node
 * Return: the number of nodes of a listint_t list
 */
size_t listint_len(const listint_t *h)
{
	size_t non;

	non = 0;
	if (h)
	{
		while (h != NULL)
		{
			h = h->next;
			non++;
		}
		return (non);
	}
	else
		return (0);
}

/**
 * add_nodeint - adds a new node at the beginning of a listint_t list
 * Prototype: listint_t *add_nodeint(listint_t **head, const int n);
 * @head: points to the first node
 * @n: integer to be inserted in the n field of a listint_t node
 * Return: the address of the newly node created or NULL on failure
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
	{
		free(new_node);
		return (NULL);
	}

	new_node->n = n;
	new_node->next = *head;
	*head = new_node;

	return (new_node);
}

/**
 * is_palindrome - checks is a singly linked list is a
 * palindrome
 *
 * Prototype: int is_palindrome(listint_t **head);
 * @head: points to the first node
 *
 * Return: 1 if it is a palindrome otherwise 0.
 */

int is_palindrome(listint_t **head)
{
	listint_t *reversed, *temp, *temp_rev;
	size_t is_pal = 0;

	temp = *head;
	reversed = NULL;
	while (temp)
	{
		add_nodeint(&reversed, temp->n);
		temp = temp->next;
	}

	temp = *head;
	temp_rev = reversed;
	while (temp_rev && temp)
	{
		if (temp_rev->n == temp->n)
			is_pal++;
		else
			break;
		temp_rev = temp_rev->next;
		temp = temp->next;
	}

	free_listint(reversed);

	if (is_pal == listint_len(*head))
		return (1);
	else
		return (0);
}

























