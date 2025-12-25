import os
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QFileDialog, QLineEdit, QTextEdit, QCheckBox, QMessageBox
)
from organizer_core import start_automation

class OrganizerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Organizer (GUI v2)")
        self.resize(700, 500)

        layout = QVBoxLayout()

        self.path_input = QLineEdit()
        self.path_input.setPlaceholderText("정리할 폴더 경로를 선택하세요")
        layout.addWidget(self.path_input)

        self.btn_browse = QPushButton("폴더 선택")
        self.btn_browse.clicked.connect(self.choose_folder)
        layout.addWidget(self.btn_browse)

        self.include_hidden = QCheckBox("숨김 파일 포함")
        layout.addWidget(self.include_hidden)

        self.btn_run = QPushButton("실행")
        self.btn_run.clicked.connect(self.run_organizer)
        layout.addWidget(self.btn_run)

        self.log_box = QTextEdit()
        self.log_box.setReadOnly(True)
        layout.addWidget(self.log_box)

        self.setLayout(layout)

    def choose_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "정리할 폴더 선택")
        if folder:
            self.path_input.setText(folder)

    def append_log(self, msg: str):
        self.log_box.append(msg)

    def run_organizer(self):
        target_dir = self.path_input.text().strip().strip('"').strip("'")

        if not os.path.isdir(target_dir):
            QMessageBox.warning(self, "경고", "유효한 폴더 경로가 아닙니다.")
            return

        self.log_box.clear()
        self.append_log(f"[시작] 대상 폴더: {target_dir}")

        start_automation(
            target_dir,
            log=self.append_log,
            include_hidden=self.include_hidden.isChecked()
        )

        self.append_log("[완료]")

if __name__ == "__main__":
    app = QApplication([])
    w = OrganizerApp()
    w.show()
    app.exec()