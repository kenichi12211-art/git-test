while True:
    word = input("自由に入力してください: ")
    if word.lower()== "q":
        break
    if any("\u3040"<=c<="\u9fff" for c in word):
        print("日本語です")
    elif any(("A"<=c<="Z")or("a"<=c<="z")for c in word):
        print("英語(English)です")
    else:
        print("記号又は他の言語です")
