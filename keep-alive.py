import time

def keep_colab_alive():
    while True:
        print("Keeping Colab alive...")
        time.sleep(60)  # Chờ 60 giây trước khi thực hiện thao tác tiếp theo

if __name__ == "__main__":
    keep_colab_alive()