def count_char(text, ch):
    count = 0
    for c in text:
        if c == ch:
            count += 1
    return count

def main():
    text = input()
    ch = input()
    print(f"{ch}\t{count_char(text, ch)}")

