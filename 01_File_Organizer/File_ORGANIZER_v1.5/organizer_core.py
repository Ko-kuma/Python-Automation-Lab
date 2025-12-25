import os
import shutil

#파일명 충돌(덮어쓰기) 방지를 위한 보조 함수
def get_available_dest_path(destination_dir, filename):
    dest_path = os.path.join(destination_dir, filename)
    if not os.path.exists(dest_path):
        return dest_path

    name, ext = os.path.splitext(filename)
    counter = 1
    while True:
        new_filename = f"{name}({counter}){ext}"
        candidate = os.path.join(destination_dir, new_filename)
        if not os.path.exists(candidate):
            return candidate
        counter += 1

def start_automation(target_path, log=None, include_hidden=False):
    def log_msg(msg: str):
        if log:
            log(msg)
        else:
            print(msg) 

    try:
        file_list = os.listdir(target_path)
    except Exception as e:
        log_msg(f"[실패] 폴더 목록을 읽을 수 없습니다: {e}")
        return 0  
    moved_count = 0

    for filename in file_list:
        if (not include_hidden) and filename.startswith('.'):
            continue

        full_path = os.path.join(target_path, filename)

        if os.path.isfile(full_path):
            try:
                extension = os.path.splitext(filename)[1].strip('.').lower()
                if extension == '':
                    extension = 'others'

                destination_dir = os.path.join(target_path, extension)
                os.makedirs(destination_dir, exist_ok=True)

                dest_path = get_available_dest_path(destination_dir, filename)
                shutil.move(full_path, dest_path)

                moved_count += 1
                log_msg(f"[이동 완료] {os.path.basename(dest_path)} -> {extension} 폴더")

            except Exception as e:
                log_msg(f"[실패] {filename} ({e})")
                continue

    if moved_count == 0:
        log_msg("[안내] 이동할 파일이 없습니다.")
    else:
        log_msg(f"[요약] 이동 완료: {moved_count}개")

    return moved_count 

# [중요] 기존 main.py에 있던 아래 블록은 organizer_core.py에서 제거됨
# if __name__ == "__main__":
#     input()으로 경로받고 실행하는 부분은 GUI(app_gui.py)가 담당해야 함
#     → core는 "기능 제공", UI는 "실행/입력" 분리(정석 구조)