def startSwitch(arg):
    switch_case = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday"
    }
    return switch_case.get(arg)


dayOfWeek = startSwitch(2)

print(dayOfWeek)
