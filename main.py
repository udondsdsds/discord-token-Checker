import os
import time
import requests

def check_token(token: str):
    url = "https://discord.com/api/v9/users/@me"
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    }

    try:
        response = requests.get(url, headers=headers, timeout=3)

        if response.status_code == 200:
            return "valid"
        elif response.status_code in (401, 403):
            return "invalid"
        elif response.status_code == 429:
            return "ratelimit"

    except Exception:
        pass
    return "error"

def main():
    print("token Checker")
    print("-" * 40)

    if not os.path.exists("tokens.txt"):
        print("tokens.txt が見つかりません")
        return
    with open("tokens.txt", "r", encoding="utf-8") as f:
        tokens = [line.strip() for line in f if line.strip()]

    if not tokens:
        print("tokens.txt に有効なトークンが記載されていません。")
        return

    print(f"チェックを開始します\n")

    valid_list = []
    invalid_list = []

    try:
        for i, token in enumerate(tokens, 1):
            status = check_token(token)

            if status == "ratelimit":
                print("レート制限を検知しました。3秒待機します...")
                time.sleep(3)
                status = check_token(token) 


            if status == "valid":
                print(f"VALID")
                valid_list.append(token)
            elif status == "invalid":
                print(f"INVALID")
                invalid_list.append(token)
            else:

                print(f"[{i}/{len(tokens)}] [INVALID] (Error/Unknown)")
                invalid_list.append(token)

            time.sleep(0.5)

    except KeyboardInterrupt:
        print("\n\n結果を保存します。")

    with open("valid.txt", "w", encoding="utf-8") as f_valid:
        f_valid.write("\n".join(valid_list) + ("\n" if valid_list else ""))

    with open("invalid.txt", "w", encoding="utf-8") as f_invalid:
        f_invalid.write("\n".join(invalid_list) + ("\n" if invalid_list else ""))

    print("\n" + "=" * 40)
    print(" 処理が完了しました")
    print(f" - 有効 (Valid): {len(valid_list)} 件 -> valid.txt に保存")
    print(f" - 無効 (Invalid): {len(invalid_list)} 件 -> invalid.txt に保存")
    print("=" * 40)
    print("乙！")

if __name__ == "__main__":
    main()
