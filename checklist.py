checklist = list()


# CREATE
def create(item):
    checklist.append(item)


# READ
def read(index):
    return checklist[index]


# UPDATE
def update(index, item):
    checklist[index] = item


# DESTROY
def destroy(index):
    checklist.pop(index)


def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1


def mark_completed(index):
    checklist[index] = "\xe2" + checklist[index]
    list_all_items()


def user_input(prompt):
    user_i = input(prompt)
    return user_i


def select(function_code):
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)
    elif function_code == "R":
        item_index = int(user_input("Index Number?"))
        if(item_index < len(checklist)):
            print(read(item_index))
        else:
            print("Enter a valid index number.")
            print("Current index size: " + str(len(checklist)))
    elif function_code == "P":
        list_all_items()

    elif function_code == "Q":
        return False

    else:
        print("Unkown Option")

    return True


def test():
    user_value = user_input("Please enter a value:")
    print(user_value)
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")

    destroy(1)

    print(read(0))


test()

running = True
while running:
    selection = user_input(
    "Press C to add to list, R to read from the list, P to display the list and Q to quit.\n"
    )
    print(chr(27) + "[2J")
    running = select(selection)
