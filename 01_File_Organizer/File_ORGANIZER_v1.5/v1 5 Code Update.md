# v1.5 Code Update

---

추가 및 변경 코드

- 기존 Main코드는 organizer_core.py로 변경
- GUI통합으로 변경 및 추가, 수정 코드

추가 코드

def start_automation(target_path, log=None, include_hidden=False):

- 추가 이유
    
    (log = None, include_hidden=False): 함수 인자 추가 
    
    GUI가 core에 [출력 함수]와 [옵션 상태(체크 박스)]를 전달 해야함
    

def log msg(msg: str)

if log :

 log(msg)

else :

print(msg)

- 추가 이유
    
    GUI에서는 print()가 화면(창)에 안 보이니까, **GUI 텍스트 박스에 찍을 수 있게 출력 통로를 함수로 분리**한 것.
    
    →“출력을 바꾸기”가 아니라 “출력을 *주입 가능*하게 만들어서 GUI에 연결”하는 것.
    

log_msg(f"[실패] 폴더 목록을 읽을 수 없습니다: {e}")

return 0

- 추가 이유
    
    os.listdir()가 실패하면 그 뒤 작업이 불가능해서 즉시 종료가 맞고, GUI에서는 조용히 죽으면 안 되니 실패 사유를 로그로 남기고, 호출한 쪽이 판단 할 수 있게 숫자(0)로 반환.
    
    →GUI입장에서 [실패 화면에 보여주고, 실행 결과를 숫자로 알 수 있게]만드는 것
    
    →return 0 는 [성공 0개]의 의미도 있지만, 더 정확히는 [작업이 시작도 못 했음을 나타내는 결과 값] 으로 사용
    

 if (not include_hidden) and filename.startswith('.'):

continue

- 추가 이유
    
    숨김 파일 처리 정책을 하드 코딩하지 않고, GUI체크 박스로 켜고 끌 수 있게 옵션화 한 것
    
    →GUI에서 [사용자 선택]으로 만들기 위함
    
    → 하드코딩은 코드에서 변수나 값을 직접 코드에 고정하는 방식을 의미
    

log_msg(f"[이동 완료] {os.path.basename(dest_path)} -> {extension} 폴더")

except Exception as e:

    log_msg(f"[실패] {filename} ({e})")

    continue

    if moved_count == 0:

        log_msg("[안내] 이동할 파일이 없습니다.")

    else:

        log_msg(f"[요약] 이동 완료: {moved_count}개")

    return moved_count

- 수정 및 추가 이유
    
    GUI에서는 진행 상황/결과가 콘솔이 아니라 사용자 인터페이스에 맞춰 창으로 보여야 하므로 전부 log_msg로 통일 
    
    한 파일 실패해도 계속 처리(continue)+0개일 때 안내는 GUI UX에서 매우 중요하기 때문([눌렀을 시 미 반응 방지])
    
    GUI에서 [처리결과]를 요약/표시 하거나, 나중에 테스트/자동화에서 검증 할 때 필요
    
    (return moved_count)
    
    →[사용자에게 보이게] + [도구처럼 안정적으로]
    

---

## English Translation

Additional and Modified Code

- Existing Main code has been renamed to organizer_core.py
- Changes and additions for GUI integration

Added Code

def start_automation(target_path, log=None, include_hidden=False):

- Reason for Addition(log = None, include_hidden=False): Added function parametersGUI needs to pass [output function] and [option state (checkbox)] to core

def log_msg(msg: str)

if log:

log(msg)

else:

print(msg)

- Reason for AdditionSince print() is not visible in the GUI window, **separated the output channel into a function so it can be printed to the GUI text box**.→ Not "changing the output" but "making the output *injectable* to connect with the GUI".

log_msg(f"[Failed] Unable to read folder list: {e}")

return 0

- Reason for AdditionIf os.listdir() fails, subsequent tasks are impossible, so immediate termination is correct. In GUI, it shouldn't die silently, so log the failure reason and return a number (0) so the caller can make decisions.→ From GUI perspective, [show on screen and make execution result available as a number]→ return 0 means [0 successes] but more precisely, it's a [result value indicating the task couldn't even start]

if (not include_hidden) and filename.startswith('.'):

continue

- Reason for AdditionMade hidden file processing policy optional through GUI checkbox instead of hard-coding, so it can be toggled on/off→ To make it a [user choice] in GUI→ Hard-coding means directly fixing variables or values in the code

log_msg(f"[Move Complete] {os.path.basename(dest_path)} -> {extension} folder")

except Exception as e:

log_msg(f"[Failed] {filename} ({e})")

continue

if moved_count == 0:

log_msg("[Notice] No files to move.")

else:

log_msg(f"[Summary] Move complete: {moved_count} files")

return moved_count

- Reason for Modification and AdditionIn GUI, progress/results should be shown in a window suited to the user interface rather than console, so unified everything to log_msgEven if one file fails, continue processing (continue) + notice when 0 files is very important for GUI UX ([prevents no response when clicked])Needed for summarizing/displaying [processing results] in GUI or for verification in testing/automation later(return moved_count)→ [Make visible to user] + [Stable like a tool]

---

## 日本語翻訳

追加および変更コード

- 既存のMainコードはorganizer_core.pyに変更
- GUI統合のための変更および追加、修正コード

追加コード

def start_automation(target_path, log=None, include_hidden=False):

- 追加理由(log = None, include_hidden=False): 関数引数を追加GUIがcoreに[出力関数]と[オプション状態(チェックボックス)]を渡す必要がある

def log_msg(msg: str)

if log:

log(msg)

else:

print(msg)

- 追加理由GUIではprint()が画面(ウィンドウ)に表示されないため、**GUIテキストボックスに出力できるように出力経路を関数として分離**した。→「出力を変える」のではなく「出力を*注入可能*にしてGUIに接続」すること。

log_msg(f"[失敗] フォルダリストを読み取れません: {e}")

return 0

- 追加理由os.listdir()が失敗すると、その後の作業が不可能なので即座に終了するのが正しく、GUIでは静かに終了してはいけないので失敗理由をログに残し、呼び出し側が判断できるように数値(0)で返す。→ GUI側からは[失敗を画面に表示し、実行結果を数値で把握できるように]する→ return 0は[成功0個]の意味もあるが、より正確には[作業が開始すらできなかったことを示す結果値]として使用

if (not include_hidden) and filename.startswith('.'):

continue

- 追加理由隠しファイル処理ポリシーをハードコーディングせず、GUIチェックボックスでオン/オフできるようにオプション化した→ GUIで[ユーザー選択]にするため→ ハードコーディングはコードで変数や値を直接コードに固定する方式を意味する

log_msg(f"[移動完了] {os.path.basename(dest_path)} -> {extension} フォルダ")

except Exception as e:

log_msg(f"[失敗] {filename} ({e})")

continue

if moved_count == 0:

log_msg("[案内] 移動するファイルがありません。")

else:

log_msg(f"[要約] 移動完了: {moved_count}個")

return moved_count

- 修正および追加理由GUIでは進行状況/結果がコンソールではなくユーザーインターフェースに合わせてウィンドウで表示する必要があるため、すべてlog_msgに統一1つのファイルが失敗しても処理を続行(continue)+0個の時の案内はGUI UXで非常に重要([クリック時の無反応を防止])GUIで[処理結果]を要約/表示したり、後でテスト/自動化で検証する際に必要(return moved_count)→[ユーザーに見えるように] + [ツールのように安定的に]

---