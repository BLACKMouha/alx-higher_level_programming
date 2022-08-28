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
	current = *head;
	if (!current || current->n >= number)
	{	new_node->next = current;
		*head = new_node;
		return (new_node);
	}

	while (current && current->next && current->next->n < number)
		current = current->next;

	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
