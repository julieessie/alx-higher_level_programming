#include "lists.h"
/**
 * *add_dnodeint - function adds new node to beginning of list
 *
 *@head: pointer to pointer of head of linked list
 *@n: const int pointer
 *
 * Return: address of new element, or NULL if failed
 */

dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
dlistint_t *node = NULL;

node = malloc(sizeof(dlistint_t));
if (node == NULL)
return (NULL);

node->n = n;
node->next = (*head);
node->prev = NULL;

if ((*head) != NULL)
(*head)->prev = node;

(*head) = node;

return (node);
}
