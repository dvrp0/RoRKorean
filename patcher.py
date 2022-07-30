import os, shutil, wget, winreg

class Patcher:
    def __init__(self):
        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Valve\Steam", 0, winreg.KEY_ALL_ACCESS)
            path, _ = winreg.QueryValueEx(key, "InstallPath")
        except:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Wow6432Node\Valve\Steam", 0, winreg.KEY_ALL_ACCESS)
            path, _ = winreg.QueryValueEx(key, "InstallPath")
        finally:
            winreg.CloseKey(key)

        path_first = os.path.join(path, "steamapps", "common", "Risk of Rain")
        path_second = os.path.join(path, "SteamLibrary", "steamapps", "common", "Risk of Rain")

        self.path_failed = False
        self.download_url = "http://raw.githubusercontent.com/dvrp0/RoRKorean/main/"
        self.filename = "data.win"

        if os.path.exists(path_first):
            self.data_path = path_first
        elif os.path.exists(path_second):
            self.data_path = path_second
        else:
            print("게임 경로 발견되지 않음.")
            print(f"다운로드되는 {self.filename} 파일을 게임 경로로 직접 이동시키세요.")
            self.path_failed = True

    def download(self):
        print("패치 파일 다운로드 중...")
        wget.download(f"{self.download_url}/{self.filename}")
        print()
        print(f"완료. ({self.filename})")

        if self.path_failed:
            return
        
        target = os.path.join(os.getcwd(), self.filename)
        new = os.path.join(self.data_path, self.filename)

        print(f"{new}로 파일 이동 중...")
        shutil.move(target, new)
        print("완료.")

    def backup(self):
        target = os.path.join(self.data_path, self.filename)
        new = os.path.join(self.data_path, f"{self.filename}BACKUP")

        print(f"기존 번역 파일 백업 중...")

        if os.path.isfile(target):
            shutil.move(target, new)
            print("완료.")
        else:
            print("기존 번역 파일 발견되지 않음, 건너뜀.")

    def revert(self):
        target = os.path.join(self.data_path, f"{self.filename}BACKUP")
        new = os.path.join(self.data_path, self.filename)

        print(f"패치 되돌리는 중...")
        shutil.move(target, new)
        print("완료.")