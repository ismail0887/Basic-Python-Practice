try:
    with open('mytext1.txt') as file:
        file.read()
except:
    print("There is a failure in try block")

try:
    with open('mytext2.txt') as file:
        file.read()
except Exception as e:
    print(e)

finally:
    print("cleaning up resources")