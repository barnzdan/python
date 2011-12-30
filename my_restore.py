#!/usr/bin/python
  
# This is 'my_restore.py'.  Invoke it as, for example,
#    my_restore.py my_source.c
# to show all the archived files named 'my_source.c'
# which the user can select for retrieval.

  
import os,sys,Tkinter
  
pattern = sys.argv[1]
archive = '/dev/nrtape'
  
def esf():
        # Construct the string which lists all selected files, 
        #    separated by a single blank.  Use that string to 
        #    specify the exact listof files to extract from the 
        #    archive.
    command = 'tar xf %s %s' % (archive,
                ' '.join([lb.get(index) for index in lb.curselection()]))
    os.system(command)
  
    # MULTIPLE so that we can select and extract several files in a 
    #    single operation.
lb = Tkinter.Listbox(height = 12, width = 30, selectmode = Tkinter.MULTIPLE)
lb.pack()
Tkinter.Button(text = "Extract selected files", command = esf).pack()
  
    # The "[:-1]" says, "ignore the trailing newline tar emits".
for qualified_name in \
            os.popen('tar tf %s' % archive).read().split('\n')[:-1]:
        # Does the basename of this item match the pattern?
    if os.path.basename(qualified_name).count(pattern) > 0:
        lb.insert(Tkinter.END, qualified_name)
  
    # Show the GUI panel.
Tkinter.mainloop()
