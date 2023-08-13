def add_action_cube(tab, var):
    print('in the function')
    tab.setvar(name="action cubes", value=var.get()+1)
    print(tab.getvar(name="action cubes"))
    