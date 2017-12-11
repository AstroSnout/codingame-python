for _ in range(int(input())):
    input()

# game loop
while True:
    print ("0 4" if int(input().split()[3]) < -39 else "0 0")
    # Dodgy scripting :S
