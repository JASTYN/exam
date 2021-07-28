import os

print(os.name)


def main():
    f =open("text.txt","w+")
    
    for i in range (10):
        f.write("Th is is ths line")
        f.close
if __name__ == "__main__":
    main()