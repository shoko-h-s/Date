# 曜日を求める
# 基準日：1800年1月1日 水曜日

y, m, d = map(int, input("曜日を求める日付を入力（yyyy/mm/dd）：").split("/"))

# 曜日変換用の辞書データ
era_list = {1: "水", 2: "木", 3: "金", 4: "土", 5: "日", 6: "月", 0: "火"}

# 経過日数用の変数
d_sum = 0

for i in range(1800, y+1):
    # 月リストは毎年更新
    month_list = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    
    # 2月部分の辞書データ確認、閏年の場合は数値を更新する
    if i % 4 == 0:
        if i % 400 == 0:
            month_list[2] = 29
        elif i % 100 == 0:
            pass
        else:
            month_list[2] = 29
    
    # ループ最後の年以外
    if i < y:
        y_days = sum(month_list.values())
        d_sum += y_days
    
    # ループ最後の年の場合
    else:
        while m > 0:
            # 前の月の日数を加算する
            if m >= 2:
                d_sum += month_list[m-1]
            else:
                d_sum += d
            m -= 1
            
week = d_sum % 7

print(f"{era_list[week]}曜日")
