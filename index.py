import rumps

clipboard = []

class UnlimitedClipboards(rumps.App):
    @rumps.clicked("Clear All Copies")
    def clearAllCopies(self, _):
        print("delete buttonn")

if __name__ == "__main__":
    UnlimitedClipboards("UC").run()