class Creator:
    smth=''
    def __init__(self,text):
        self.text=text
    def readwrite(self):
        f=open('log.txt',mode='r', encoding='utf-8')
        loglog=open('helplog.txt', mode='w', encoding='utf-8')
        for line in f:
            loglog.write(line)
        loglog.close()
        f.close()
        read=open('helplog.txt',mode='r', encoding='utf-8')
        for line in read:
            self.smth=self.smth+line
        read.close()
        file=open('log.txt',mode='w+', encoding='utf-8')
        file.write(self.smth+'\n'+self.text)
        file.close()

#Creator('he').readwrite()
