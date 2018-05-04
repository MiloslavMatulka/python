"""
This program counts characters.
The program reads from file "japanese_text.txt"
and found out how many characters is written in specified
japanese alphabets.

"""

# There can be used path as an input, e.g. H:/japanese_text.txt
japanese_text = input("Insert the name of your japanese text file: ")

# ひらがな(hiragana)
hiragana = """ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただち
            ぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめも
            ゃやゅゆょよらりるれろゎわゐゑをんゔ"""
# カタカナ(katakana)
katakana = """ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチ
            ヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモ
            ャヤュユョヨラリルレロヮワヰヱヲンヴヵヶヷヸヹヺ"""
counter_hir = 0
counter_kat = 0

try:
    with open(japanese_text, 'r', encoding="utf-8-sig") as file:
        preparation = file.read().split()
        contents = ''.join(preparation)
        for character in contents:
            if character in hiragana:
                counter_hir += 1
            elif character in katakana:
                counter_kat += 1
            else:
                pass
        print(f"File contains {counter_hir} hiragana characters.")
        print(f"File contains {counter_kat} katakana characters.")
except FileNotFoundError:
    print("File not found.")
