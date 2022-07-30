from cx_Freeze import setup, Executable

build_options = dict(packages=["wget", "os", "shutil"])
exe = [Executable("main.py", target_name="RoRKoreanPatcher.exe")]
setup(
    name="RoRKoreanPatcher",
    version="0.1",
    author="DVRP",
    description="Risk of Rain 한국어화 패쳐",
    options=dict(build_exe=build_options),
    executables=exe
)