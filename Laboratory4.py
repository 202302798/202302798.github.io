def ascii_visualizer():
    # for inputs
    sentence = input("Enter a sentence: ")
    symbol = input("Enter the symbol or character to display: ")
    
    print("--- Output ---")
    
    # che-check each character
    for char in sentence:
        ascii_value = ord(char)
        count = ascii_value % 15
        
        if count == 0:
            count = 15
            
        print(f"'{char}' (Count: {count:2}) -> {symbol * count}")

if __name__ == "__main__":
    ascii_visualizer()