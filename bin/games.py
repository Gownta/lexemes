#!/usr/bin/python3

# ctrl-v uNNNN

Display = {
    "chess": (0x2654, 0x2660),
    "cards": (0x2660, 0x2668),
}

for grp, (lb, ub) in Display.items():
    print(grp)
    for i in range(lb, ub):
        print(f"  {hex(i)}  {chr(i)}")
