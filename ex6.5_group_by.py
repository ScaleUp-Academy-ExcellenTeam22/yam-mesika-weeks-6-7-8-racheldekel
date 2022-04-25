def group_by(function, iterable):
    dictionary = {}
    for item in iterable:
        if function(item) in dictionary.keys():
            dictionary[function(item)].extend([item])
        else:
            dictionary[function(item)] = [item]
    return dictionary


if __name__ == "__main__":
    lst = ["hi", "bye", "yo", "try"]
    print(group_by(len, lst))
