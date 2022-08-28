#include "lists.h"

/**
 * insert_node - inserts a new node into a sorted
 * listin_t singly linked list
 *
 * Prototype:
 * listint_t *insert_node(listin_t **head, int number);
 *
 * @head: points to the first node
 * @number: integer to insert
 *
 * Return: the address of the new node or NULL if it
 * failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		dprintf(2, "Malloc failed\n");
		return (NULL);
	}

	new_node->n = number;

	if (head == NULL) /** Empty list */
		*head = new_node;

	if ((*head)->n >= new_node->n)
	{
		new_node->next = *head;
		*head = new_node;
	}

	current = *head;
	while (current->next)
	{
		if (((new_node->n > current->n) &&
		    (new_node->n <= current->next->n)))
		{
			new_node->next = current->next;
			current->next = new_node;
			current = new_node;
		}
		current = current->next;
	}

	current = *head;
	while (current->next)
		current = current->next;
	if (current->n <= new_node->n)
		new_node = add_nodeint_end(head, number);
	return (new_node);
}
