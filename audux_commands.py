#       Import each file
import test

cmds = {
    #Voice command   command (expressed as function)
    "test"         : test
}


# --- DO NOT TOUCH: YOUR ASSISTANT WILL BREAK
def interpret_command(cmd, args : list = []):
    if cmd.val in cmds.keys(): cmds[cmd.val].fnc(args)
    # checks if the command exists,         then runs the function if it does
