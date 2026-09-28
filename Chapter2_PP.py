import os

print()
# Returns the absolute path of the current file
file_path = os.path.realpath(__file__)
print(f"File path: {file_path}")

# Returns the directory containing the current file
dir_path = os.path.dirname(os.path.realpath(__file__))
print(f"Directory: {dir_path}")

file_name = file_path.split("\\")[5]
print(f"Running from Python file: {file_name}")
print()


names = [" Tom", " Shelly ", " Garth "]
names_iter = iter(names)


# The following function uses a yield statement and returns a generator object
def gen_nums():

    # initial entry point
    n = 0
    while n < 4:

        # return and save where your at with yield and n,(Signals could be an entry and exit point)
        yield n

        # subsequent entry points after initial entry point
        n += 1

    # second entry and exit point, but since there's no line after this one
    # it is only an exit point
    yield "All Done"


# sequence is a generator
#sequence = gen_nums()

# Can loop through the generator
#for num in gen_nums():
    # print(num)
#print()


def safe_iteration(iterator):
    try:
        name = next(iterator)
        print(name)
        safe_iteration(iterator)
        return iterator
    except StopIteration:
        print()
        print("No more to iterate on.")


# safe_iteration(names_iter)


def gen_squares(max_num):
    for num in range(max_num):
        print(num)
        yield num ** 2
        print(f"The square of {num} = {num ** 2}" )


squares = gen_squares(5)

while True:
    try:
        next(squares)
    except StopIteration:
        break
