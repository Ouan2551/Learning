#include <stdio.h>
#include <stdlib.h> // working with dynamically memory
#include <stdbool.h>

typedef struct
{
    int *collection;
    int capacity;
    int size;
} Stack;

Stack *create_stack(int capacity);
// create function to destroy stack
void destroy_stack(Stack *stack);
// checking stack
bool is_full(Stack *stack);
bool is_empty(Stack *stack);
// pop and push stack
bool pop(Stack *stack, int *item);
bool push(Stack *stack, int item);
// peek is return value that's the top of stack
bool peek(Stack *stack, int *item);

int main()
{
    // LFIO => last in first out
    Stack *stack = create_stack(0);

    if (stack == NULL)
    {
        printf("Error creating stack.\n"); return 1; // return 1 to terminal that it have something wrong
    }
    if (is_empty(stack) == true)
    {
        printf("Stack is empty.\n");
    }
    // if (is_empty(stack)) printf("Stack is empty\n");
    destroy_stack(stack);
}

// before creating stack it require capacity need > 0
Stack *create_stack(int capacity)
{
    if (capacity <= 0)
    {
        return NULL;
    }

    Stack *stack = malloc(sizeof(Stack));
    // mallof => allocate space to store stack (return to *stack)
    if (stack == NULL)
    {
        return NULL;
    }

    stack->collection = malloc(sizeof(int) * capacity);
    // malloc => allocate space for int data types
    // then malloc return memory address store into collection of stack
    if (stack->collection == NULL)
    {
        free(stack); return NULL;
    }

    stack->capacity = capacity;
    stack->size = 0;

    return stack;
}

void destroy_stack(Stack *stack)
{
    free(stack->collection); free(stack);
}

bool is_full(Stack *stack)
{
    return stack->capacity == stack->size; //checking and return true or false
}

bool is_empty(Stack *stack)
{
    return stack->size == 0;
}