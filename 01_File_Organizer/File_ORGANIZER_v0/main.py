import os
import shutil

def start_automation(target_path):
    # 대상 폴더 안의 파일 목록 읽기 (자료구조: 리스트 활용)
    # os.listdir()은 폴더 내의 파일/폴더 이름을 리스트로 반환
    file_list = os.listdir(target_path)
    
    # 반복문(for)으로 파일 하나씩 살펴보기
    for filename in file_list:
        # 파일의 전체 경로를 만듬
        full_path = os.path.join(target_path, filename)
        
        # 조건문(if)으로 파일 종류 확인하기
        # 폴더가 아닌 '파일'인 경우에만 정리를 진행
        if os.path.isfile(full_path):
            # 파일 이름에서 확장자를 추출합니다. (예: .txt, .pdf)
            extension = os.path.splitext(filename)[1].strip('.').lower()
            
            # 확장자가 없는 파일(예: LICENSE)은 'others' 폴더로 분류합니다.
            if extension == '':
                extension = 'others'
            
            # 폴더 만들고 이동하기
            # 이동할 대상 폴더 경로 (예: ./target/pdf)
            destination_dir = os.path.join(target_path, extension)
            
            # 폴더가 없으면 새로 만듭니다.
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
            
            # 파일을 새 폴더로 이동시킵니다.
            shutil.move(full_path, os.path.join(destination_dir, filename))
            print(f"[이동 완료] {filename} -> {extension} 폴더")

if __name__ == "__main__":

    target_dir = input("정리하고 싶은 폴더의 전체 경로를 복사해서 붙여넣으세요: ")
    
    if os.path.exists(target_dir):
        start_automation(target_dir)
        print("정리가 완료되었습니다.")
    else:
        print("입력하신 경로가 존재하지 않습니다. 경로를 다시 확인해주세요.")

