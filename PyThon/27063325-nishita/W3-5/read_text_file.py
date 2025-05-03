def count_underscores(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            count = content.count('__')
            print(f"Number of '__' in the file: {count}")
            return count
    except FileNotFoundError:
        print("File not found. Please check the file path.")

# Example usage
file_path = r'C:\Users\DELL\Documents\Professional-Software-Engineering\PyThon\27063325-nishita\W3-5\sample_text.txt'
count_underscores(file_path)
