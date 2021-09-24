depth = ""
def make_rolls(dice_remaining, total_rolls = [], past_rolls = []):
    global depth
    print(f"{depth}calling make_rolls({dice_remaining}, {past_rolls})")
    depth += "  "

    if dice_remaining > 0:
        for i in range(1, 7):
            make_rolls(dice_remaining-1, total_rolls, past_rolls+[i])
    else:
        total_rolls.append(past_rolls)

    depth = depth[:-2]
    return total_rolls

make_rolls(2)
