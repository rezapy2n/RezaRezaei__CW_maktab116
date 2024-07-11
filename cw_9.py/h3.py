class CustomStack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = []

    def push(self, value):
        if len(self.stack) < self.max_size:
            self.stack.append(value)
        else:
            print("Stack is full. Cannot push more elements.")

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            print("Stack is empty. Cannot pop.")

    def __len__(self):
        return len(self.stack)

    def __repr__(self):
        return f"CustomStack({self.max_size})"


if __name__ == "__main__":
    my_stack = CustomStack(max_size=5)
    my_stack.push(80)
    my_stack.push(69)
    my_stack.push(96)
    print(f"Stack size: {len(my_stack)}")
    print(f"Stack representation: {my_stack}")
    popped_value = my_stack.pop()
    print(f"Popped value: {popped_value}")
    print(f"Stack size after popping: {len(my_stack)}")
