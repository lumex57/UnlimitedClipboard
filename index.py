import rumps
import threading

clipboard = []
running = True

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
        print('ss')

# app = threading.Thread(target=runApp)
# clipboardWatcher = threading.Thread(target=runClipboardWatcher)


if __name__ == "__main__":
    
    clipboardWatcher = threading.Thread(target=runClipboardWatcher, daemon=True)
    clipboardWatcher.start()

    UnlimitedClipboards("UC").run()