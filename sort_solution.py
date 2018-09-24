data = ["a", "b", "c", "d", "e", 0, 1, 0, 0, "f", "g", "h", False, False, "i", "j"]

def sort_list(some_list):
    numbers = []
    new_data = []

    for entry in data:
        if isinstance(entry, int) and not isinstance(entry, bool):
            numbers.append(entry)
        else:
            continue

    for entry in data:
        if isinstance(entry, str) or isinstance(entry, bool):
            new_data.append(entry)

    some_list = new_data + numbers
    print(some_list)

sort_list(data)