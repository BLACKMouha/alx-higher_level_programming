#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * Prototype: int check_cycle(listint_t *list);
 * @list: points to the first node
 * Return: 1 if there is a cycle, otherwise 0
 *
 */

int check_cycle(listint_t *list)
{
	listint_t *turtle, *cheetah;

	turtle = list;
	cheetah = list;
	while(turtle && cheetah && cheetah->next)
	{
		turtle = turtle->next;
		cheetah = cheetah->next->next;
		if (turtle == cheetah)
			return (1);
	}
	return (0);
}
