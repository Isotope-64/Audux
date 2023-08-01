import test

cmds = {
    #Voice command   command as function
    "test"         : test
}


# --- DO NOT TOUCH: YOUR ASSISTANT WILL BREAK
def interpret_command(cmd, args : list = []):
    if cmd.val in cmds.keys(): cmds[cmd.val].fnc(args)
