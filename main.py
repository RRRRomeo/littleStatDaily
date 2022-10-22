from mp32wav import audio_transfor
from mp32wav import handle

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file_name = '陈一发儿 - 童话镇.flac'
    file_dir = "~/media/xs/datas/test_music/"
    # audio_transfor(file_name, file_dir)
    handle("/media/xs/datas/test_music/", "/media/xs/datas/test_music/wav")
    print_hi('PyCharm')

