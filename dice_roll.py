#n dice roll sample space
def foo(n, rolls=[], roll=[]):
    if n > 0:
        for i in range(1,7):
            foo(n-1, rolls, roll+[i])
    else:
       rolls.append(roll)
    return rolls

print(rolls:=foo(3), "\n\n", [sum(roll) for roll in rolls])
