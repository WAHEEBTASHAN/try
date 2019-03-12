
print("Enter number of students inside the class")
students = int(input())
if students < 0:
    print("Wrong Entry: Try again")
    exit(1)
print("The Number of english alphabets is 26")
if students < 26:
    print("Pigeon rule does not apply:n<26")
elif students == 26:
    print("Pigeon rule does not apply")
    print("stuents  may or may not have same alphabets")
elif students > 26:
    print("Pigeon rule applies:n>m")
    result1 = students % 26
    result = float(students // 26)
    if result1 == 0:
        print(" Minimum number of students having the same alphbets:\n", result)
    else:
        print("Minimum number of people having the same alphbets:\n ", result + 1)
else:
    print("Invalid Input: Please select again")
