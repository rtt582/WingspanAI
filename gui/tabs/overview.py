import tkinter as tk
from tab_functions import action_cube

# '-*-lucidatypewriter-medium-r-*-*-*-140-*-*-*-*-*-*'
FONT = ('Times New Roman',10,'normal')
VP_FONT = ('Times New Roman',25,'bold')
VP = 0

def init_tab(tab):
    
    # Tab functions ==========================================================================
    def disable_newlines(event, field=None):
        if event.keysym == 'Return':
            try:
                return "break"
            finally:
                #match field: # why won't my fucking python update work 
                    #case "bird hand":
                add_bird_to_hand()
    
    def add_bird_to_hand():
        bird_name = bird_hand_input_text.get("1.0", "end-1c")  # Get the input text
        if bird_name:
            bird_hand_text.config(state="normal")
            bird_hand_text.insert("end", bird_name + ";")  # Insert the bird name in the text widget
            bird_hand_text.config(state="disabled")
            bird_hand_input_text.delete("1.0", "end")  # Clear the input text
            
    def remove_bird_from_hand():
        bird_name = bird_hand_input_text.get("1.0", "end-1c")  # Get the input text
        if bird_name:
            bird_hand_text.config(state="normal")
            content = bird_hand_text.get("1.0", "end")
            updated_content = content.replace(bird_name + ";\n", "")  # Remove bird name
            bird_hand_text.delete("1.0", "end")
            bird_hand_text.insert("1.0", updated_content)
            bird_hand_text.config(state="disabled")
            bird_hand_input_text.delete("1.0", "end")  # Clear the input text
    
    # Action cubes ===========================================================================
    action_cube_label               = tk.Label      (tab,   text="Action Cubes:",   font=FONT)
    action_cube_label.place                         (relx=0, rely=0)
    
    action_cube_decrement_button    = tk.Button     (tab,   text='-',               font=FONT)
    action_cube_decrement_button.place              (relx=0, rely=0.05)
    
    action_cube_entry               = tk.Entry      (tab,   text='',                font=FONT,  width=3)
    action_cube_entry.place                         (relx=22/600, rely=0.05)
    
    action_cube_increment_button    = tk.Button     (tab,   text='+',               font=FONT)
    action_cube_increment_button.place              (relx=54/600, rely=0.05)
    
    # Victory points ===========================================================================
    victory_point_label             = tk.Label      (tab,   text="Victory Points:" + str(VP),   font=VP_FONT)
    victory_point_label.place                       (relx=0.5, rely=0)
    
    # Bird hand ==============================================================================
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
    bird_hand_input_text.bind                       ("<KeyPress>", disable_newlines)
    
    bird_hand_add_button            = tk.Button     (tab, text='Add', command=add_bird_to_hand, font=FONT)
    bird_hand_add_button.place                      (relx=210/600, rely=0.15)
    
    bird_hand_remove_button         = tk.Button     (tab, text='Remove', command=remove_bird_from_hand, font=FONT)
    bird_hand_remove_button.place                   (relx=250/600, rely=0.15)
    
    # Bonus hand ==============================================================================
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
    
    # Food =====================================================================================
    food_label                       = tk.Label      (tab,   text="Food:",      font=FONT)
    food_label.place                                 (relx=0, rely=0.3)
    
    food_scrollbar                   = tk.Scrollbar  (tab, orient="horizontal")
    food_scrollbar.place                             (relx=530/600, rely=0.3, width=60)
    food_text                        = tk.Text       (tab,   font=FONT,              wrap='none',    bg='#DADADA',   xscrollcommand=food_scrollbar.set)
    food_scrollbar.config                            (command=bird_hand_text.xview)
    food_text.place                                  (relx=90/600, rely=0.3, height=20, width=435)
    food_text.config                                 (state='disabled')
        
    food_input_text                  = tk.Text       (tab)
    food_input_text.place                            (relx=5/600, rely=0.35, height=20, width=200)
    
    food_add_button                  = tk.Button     (tab,   text='Add',             font=FONT)
    food_add_button.place                            (relx=210/600, rely=0.35)
    
    food_remove_button               = tk.Button     (tab,   text='Remove',          font=FONT)
    food_remove_button.place                         (relx=250/600, rely=0.35)
    
    # Forest ===================================================================================
    forest_label                     = tk.Label      (tab,   text="Forest:",      font=FONT)
    forest_label.place                               (relx=0, rely=0.4)
    
    forest_scrollbar                 = tk.Scrollbar  (tab, orient="horizontal")
    forest_scrollbar.place                           (relx=530/600, rely=0.4, width=60)
    forest_text                      = tk.Text       (tab,   font=FONT,              wrap='none',    bg='#DADADA',   xscrollcommand=forest_scrollbar.set)
    forest_scrollbar.config                          (command=bird_hand_text.xview)
    forest_text.place                                (relx=90/600, rely=0.4, height=20, width=435)
    forest_text.config                               (state='disabled')
    
    forest_input_text                = tk.Text       (tab)
    forest_input_text.place                          (relx=5/600, rely=0.45, height=20, width=200)
    
    forest_add_button                = tk.Button     (tab,   text='Add',             font=FONT)
    forest_add_button.place                          (relx=210/600, rely=0.45)
    
    forest_remove_button             = tk.Button     (tab,   text='Remove',          font=FONT)
    forest_remove_button.place                       (relx=250/600, rely=0.45)
    
    # Grassland =================================================================================
    grassland_label                  = tk.Label      (tab,   text="Grassland:",      font=FONT)
    grassland_label.place                            (relx=0, rely=0.5)
    
    grassland_scrollbar              = tk.Scrollbar  (tab, orient="horizontal")
    grassland_scrollbar.place                        (relx=530/600, rely=0.5, width=60)
    grassland_text                   = tk.Text       (tab,   font=FONT,              wrap='none',    bg='#DADADA',   xscrollcommand=grassland_scrollbar.set)
    grassland_scrollbar.config                       (command=bird_hand_text.xview)
    grassland_text.place                             (relx=90/600, rely=0.5, height=20, width=435)
    grassland_text.config                            (state='disabled')
    
    grassland_input_text             = tk.Text       (tab)
    grassland_input_text.place                       (relx=5/600, rely=0.55, height=20, width=200)
    
    grassland_add_button             = tk.Button     (tab,   text='Add',             font=FONT)
    grassland_add_button.place                       (relx=210/600, rely=0.55)
    
    grassland_remove_button          = tk.Button     (tab,   text='Remove',          font=FONT)
    grassland_remove_button.place                    (relx=250/600, rely=0.55)
    
    # Wetland ==================================================================================
    wetland_label                    = tk.Label      (tab,   text="Wetland:",      font=FONT)
    wetland_label.place                              (relx=0, rely=0.6)
    
    wetland_scrollbar                = tk.Scrollbar  (tab, orient="horizontal")
    wetland_scrollbar.place                          (relx=530/600, rely=0.6, width=60)
    wetland_text                     = tk.Text       (tab,   font=FONT,              wrap='none',    bg='#DADADA',   xscrollcommand=wetland_scrollbar.set)
    wetland_scrollbar.config                         (command=bird_hand_text.xview)
    wetland_text.place                               (relx=90/600, rely=0.6, height=20, width=435)
    wetland_text.config                              (state='disabled')
    
    wetland_input_text               = tk.Text       (tab)
    wetland_input_text.place                         (relx=5/600, rely=0.65, height=20, width=200)
    
    wetland_add_button               = tk.Button     (tab,   text='Add',             font=FONT)
    wetland_add_button.place                         (relx=210/600, rely=0.65)
    
    wetland_remove_button            = tk.Button     (tab,   text='Remove',          font=FONT)
    wetland_remove_button.place                      (relx=250/600, rely=0.65)
    
    # Goal tiles ===============================================================================
    goal_tiles_label                 = tk.Label      (tab,   text="Goal Tiles:",      font=FONT)
    goal_tiles_label.place                           (relx=0, rely=0.7)
    
    goal_tiles_scrollbar             = tk.Scrollbar  (tab, orient="horizontal")
    goal_tiles_scrollbar.place                       (relx=530/600, rely=0.7, width=60)
    goal_tiles_text                  = tk.Text       (tab,   font=FONT,              wrap='none',    bg='#DADADA',   xscrollcommand=goal_tiles_scrollbar.set)
    goal_tiles_scrollbar.config                      (command=bird_hand_text.xview)
    goal_tiles_text.place                            (relx=90/600, rely=0.7, height=20, width=435)
    goal_tiles_text.config                           (state='disabled')
    
    goal_tiles_input_text            = tk.Text       (tab)
    goal_tiles_input_text.place                      (relx=5/600, rely=0.75, height=20, width=200)
    
    goal_tiles_add_button            = tk.Button     (tab,   text='Add',             font=FONT)
    goal_tiles_add_button.place                      (relx=210/600, rely=0.75)
    
    goal_tiles_remove_button         = tk.Button     (tab,   text='Remove',          font=FONT)
    goal_tiles_remove_button.place                   (relx=250/600, rely=0.75)
    
    # Birdfeeder ===============================================================================
    birdfeeder_label                 = tk.Label      (tab,   text="Birdfeeder:",      font=FONT)
    birdfeeder_label.place                           (relx=0, rely=0.8)
    
    birdfeeder_scrollbar             = tk.Scrollbar  (tab, orient="horizontal")
    birdfeeder_scrollbar.place                       (relx=530/600, rely=0.8, width=60)
    birdfeeder_text                  = tk.Text       (tab,   font=FONT,              wrap='none',    bg='#DADADA',   xscrollcommand=birdfeeder_scrollbar.set)
    birdfeeder_scrollbar.config                      (command=bird_hand_text.xview)
    birdfeeder_text.place                            (relx=90/600, rely=0.8, height=20, width=435)
    birdfeeder_text.config                           (state='disabled')
    
    birdfeeder_input_text            = tk.Text       (tab)
    birdfeeder_input_text.place                      (relx=5/600, rely=0.85, height=20, width=200)
    
    birdfeeder_add_button            = tk.Button     (tab,   text='Add',             font=FONT)
    birdfeeder_add_button.place                      (relx=210/600, rely=0.85)
    
    birdfeeder_remove_button         = tk.Button     (tab,   text='Remove',          font=FONT)
    birdfeeder_remove_button.place                   (relx=250/600, rely=0.85)
    
    # Birdtray =================================================================================
    birdtray_label                   = tk.Label      (tab,   text="Birdtray:",      font=FONT)
    birdtray_label.place                             (relx=0, rely=0.9)
    
    birdtray_scrollbar               = tk.Scrollbar  (tab, orient="horizontal")
    birdtray_scrollbar.place                         (relx=530/600, rely=0.9, width=60)
    birdtray_text                    = tk.Text       (tab,   font=FONT,              wrap='none',    bg='#DADADA',   xscrollcommand=birdtray_scrollbar.set)
    birdtray_scrollbar.config                        (command=bird_hand_text.xview)
    birdtray_text.place                              (relx=90/600, rely=0.9, height=20, width=435)
    birdtray_text.config                             (state='disabled')
    
    birdtray_input_text              = tk.Text       (tab)
    birdtray_input_text.place                        (relx=5/600, rely=0.95, height=20, width=200)
    
    birdtray_add_button              = tk.Button     (tab,   text='Add',             font=FONT)
    birdtray_add_button.place                        (relx=210/600, rely=0.95)
    
    birdtray_remove_button           = tk.Button     (tab,   text='Remove',          font=FONT)
    birdtray_remove_button.place                     (relx=250/600, rely=0.95)