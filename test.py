from tkinter import *
import threading

class MyApp:
    def __init__(self, root):
        self.root = root
        self.timer_evt = threading.Event()
        cf = Frame(root, borderwidth=1, relief="raised")
        cf.pack()
        Button(cf, text="Run", command=self.Run).pack(fill=X)
        Button(cf, text="Pause", command=self.Pause).pack(fill=X)
        Button(cf, text="Kill", command=self.Kill).pack(fill=X)

    def process_stuff(self):        # processing threads
        while self.go:
            print("Spam... ")
            self.timer_evt.wait()
            self.timer_evt.clear()

    def Run(self):                  # start another thread
        self.go = 1
        threading.Thread(target=self.process_stuff, name="_proc").start()
        self.root.after(0, self.tick)

    def Pause(self):
        self.go = 0

    def Kill(self):                 # wake threads up so they can die
        self.go = 0
        self.timer_evt.set()

    def tick(self):
        if self.go:
            self.timer_evt.set()    # unblock processing threads
            self.root.after(1000, self.tick)

def main():
    root = Tk()
    root.title("ProcessingThread")
    app = MyApp(root)
    root.mainloop()

main()