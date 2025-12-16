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
    Stack *stack = create_stack(5);

    if (stack == NULL)
    {
        printf("Error creating stack.\n"); return 1; // return 1 to terminal that it have something wrong
    }
    // ----------------------------------------------------------------------------------------------------
    if (is_empty(stack) == true)
    {
        printf("Stack is empty.\n");
    }
    // if (is_empty(stack)) printf("Stack is empty\n");

    // ----------------------------------------------------------------------------------------------------

    push(stack, 1);
    printf("Stack size: %d\n", stack->size);
    push(stack, 2); push(stack, 3); push(stack, 4); push(stack, 5);
    printf("Stack size: %d\n", stack->size);

    if (is_full(stack) == true)
    {
        printf("Stack is full.\n");
    }

    bool try_push = push(stack, 6);
    if (try_push == false) printf("Push failed.\n");

    // ----------------------------------------------------------------------------------------------------

    int peek_value = 0;
    peek(stack, &peek_value);

    printf("Peek value : %d\n", peek_value);

    // ----------------------------------------------------------------------------------------------------

    int pop_value = 0;
    for (int i = 0; i < 5; i++)
    {
        pop(stack, &pop_value);
        printf("Pop_value : %d\n", pop_value);
    }

    // ----------------------------------------------------------------------------------------------------
    bool try_pop = pop(stack, &pop_value);
    if (try_pop == false) printf("Pop failed. \n");

    // ----------------------------------------------------------------------------------------------------
    bool try_peek = peek(stack, &peek_value);
    if (try_peek == false) printf("Peek failed. \n");
    // ----------------------------------------------------------------------------------------------------
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

bool push(Stack *stack, int item)
{
    if (is_full(stack) == true)
    {
        return false;
    }
    stack->collection[stack->size] = item;
    stack->size++;
    return true;
}

bool peek(Stack *stack, int *item)
{
    if (is_empty(stack) == true) return false;
    *item = stack->collection[stack->size -1];
    return true;
}

bool pop(Stack *stack, int *item)
{
    if (is_empty(stack)) return false;
    stack->size--; // pop function modification top of stock
    *item = stack->collection[stack->size];
    return true;
}