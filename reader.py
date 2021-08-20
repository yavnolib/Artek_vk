class Read:
    what=''
    #выдает строку с идом идентифицированного чата и статусом (админ чат и т.д.)
    def __init__(self,chat_id,chat_status):
        self.chat_id=chat_id
        self.chat_status=chat_status
    def read(self):
        f=open('log.txt',mode='r')
        for line in f:
            self.what=self.what+line
            if str(self.chat_id) in line:
                itog=line
        f.close()
        if self.chat_status in itog:
            return 1
        else:
            return 0
#                                                     print(Read('13','admin_chat').read())
