import sys 
print("Enter your line press ctrl + z if you want to end.")
try:
    lines = sys.stdin.readlines()

except EOFError:
    print("End of the file. ")

finally:
    for item in reversed(lines):
        print(item.strip())
