def name(filename):
    fileobj = open(filename, 'r', encoding="utf-8")     # Open the file.
    dic = {}                                            # Initialize the dictionary.
    fileobj.readline()                                  # Ignore the heading (the file's first line is "Name", so we wanna avoid that line).

    for line in fileobj:
        line_split = line.strip().split(" ")            # Remove the "\n" and split the name between spaces.

        if line_split[-1] not in dic.keys():
            dic[line_split[-1]] = {line_split[0]}       # Create a new dictionary key. The first value is a set with the first name corresponding to that surname.
        
        else:
            dic[line_split[-1]].add(line_split[0])      # Add the first name to the set.
    
    fileobj.close()                                     # Close the file.
    return dic                                          # Return the dictionary.


def main():
    filename = "names.txt"                              # WARNING!!!1!1! This line requires you to have this file in the same folder as this script. Move your ass and check that.
    dic = name(filename)                                # Associate the variable "dic" to the called function.
    for key, value in dic.items():
        print(key, ":", value)                          # Print each item of the dictionary in a new line.

main()