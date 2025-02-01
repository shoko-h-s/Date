# 西暦の和暦変換
# 明治以降に対応

y, m, d = map(int, input("変換する日付を入力（yyyy/mm/dd）：").split("/"))

# 和暦変換用の辞書データ
era_list = {"明治": 1867, "大正": 1911, "昭和": 1925, "平成": 1988, "令和": 2018}


# 元号の判定
if y <= 1911:
    era_name = "明治"
    
elif y == 1912:
    if (m <= 6) or ((m == 7) and (d <= 29)):
        era_name = "明治"
    else:
        era_name = "大正"

elif y <= 1925:
    era_name = "大正"
    
elif y == 1926:
    if not ((m == 12) and (d >= 25)):
        era_name = "大正"
    else:
        era_name = "昭和"  

elif y <= 1988:
    era_name = "昭和"
    
elif y == 1989:
    if (m == 1) and (d <= 7):
        era_name = "昭和"
    else:
        era_name = "平成"  
        
elif y <= 2018:
    era_name = "平成"
    
else:
    if (y == 2019) and (m <= 4):
        era_name = "平成"
    else:
        era_name = "令和"  

# 和暦への変換処理
era_year = y - era_list[era_name]

# 1年の場合は元年に直す
if era_year == 1:
    era_year = "元"
        
print(f"{era_name}{era_year}年{m}月{d}日")
