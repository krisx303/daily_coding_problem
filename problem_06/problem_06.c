#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdio.h>
#define MEMORY_ALLOCATION_ERROR -1

typedef struct ListElement
{
    void *data;
    int both;
} ListElement;

typedef struct List
{
    ListElement *head;
    ListElement *tail;
    int size;
} List;

//* Funkcje alokujące pamięć dla nowych obiektów
List *initList()
{
    List *list = (List *)malloc(sizeof(List));
    if (list == NULL)
    {
        exit(MEMORY_ALLOCATION_ERROR);
    }
    list->size = 0;
    list->head = NULL;
    list->tail = NULL;
    return list;
}

ListElement *initListElement()
{
    ListElement *node = (ListElement *)malloc(sizeof(ListElement));
    if (node == NULL)
    {
        exit(MEMORY_ALLOCATION_ERROR);
    }
    node->both = 0;
    return node;
}

int *create_data_int(int v)
{
    int *addr = malloc(sizeof(int));
    *addr = v;
    return addr;
}

ListElement *createListElement(int data)
{
    ListElement *element = initListElement();
    element->data = create_data_int(data);
    return element;
}

//* Funkcja dodająca nowy element na koniec listy z podanymi danymi
void pushBack(List *list, int data)
{
    ListElement *node = createListElement(data);
    ListElement *tail = list->tail;
    int pointer = (int)node;
    if (tail)
    {
        tail->both = tail->both ^ pointer;
    }
    list->tail = node;
    node->both = (int)tail;
    if (!list->head)
        list->head = node;
    list->size++;
}

void printInt(ListElement *element)
{
    int *pointer = (int *)element->data;
    printf("value: %d\n", *pointer);
}

void printList(List *list)
{
    printf("list elements:\n");
    ListElement *element = list->head;
    int pointer = 0;
    for (int i = 0; i < list->size; i++)
    {
        printInt(element);
        ListElement *el = (ListElement *)(element->both ^ pointer);
        pointer = (int)element;
        element = el;
    }
}

ListElement *getElement(List *list, int index)
{
    ListElement *element = list->head;
    int pointer = 0;
    for (int i = 0; i < index; i++)
    {
        ListElement *el = (ListElement *)(element->both ^ pointer);
        pointer = (int)element;
        element = el;
    }
    return element;
}

int main()
{
    List *list = initList();
    pushBack(list, 123);
    pushBack(list, 312);
    pushBack(list, 5050);
    printList(list);
    printInt(getElement(list, 2));
    return 0;
}