#!/usr/bin/python
  # We need to:  access an external process; do easy
  # string substitution; and show a GUI.  These three
  # modules provide such functionality.
import commands, re, Tkinter

# Every second--one thousand milliseconds--this function
# gets the latest 'uptime' result, displays it, then
# reschedules itself for the next cycle.
def one_update():
    # This just collects the result of the external
    # built-in 'uptime' command.
    result = commands.getoutput("uptime")

    # Discard everything in the result string that
    # appears before the load averages themselves.
    pattern = ".*load averages*: "
    display_text.set(re.sub(pattern, "", result))

       # Do it again another second later.
    label.after(1000, one_update)

root = Tkinter.Tk()
  # Create a display "buffer".
display_text = Tkinter.StringVar()

  # Create a GUI widget which shows the results.
label = Tkinter.Label(root, textvariable = display_text, width = 20)

  # Place the Label in the main window.
label.pack()

  # Begin the measurements.
one_update()

  # Start processing events, that is, turn the GUI "on".
root.mainloop()

