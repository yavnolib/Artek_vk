class new_admin:
    smth=''
    def __init__(self,text):
        self.text=text
    def readwrite(self):
        f=open('admins.txt',mode='r')
        loglog=open('helplog.txt', mode='w')
        for line in f:
            loglog.write(line)
        loglog.close()
        f.close()
        read=open('helplog.txt',mode='r')
        for line in read:
            self.smth=self.smth+line
        read.close()
        file=open('admins.txt',mode='w+')
        file.write(self.smth+'\n'+self.text)
        file.close()
