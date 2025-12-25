import os
import shutil

# 충돌 방지(덮어쓰기) 함수
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

def start_automation(target_path):
    try:
        file_list = os.listdir(target_path)
    except Exception as e:
        print(f"[실패] 폴더 목록을 읽을 수 없습니다: {e}")
        return

    moved_count = 0  # 이동 성공 카운트

    for filename in file_list:
        # 숨김 파일/시스템 파일 스킵 (예: .DS_Store)
        if filename.startswith('.'):
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
                print(f"[이동 완료] {os.path.basename(dest_path)} -> {extension} 폴더")

            except Exception as e:
                print(f"[실패] {filename} ({e})")
                continue

    if moved_count == 0:
        print("[안내] 이동할 파일이 없습니다. (숨김 파일/폴더만 있거나 이미 정리된 상태일 수 있습니다.)")

if __name__ == "__main__":
    target_dir = input("정리하고 싶은 폴더의 전체 경로를 복사해서 붙여넣으세요: ")
    target_dir = target_dir.strip().strip('"').strip("'")

    if os.path.isdir(target_dir):
        start_automation(target_dir)
        print("정리가 완료되었습니다.")
    else:
        print("입력하신 경로가 존재하지 않거나 폴더가 아닙니다. 경로를 다시 확인해주세요.")
