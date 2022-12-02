# Find elves carrying the most calories
import numpy as np

filename = "calories.txt"
elf_delimiter = "\n\n" # Separates item entries from different elves
item_delimiter = "\n" # Separates item entries for the same elf

def read_elf_calories(calories_file):
    """ Read the text file with the item calories carried by each elf.
    Return a list of the total calories carried by each elf """
    elf_totals = [] # Total calories held by each elf
    with open(calories_file, 'r') as file:
        data = file.read() # Read entire dataset
        elf_datas = data.split(elf_delimiter) # Split dataset among different elves
        for ed in elf_datas:
            ed = ed.strip()
            elf_list = ed.split(item_delimiter) # Split elf dataset into items
            elf_list_int = [int(cals) for cals in elf_list] # Convert to int
            elf_totals += [sum(elf_list_int)]
    return elf_totals

def find_max_n(lx, n):
    " Given a list lx, return a list with the the maximum n entries."
    maxes = []
    for _ in range(n):
        imax = max(lx)
        maxes += [imax]
        lx.remove(imax)
    return(maxes)


elf_totals = read_elf_calories(filename)
max_elf_id = np.argmax(elf_totals)
max_elf_calories = elf_totals[max_elf_id]
print(f"Elf #{max_elf_id} is carrying the most calories ({max_elf_calories}).")

max_3_calories = find_max_n(elf_totals, 3)
max_3_total = sum(max_3_calories)
print(f"The three elves carrying the most calories hold a total of {max_3_total} calories.")