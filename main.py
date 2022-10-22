from mp32wav import audio_transfor
from mp32wav import handle

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print("%s\r\n" %name);


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('start trans')
    file_path = '/media/xs/datas/test_music/'
    file_name = '陈一发儿 - 童话镇.flac'
    # file_dir = '/media/xs/datas/code_space/python_code/mp32wav/童话镇.mp3'
    out_dir = '/media/xs/datas/code_space/python_code/mp32wav/'
    # audio_transfor(file_name, file_dir)
    handle(file_path+file_name)
    print_hi('trans end')

