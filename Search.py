import psycopg

connection = psycopg.connect(
    host='localhost',
    dbname='database',
    user='postgres',
    password='password',
)

# 1から12までの月を入力してもらう
month = input("1から12までの月を入力してください: ")

# 入力された文字列を整数に変換
try:
    user_month = int(month)

    # 入力された月が1から12の範囲にあるか確認
    if 1 <= user_month <= 12:
        # 1から31までの日を入力してもらう
        day = input("1から31までの日を入力してください: ")
        
        # 入力された文字列を整数に変換
        try:
            user_day = int(day)

            # 入力された日が1から31の範囲にあるか確認
            if 1 <= user_day <= 31:
                # 入力された月と日を変数に保存
                selected_month = user_month
                selected_day = user_day
                print(f"{selected_month}月{selected_day}日 のデータ")

                # SQL文のプレースホルダーを使用して、変数をクエリに組み込む
                sql = '''
                SELECT "花の名前", "花言葉", "星の名前", "星言葉", "星座", "宝石の名前", "宝石言葉", "酒の名前", "酒言葉"
                FROM "日付データ"
                JOIN "花データ" ON "日付データ"."花ID" = "花データ"."花ID"
                JOIN "星データ" ON "日付データ"."星ID" = "星データ"."星ID"
                JOIN "宝石データ" ON "日付データ"."宝石ID" = "宝石データ"."宝石ID"
                JOIN "酒データ" ON "日付データ"."酒ID" = "酒データ"."酒ID"
                WHERE 月 = %s AND 日 = %s;
                '''
                
                # プレースホルダーに値をセットしてクエリを実行
                result = connection.execute(sql, (selected_month, selected_day))

                for row in result:
                    # 各情報をフォーマットして表示
                    print(f"花の名前: {row[0]}  花言葉: {row[1]}")
                    print(f"星の名前: {row[2]}  星言葉: {row[3]}  星座: {row[4]}")
                    print(f"宝石の名前: {row[5]}  宝石言葉: {row[6]}")
                    print(f"酒の名前: {row[7]}  酒言葉: {row[8]}")
            else:
                print("エラー: 1から31までの範囲で日を入力してください。")
        except ValueError:
            print("エラー: 正しい形式の数字を入力してください。")
    else:
        print("エラー: 1から12までの範囲で月を入力してください。")
except ValueError:
    print("エラー: 正しい形式の数字を入力してください。")
