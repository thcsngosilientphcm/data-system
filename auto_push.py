import subprocess
import datetime

def run(cmd):
    print(f"👉 {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        raise SystemExit("❌ Lỗi khi chạy lệnh Git")

# Tạo nội dung commit theo thời gian
msg = f"Auto update - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

run("git add .")
run(f'git commit -m "{msg}"')
run("git push")

print("🎉 Đã cập nhật lên GitHub thành công!")
