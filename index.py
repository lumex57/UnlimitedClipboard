import rumps
import threading
import pyperclip
import time

clipboard = []
running = True
check_delay = 0.2

class UnlimitedClipboards(rumps.App):
    @rumps.clicked("Clear All Copies")
    def clearAllCopies(self, _):
        response = rumps.alert(
            title="Really?",
            message="진짜 지울거임?",
            ok="Comfirm", 
            cancel="Cancel"
        )

        if response == 1:
            print("clicked yes")

def runClipboardWatcher():
    while running:
        text = pyperclip.paste()
        print(text)

        if text:
            if not clipboard or clipboard[-1] != text:
                clipboard.append(text)
            else:
                print('마지막으로 복사한것과 같다.')

        else:
            print('클립보드가 비어있ㅇ음.')

        print(clipboard)
        time.sleep(check_delay)

if __name__ == "__main__":
    clipboardWatcher = threading.Thread(target=runClipboardWatcher, daemon=True)
    clipboardWatcher.start()

    UnlimitedClipboards("UC").run()