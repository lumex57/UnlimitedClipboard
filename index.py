import rumps

clipboard = []

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

if __name__ == "__main__":
    UnlimitedClipboards("UC").run()