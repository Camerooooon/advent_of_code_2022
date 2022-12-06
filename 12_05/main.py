stream = input("STream: ")
print(stream)

recent = []
i = 0;
for char in stream:
    i += 1
    recent.append(char)
    print(recent);

    if len(recent) > 13:

        has_repeat = False
        repeat = []
        for item in recent:
            if item in repeat:
                has_repeat = True;
                print("Repeat item: " + item)
            repeat.append(item)

        if not has_repeat:
            print(str(i))
            exit();
        del recent[0]



