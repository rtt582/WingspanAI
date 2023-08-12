import tkinter as tk

FONT = ('-*-lucidatypewriter-medium-r-*-*-*-140-*-*-*-*-*-*',10,'normal')
x = 10

def init_tab(tab):
    
    # Action cubes
    action_cube_label               = tk.Label      (tab,   text="Action Cubes:",   font=FONT)
    action_cube_label.place                         (relx=0, rely=0)
    
    action_cube_decrement_button    = tk.Button     (tab,   text='-',               font=FONT)
    action_cube_decrement_button.place              (relx=0, rely=0.05)
    
    action_cube_entry               = tk.Entry      (tab,   text='',                font=FONT,  width=3, border=0)
    action_cube_entry.place                         (relx=22/600, rely=0.05)
    
    action_cube_increment_button    = tk.Button     (tab,   text='+',               font=FONT)
    action_cube_increment_button.place              (relx=54/600, rely=0.05)
    
    # Bird hand
    bird_hand_label                 = tk.Label      (tab,   text="Bird Hand:",      font=FONT)
    bird_hand_label.place                           (relx=0, rely=0.1)
    
    bird_hand_scrollbar             = tk.Scrollbar  (tab, orient="horizontal")
    bird_hand_scrollbar.place                       (relx=530/600, rely=0.1, width=60)
    bird_hand_text                  = tk.Text       (tab,   font=FONT,              wrap='none',    bg='#DADADA',   xscrollcommand=bird_hand_scrollbar.set)
    bird_hand_scrollbar.config                      (command=bird_hand_text.xview)
    bird_hand_text.place                            (relx=90/600, rely=0.1, height=20, width=435)
    bird_hand_text.config                           (state='disabled')
    
    bird_hand_input_text            = tk.Text       (tab)
    bird_hand_input_text.place                      (relx=5/600, rely=0.15, height=20, width=200)
    
    bird_hand_add_button            = tk.Button     (tab,   text='Add',             font=FONT)
    bird_hand_add_button.place                      (relx=210/600, rely=0.15)
    
    bird_hand_remove_button         = tk.Button     (tab,   text='Remove',          font=FONT)
    bird_hand_remove_button.place                   (relx=250/600, rely=0.15)
    
    # Bonus hand
    bonus_hand_label                 = tk.Label      (tab,   text="Bonus Hand:",      font=FONT)
    bonus_hand_label.place                           (relx=0, rely=0.2)
    
    bonus_hand_scrollbar             = tk.Scrollbar  (tab, orient="horizontal")
    bonus_hand_scrollbar.place                       (relx=530/600, rely=0.2, width=60)
    bonus_hand_text                  = tk.Text       (tab,   font=FONT,              wrap='none',    bg='#DADADA',   xscrollcommand=bonus_hand_scrollbar.set)
    bonus_hand_scrollbar.config                      (command=bird_hand_text.xview)
    bonus_hand_text.place                            (relx=90/600, rely=0.2, height=20, width=435)
    bonus_hand_text.config                           (state='disabled')
    
    bonus_hand_input_text            = tk.Text       (tab)
    bonus_hand_input_text.place                      (relx=5/600, rely=0.25, height=20, width=200)
    
    bonus_hand_add_button            = tk.Button     (tab,   text='Add',             font=FONT)
    bonus_hand_add_button.place                      (relx=210/600, rely=0.25)
    
    bonus_hand_remove_button         = tk.Button     (tab,   text='Remove',          font=FONT)
    bonus_hand_remove_button.place                   (relx=250/600, rely=0.25)
    
    tk.Label(tab, text="Food:", font=('-*-lucidatypewriter-medium-r-*-*-*-140-*-*-*-*-*-*',10,'normal')).place(relx=0, rely=0.3)
    tk.Label(tab, text="Forest:", font=('-*-lucidatypewriter-medium-r-*-*-*-140-*-*-*-*-*-*',10,'normal')).place(relx=0, rely=0.4)
    tk.Label(tab, text="Grassland:", font=('-*-lucidatypewriter-medium-r-*-*-*-140-*-*-*-*-*-*',10,'normal')).place(relx=0, rely=0.5)
    tk.Label(tab, text="Wetland:", font=('-*-lucidatypewriter-medium-r-*-*-*-140-*-*-*-*-*-*',10,'normal')).place(relx=0, rely=0.6)
    tk.Label(tab, text="Goal Tiles:", font=('-*-lucidatypewriter-medium-r-*-*-*-140-*-*-*-*-*-*',10,'normal')).place(relx=0, rely=0.7)
    tk.Label(tab, text="Birdfeeder:", font=('-*-lucidatypewriter-medium-r-*-*-*-140-*-*-*-*-*-*',10,'normal')).place(relx=0, rely=0.8)
    tk.Label(tab, text="Bird Tray:", font=('-*-lucidatypewriter-medium-r-*-*-*-140-*-*-*-*-*-*',10,'normal')).place(relx=0, rely=0.9)
