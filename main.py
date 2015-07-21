__author__ = 'adm'
import Image
import glob
import threading
div = 5
l = glob.glob('*.JPG')

class MyThread(threading.Thread):
    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        self.name = name
        self.counter = counter
    def run(self):
        main(self.name, self.counter)



def main(thread, i):
    for filename in xrange(0,4):
        i = i + 1
        im = Image.open(l[filename])
        width = im.size[0] / div
        height = im.size[1] / div
        im2 = im.resize((width, height), Image.NEAREST)
        im2.save(str(i) + str(thread) + ".jpg")


if __name__ == "__main__":
    t1 = MyThread('Thread - 1', 2)
    t1.start()
    t1.join()