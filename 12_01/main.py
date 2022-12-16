
with open("input") as file:
    cal_string = file.read();
    elfs = []
    current_elf = 0
    for item in cal_string.split("\n"):
        if (item == ""):
            print(current_elf)
            elfs.append(current_elf)
            current_elf = 0;
        else:
            current_elf += int(item)

    elfs.sort()
    print("Highest: " + str(elfs[len(elfs)- 1]))
    print("Highest: " + str(elfs[len(elfs)- 2]))
    print("Highest: " + str(elfs[len(elfs)- 3]))
