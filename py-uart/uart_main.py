#import uart_main.py
from uart_read import setup, read
from uart_write import write
import time
def main():
        setup()
        print("good bye world.")


if __name__ == "__main__":
    print("hello world")
    main()

