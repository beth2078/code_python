# Sorting Names and putting them in a .txt file

# 1. Read the names from names.txt and store them in a variable
names = [] #declare an empty list that can store our name in string values

with open("./names.txt", "r") as data_file: # r --> read
       for line in data_file.readlines():
          value = line.replace("\n", "") # for all strings we can use the .replace() method to replace  a old  pattern with a new pattern 
          names.append(value) # for all lists, we can use .append() to add the given argument to the back of the list
# end of getting names


# 2. Sort the names in the alphabetical order; we will  use the selection  sort algorithm 
i = 0
j = 0

while i < len(names):
    j = 1 + i

    smallest_name = names[i]
    smallest_index = j 
    while j < len(names):
        if names[j] < smallest_name:
            smallest_name = names[j]
            smallest_index = j
        j += 1 
    # end of inner while

    if smallest_name < names[i]:
        names[i], names[smallest_index] = names[smallest_index], names[i]

    i += 1
#end while

print(names)

# 3. Write the names into a new file called "sortedNames.txt"
# test = [3, 1, 4]
# initial_position = test[0]
# i = 1
# smallest_value = test{i}
# while i < len(test):
#     smallest_value = min(smallest_value, test[i])
#     i += 1

# if smallest_value < initial_position:
#     temp = initial_position
#     initial_position = smallest_value
#     smallest_value = temp
