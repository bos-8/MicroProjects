import tkinter as tk
import tkinter.ttk as ttk

def stylename_elements_options(stylename):
    '''Function to expose the options of every element associated to a widget
       stylename.'''
    try:
        # Get widget elements
        style = ttk.Style()
        layout = str(style.layout(stylename))
        print('Stylename = {}'.format(stylename))
        print('Layout    = {}'.format(layout))
        elements=[]
        for n, x in enumerate(layout):
            if x=='(':
                element=""
                for y in layout[n+2:]:
                    if y != ',':
                        element=element+str(y)
                    else:
                        elements.append(element[:-1])
                        break
        print('\nElement(s) = {}\n'.format(elements))

        # Get options of widget elements
        for element in elements:
            print('{0:30} options: {1}'.format(
                element, style.element_options(element)))

    except tk.TclError:
        print('_tkinter.TclError: "{0}" in function'
              'widget_elements_options({0}) is not a regonised stylename.'
              .format(stylename))


    # root = tk.Tk()

    # # Dictionary mapping widget names to their respective tk classes
    # widget_classes = {
    #     'Button': tk.Button,
    #     'Label': tk.Label,
    #     'Checkbutton': tk.Checkbutton,
    #     'Radiobutton': tk.Radiobutton,
    #     'Entry': tk.Entry,
    #     'Menu': tk.Menu,
    #     'Canvas': tk.Canvas,
    #     'Frame': tk.Frame,
    #     'Scrollbar': tk.Scrollbar,
    #     'Listbox': tk.Listbox,
    #     'Scale': tk.Scale,
    #     'Spinbox': tk.Spinbox,
    #     'OptionMenu': tk.OptionMenu
    # }

    # try:
    #     widget = widget_classes[stylename](root)
    #     # Get widget options
    #     options = widget.configure()
    #     print(f'Widget class = {widget.winfo_class()}')
    #     print('\nAvailable options and their current values:')
    #     for opt, val in options.items():
    #         print(f'{opt:30} current value: {val[-1]}')

    #     # Get children (if any)
    #     children = widget.winfo_children()
    #     if children:
    #         print(f'\nChildren of the {widget}:')
    #         for child in children:
    #             print(f'- {child.winfo_class()}')
    #     else:
    #         print(f'\nNo children for the {widget} widget.')

    # except tk.TclError as e:
    #     print(f'_tkinter.TclError: {e}')

stylename_elements_options('TSpinbox')