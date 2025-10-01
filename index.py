import rumps
import threading
import pyperclip
import time
from rumps import *


class UnlimitedClipboards(rumps.App):
    def __init__(self):
        super().__init__("ww")
        self.clipboard = []
        self.running = True
        self.check_delay = 0.2
        self.menu = ['Clear All Copies']
        threading.Thread(target=self.runClipboardWatcher, daemon=True).start()


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

    def runClipboardWatcher(self):
        lst = ""
        while self.running:
            try:
                text = pyperclip.paste()
                if text != lst and text.strip() != "":
                    lst = text
                    self.clipboard.append(text)
                    self.menu.add(text)
            except:
                print('idc')

            print(self.clipboard)
            time.sleep(self.check_delay)
    
    @rumps.clicked('Clear All Copies')
    def clear_all(self, _):
        self.clipboard.clear()
        self.menu.clear()
        self.menu.add("Clear All Copies")
        rumps.alert("Done.")

if __name__ == "__main__":
    UnlimitedClipboards().run()