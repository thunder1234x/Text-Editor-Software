import tkinter as tk  
from tkinter import ttk
from tkinter import colorchooser ,messagebox,filedialog,font
import os

main_application=tk.Tk()
main_application.geometry('1200x800')
main_application.title('RB_Oficial Text Editor')
main_application.wm_iconbitmap('icon.ico')


########################################   Start MainMenu      #####################################

main_menu =tk.Menu()

#file icons
new_icon=tk.PhotoImage(file='icons2/new.png')
open_icon=tk.PhotoImage(file='icons2/open.png')
save_icon=tk.PhotoImage(file='icons2/save.png')
save_as_icon=tk.PhotoImage(file='icons2/save_as.png')
exit_icon=tk.PhotoImage(file='icons2/exit.png')

#file
file=tk.Menu(main_menu,tearoff=False)

#edit icons
copy_icon=tk.PhotoImage(file='icons2/copy.png')
paste_icon=tk.PhotoImage(file='icons2/paste.png')
cut_icon=tk.PhotoImage(file='icons2/cut.png')
clear_all_icon=tk.PhotoImage(file='icons2/clear_all.png')
find_icon=tk.PhotoImage(file='icons2/find.png')

#edit
edit=tk.Menu(main_menu,tearoff=False)

#view icons
toolbar_icon=tk.PhotoImage(file='icons2/tool_bar.png')
statusbar_icon=tk.PhotoImage(file='icons2/status_bar.png')

#view
view=tk.Menu(main_menu,tearoff=False)

#color_theme image
light_default_icon=tk.PhotoImage(file='icons2/light_default.png')
light_plus_icon=tk.PhotoImage(file='icons2/light_plus.png')
dark_icon=tk.PhotoImage(file='icons2/dark.png')
red_icon=tk.PhotoImage(file='icons2/red.png')
monokai_icon=tk.PhotoImage(file='icons2/monokai.png')
night_blue_icon=tk.PhotoImage(file='icons2/night_blue.png')

#color_theme
color_theme=tk.Menu(main_menu,tearoff=False)
theme_choice=tk.StringVar()
color_icons=(light_default_icon,light_plus_icon,dark_icon,red_icon,monokai_icon,night_blue_icon)

color_dict={
    'Light Default':('#000000','#ffffff'),
    'Light Plus':('#474747','#e0e0e0'),
    'Dark':('#c4c4c4','#2d2d2d'),
    'Red':('#2d2d2d','#ffe8e8'),
    'Monokai':('#d3b774','#474747'),
    'Night Blue':('#ededed','#6b9dc2')
    }


#cascade
main_menu.add_cascade(label='File',menu=file)
main_menu.add_cascade(label='Edit',menu=edit)
main_menu.add_cascade(label='View',menu=view)
main_menu.add_cascade(label='Color Theme',menu=color_theme)

# -------------------------------&&&&&&&&&&  End MainMenu        &&&&&&&&&&&&&------------------------


########################################    Start tootlBar        #####################################

tool_bar=ttk.Label(main_application)
tool_bar.pack(side=tk.TOP,fill=tk.X)

#font box
font_tuple=tk.font.families()
font_family=tk.StringVar()
font_box=ttk.Combobox(tool_bar,width=30,textvariable=font_family,state='readonly')
font_box['values']=font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0,column=0,padx=5)

#size box
size_var=tk.IntVar()
size_box=ttk.Combobox(tool_bar,width=14,textvariable=size_var,state='readonly')
size_box['values']=tuple(range(8,81,2))
size_box.current(2)
size_box.grid(row=0,column=1,padx=5)

#bold button
bold_icon=tk.PhotoImage(file='icons2/bold.png')
bold_button=ttk.Button(tool_bar,image=bold_icon)
bold_button.grid(row=0,column=2)

#italic button
italic_icon=tk.PhotoImage(file='icons2/italic.png')
italic_button=ttk.Button(tool_bar,image=italic_icon)
italic_button.grid(row=0,column=3,padx=5)

#underline button
underline_icon=tk.PhotoImage(file='icons2/underline.png')
underline_button=ttk.Button(tool_bar,image=underline_icon)
underline_button.grid(row=0,column=4,padx=5)

#fontcolor Button
fontcolor_icon=tk.PhotoImage(file='icons2/font_color.png')
font_color_button=ttk.Button(tool_bar,image=fontcolor_icon)
font_color_button.grid(row=0,column=5,padx=5)

#align left Button
align_left_icon=tk.PhotoImage(file='icons2/align_left.png')
align_left_button=ttk.Button(tool_bar,image=align_left_icon)
align_left_button.grid(row=0,column=6,padx=5)

#align center button
align_center_icon=tk.PhotoImage(file='icons2/align_center.png')
align_center_button=ttk.Button(tool_bar,image=align_center_icon)
align_center_button.grid(row=0,column=7,padx=5)

#align right button
align_right_icon=tk.PhotoImage(file='icons2/align_right.png')
align_right_button=ttk.Button(tool_bar,image=align_right_icon)
align_right_button.grid(row=0,column=8,padx=5)

# -------------------------------&&&&&&&&&&  End   toolbar      &&&&&&&&&&&&&------------------------


########################################    Start Text Editor        #####################################

text_editor =tk.Text(main_application)
text_editor.config(wrap='word',relief=tk.FLAT)

scroll_bar=tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

#font family and size choice functionality
current_font_family='Arial'
current_font_size=12
italic='roman'
bold='normal'
underline_dict={0:'normal',1:'underline'}
underline=0

def change_font_family(main_applications):
    global current_font_family
    current_font_family=font_family.get()
    text_editor.configure(font=(current_font_family,current_font_size,bold,italic,underline_dict[underline]))

def change_font_size(main_applications):
    global current_font_size
    current_font_size=size_var.get()
    text_editor.configure(font=(current_font_family,current_font_size,bold,italic,underline_dict[underline]))

font_box.bind("<<ComboboxSelected>>",change_font_family)
size_box.bind("<<ComboboxSelected>>",change_font_size)

#buttons functionality

#bold button
def change_weight():
    global bold
    current_weight=tk.font.Font(font=text_editor['font'])
    if current_weight.actual()['weight']=='normal':
        bold='bold'
        text_editor.configure(font=(current_font_family,current_font_size,bold,italic))
    else:
        bold='normal'
        text_editor.configure(font=(current_font_family,current_font_size,bold,italic))

bold_button.configure(command=change_weight)

#italic button
def change_italic():
    global italic
    current_style=tk.font.Font(font=text_editor['font'])
    if current_style.actual()['slant']=='roman':
        italic='italic'
        text_editor.configure(font=(current_font_family,current_font_size,bold,italic,underline_dict[underline]))
    else:
        italic='roman'
        text_editor.configure(font=(current_font_family,current_font_size,bold,italic,underline_dict[underline]))

italic_button.configure(command=change_italic)

#underline button
def change_underline():
    global underline
    current_line=tk.font.Font(font=text_editor['font'])
    if current_line.actual()['underline']==0:
        underline=1
        text_editor.configure(font=(current_font_family,current_font_size,bold,italic,'underline'))
    else:
        underline=0
        text_editor.configure(font=(current_font_family,current_font_size,bold,italic,'normal'))

underline_button.configure(command=change_underline)

def change_font_color():
    color_var=tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])

font_color_button.configure(command=change_font_color)

#left alignment button
def left_align():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'left')

align_left_button.configure(command=left_align)

#center alignment button
def center_align():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'center')

align_center_button.configure(command=center_align)

#right alignment button
def right_align():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'right')

align_right_button.configure(command=right_align)

text_editor.configure(font=('Arial',12,bold,italic,underline_dict[underline]))
# -------------------------------&&&&&&&&&&  End  text editor       &&&&&&&&&&&&&------------------------


########################################     Start Status Bar      #####################################

status_bar=ttk.Label(main_application,text='Status Bar')
status_bar.pack(side=tk.BOTTOM)

text_changed=False
def change(main_application):
    global text_changed
    if text_editor.edit_modified():
        text_changed=True
        words=len(text_editor.get(1.0,'end-1c').split())
        characters=len(text_editor.get(1.0,'end-1c'))
        status_bar.configure(text=f'Characters: {characters}, words: {words}')
    text_editor.edit_modified(False)

text_editor.bind('<<Modified>>',change)

# -------------------------------&&&&&&&&&&   End  status bar      &&&&&&&&&&&&&------------------------


########################################  Command of Main Menu          #####################################

#variable name
url=''

#new file functinality
def new_file(event=None):
    global url
    url=''
    text_editor.delete(1.0,'end')
    main_application.title('undefiend')
#new file command
file.add_command(label='New',image=new_icon,compound=tk.LEFT,accelerator='Ctrl+N',command=new_file)

#open file functionality
def open_file(event=None):
    global url
    url=tk.filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File',filetype=(('Text File','*.txt'),('All Files','*.*')))
    try:
        with open(url,'r') as f:
            text_editor.delete(1.0,'end')
            text_editor.insert(tk.INSERT,f.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(url))
#open file command
file.add_command(label='Open',image=open_icon,compound=tk.LEFT,accelerator='Ctrl+O',command=open_file)

#save file functionality
def save_file(event=None):
    global url
    try:
        if url:
            content=str(text_editor.get(1.0,'end'))
            with open(url,'w',encoding='utf-8') as f:
                f.write(content)
        else:
            url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetype=(('Text File','*.txt'),('All Files','*.*')))
            content=text_editor.get(1.0,'end')
            url.write(content)
            # main_application.title(os.path.basename(url))
            url.close()
    except:
        return
    
#save file command
file.add_command(label='Save',image=save_icon,compound=tk.LEFT,accelerator='Ctrl+S',command=save_file)

#save as functionality
def save_as(event=None):
    global url
    if url:
        content=text_editor.get(1.0,'end')
        with open(url,'w',encoding='utf-8') as f:
            f.write(content)  
    else:
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetype=(('Text File','*.txt'),('All Files','*.*')))
        content=text_editor.get(1.0,'end')
        try:
            url.write(content)
            url.close()
        except:
            return
#save as command
file.add_command(label='Save As',image=save_as_icon,compound=tk.LEFT,accelerator='Alt+S',command=save_as)

#exit functionality
def exit_func(event=None):
    global url,text_changed
    try:
        if text_changed:
            mbox=messagebox.askyesnocancel('Warning','Do you wants to save it?')
            if mbox is True:
                if url:
                    content=str(text_editor.get(1.0,'end'))
                    with open(url,'w') as f:
                        f.write(content)
                        main_application.destroy()
                else:
                    url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetype=(('Text File','*.txt'),('All Files','*.*')))
                    content=text_editor.get(1.0,'end')
                    url.write(content)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return
#exit button command
file.add_command(label='Exit',image=exit_icon,compound=tk.LEFT,accelerator='Ctrl+Q',command=exit_func)


# edit command

#find functionality
def find_text(event=None):

    def find():
        word = find_input.get()
        text_editor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break 
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match', foreground='red', background='yellow')
    

    def replace():
            word=find_input.get()
            replace_word=replace_input.get()
            content=text_editor.get(1.0,tk.END)
            new_content=content.replace(word, replace_word)
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,new_content)

    find_dialouge=tk.Toplevel()
    find_dialouge.geometry('450x250+500+200')
    find_dialouge.title('Find')
    find_dialouge.resizable(0,0)

    #frame
    find_frame=ttk.LabelFrame(find_dialouge,text='Find/Replace')
    find_frame.pack(pady=20)
    #labels
    text_find_label=ttk.Label(find_frame,text='Find')
    text_replace_label=ttk.Label(find_frame,text='Replace')
    #entry
    find_input=ttk.Entry(find_frame,width=30)
    replace_input=ttk.Entry(find_frame,width=30)
    #buttons
    find_button=ttk.Button(find_frame,text='Find',command=find)
    replace_button=ttk.Button(find_frame,text='Replace',command=replace)

    #labels grid
    text_find_label.grid(row=0,column=0,padx=4,pady=4)
    text_replace_label.grid(row=1,column=0,padx=4,pady=4)
    #entry greed
    find_input.grid(row=0,column=1,padx=5,pady=5)
    replace_input.grid(row=1,column=1,padx=5,pady=5)
    #buttons grid
    find_button.grid(row=2,column=0,padx=8,pady=4)
    replace_button.grid(row=2,column=1,padx=8,pady=4)

    find_dialouge.mainloop()

#edit command with functionality
edit.add_command(label='Copy',image=copy_icon,compound=tk.LEFT,accelerator='Ctrl+C',command=lambda: text_editor.event_generate('<Control c>'))
edit.add_command(label='Paste',image=paste_icon,compound=tk.LEFT,accelerator='Ctrl+V',command=lambda:text_editor.event_generate('<Control v>'))
edit.add_command(label='Cut',image=cut_icon,compound=tk.LEFT,accelerator='Ctrl+X',command=lambda:text_editor.event_generate('<Control x>'))
edit.add_command(label='Clear All',image=clear_all_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+X',command=lambda:text_editor.delete(1.0,tk.END))

#find text command
edit.add_command(label='Find',image=find_icon,compound=tk.LEFT,accelerator='Ctrl+F',command=find_text)

# view command
#variable
show_toolbar=tk.BooleanVar()
show_toolbar.set(True)
show_statusbar=tk.BooleanVar()
show_statusbar.set(True)

#toolbar toggle functionality
def toggle_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill=tk.X)
        text_editor.pack(fill=tk.BOTH,expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar=True
#toggle status bar functionality
def toggle_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False 
    else :
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar = True 

#toggle toolbar command
view.add_checkbutton(label='Tool Bar',onvalue=True,offvalue=False,variable=show_toolbar,image=toolbar_icon,compound=tk.LEFT,command=toggle_toolbar)
#toggle statusbar command
view.add_checkbutton(label='Status Bar',onvalue=True,offvalue=False,variable=show_statusbar,image=statusbar_icon,compound=tk.LEFT,command=toggle_statusbar)

#color theme functionality
def change_theme():
    chosen_theme = theme_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text_editor.config(background=bg_color, fg=fg_color)
#color theme command
count=0
for i in color_dict:
    color_theme.add_radiobutton(label=i,image=color_icons[count],variable=theme_choice,compound=tk.LEFT,command=change_theme)
    count+=1

# -------------------------------&&&&&&&&&&   End  command      &&&&&&&&&&&&&------------------------

main_application.config(menu=main_menu)

#bind shortcut keys
main_application.bind('<Control-n>',new_file)
main_application.bind('<Control-o>',open_file)
main_application.bind('<Control-s>',save_file)
main_application.bind('<Alt-s>',save_as)
main_application.bind('<Control-q>',exit_func)
main_application.bind('<Control-f>',find_text)

main_application.mainloop()
