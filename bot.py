import beseda
import beseda_real
try:
    t2=beseda_real.Chat()
    t2.start()
except:
    pass
beseda.User.listen()
