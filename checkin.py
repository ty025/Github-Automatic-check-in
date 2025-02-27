import os
from datetime import datetime

def generate_checkin_file():
    # 生成日期信息（北京时间）
    beijing_time = datetime.utcnow().replace(hour=8)  # GitHub Actions 默认UTC时间，+8小时转为北京时间
    date_str = beijing_time.strftime("%Y-%m-%d %H:%M:%S")

    # 写入文件（追加模式）
    with open("daily-log.txt", "a",encoding='utf-8') as f:
        f.write(f"自动签到时间: {date_str}\n")
        f.write(" 😎 👀 ✔\n")

    # print("✅ 签到文件已生成")

def git_commit_and_push():
    # 配置Git用户信息（必须设置，否则提交失败）
    os.system('git config --global user.name "xiname"')
    os.system('git config --global user.email "xinametravel@qq.com"')

    # 添加、提交
    os.system("git add daily-log.txt")
    os.system(f'git commit -m "Daily checkin: {datetime.utcnow().strftime("%Y-%m-%d")}"')
    os.system("git push origin main")
    # print("🚀 代码已提交到仓库")

if __name__ == "__main__":
    generate_checkin_file()
    git_commit_and_push()
