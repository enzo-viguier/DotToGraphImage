digraph StackOfLinkedList {
    node [shape=box];
    
    // Main method
    start [label="Start"];
    create_stack [label="Create LinkedListStack"];
    push_1 [label="Push 1"];
    push_2 [label="Push 2"];
    push_3 [label="Push 3"];
    push_4 [label="Push 4"];
    push_5 [label="Push 5"];
    print_stack [label="Print stack"];
    print_size [label="Print size"];
    pop_5 [label="Pop (assert 5)"];
    pop_4 [label="Pop (assert 4)"];
    print_peek [label="Print peek"];
    end [label="End"];

    // Push method
    push_start [label="push(int x)"];
    create_node [label="Create new Node"];
    set_next [label="Set new Node.next to head"];
    update_head [label="Update head"];
    increment_size [label="Increment size"];
    push_return [label="Return true"];

    // Pop method
    pop_start [label="pop()"];
    pop_check_empty [label="Check if empty"];
    pop_throw_exception [label="Throw NoSuchElementException"];
    pop_get_head [label="Get head data"];
    pop_update_head [label="Move head to next"];
    pop_decrement_size [label="Decrement size"];
    pop_return [label="Return value"];

    // Peek method
    peek_start [label="peek()"];
    peek_check_empty [label="Check if empty"];
    peek_throw_exception [label="Throw NoSuchElementException"];
    peek_return [label="Return head.data"];

    // Main flow
    start -> create_stack;
    create_stack -> push_1 -> push_2 -> push_3 -> push_4 -> push_5;
    push_5 -> print_stack -> print_size;
    print_size -> pop_5 -> pop_4 -> print_peek -> end;

    // Push method flow
    push_start -> create_node -> set_next -> update_head -> increment_size -> push_return;

    // Pop method flow
    pop_start -> pop_check_empty;
    pop_check_empty -> pop_throw_exception [label="Empty"];
    pop_check_empty -> pop_get_head [label="Not Empty"];
    pop_get_head -> pop_update_head -> pop_decrement_size -> pop_return;

    // Peek method flow
    peek_start -> peek_check_empty;
    peek_check_empty -> peek_throw_exception [label="Empty"];
    peek_check_empty -> peek_return [label="Not Empty"];
}