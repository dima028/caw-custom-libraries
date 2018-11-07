# ====== Packages =================================================
from ipywidgets import widgets
from IPython.display import display, Javascript


# ====================== Lock Settings Toggle ================================
# Function to return toggle button that will lock and unlock widgets from list
# and call function "ExecuteOnLock()" every time the settings are locked
# and "ExecuteOnUnlock()" everytime the settings are unlocked - 
#   it is in this function that can account for unlocking acceptions
# If there are no exceptions or explicit ExecuteOnLock or ExecuteOnUnlock,
# still define an empty function - eg:
"""
def ExecuteOnUnlock():
    return None
"""



# ExecuteOnLock is a function that can be inherrited from 
def SimpleToggleLockSettings(WidgList, ExecuteOnLock, ExecuteOnUnlock):
    # Toggle button
    button = widgets.ToggleButton(
        description = "Lock Settings", 
        button_style = 'Danger',
        disabled = False,
        value = False
    )
    
    def on_button_clicked(args):
        if args['new'] == True:
            # changing colour and description
            button.description = 'Unlock Settings'
            button.button_style = 'Success'
            # Function called to be done every time settings are locked
            ExecuteOnLock()
            # Locking Widgets:
            for widg in WidgList:
                widg.disabled = True


        else:
            # Resetting Toggle Locking
            button.description = 'Lock Settings'
            button.button_style = 'Danger'
            # Unlocking Widgets:
            for widg in WidgList:
                widg.disabled = False

            # execute the programmerdefined function; notice that it comes after the widgets being enabled, 
            # here the programmer can override that and re-disable a widget
            ExecuteOnUnlock()
            

    button.observe(on_button_clicked,'value')
    display(button)
 

# ====================== Lock Settings Toggle ================================
# Function to return toggle button that will lock and unlock widgets from list
# and call function "ExecuteOnLock()" every time the settings are locked
# and "ExecuteOnUnlock()" everytime the settings are unlocked - 
#   it is in this function that can account for unlocking acceptions
# If there are no exceptions or explicit ExecuteOnLock or ExecuteOnUnlock,
# still define an empty function - eg:
"""
def ExecuteOnUnlock():
    return None
"""


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# ExecuteOnLock is a function that can be inherrited from 
def SimpleClickProceedSettings():
    # Toggle button
    button = widgets.ToggleButton(
        description = "Proceed", 
        button_style = 'warning',
        disabled = False,
        value = False
    )
    
    def on_button_clicked(args):
        if args['new'] == True:
            # changing colour and description
            button.description = 'Unlock Settings'
            button.close()
            # Function called to be done every time settings are locked
            display(Javascript('IPython.notebook.execute_cell_range(IPython.notebook.get_selected_index()+1, IPython.notebook.get_selected_index()+2)'))
            
        else:
            # Resetting Toggle Locking
            button.description = 'Lock Settings'
            button.button_style = 'Danger'

    button.observe(on_button_clicked,'value')
    display(button)
 


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# ========== Select Files GUI =======================    
import traitlets
from tkinter import Tk, filedialog
import os

class SelectFilesButton(widgets.Button):
    """A file widget that leverages tkinter.filedialog."""

    def __init__(self, *args, **kwargs):
        """Initialize the SelectFilesButton class."""
        super(SelectFilesButton, self).__init__(*args, **kwargs)
        # Add the selected_files trait
        self.add_traits(files=traitlets.traitlets.List())
        # Create the button.
        self.description = "Select Files"
        self.icon = "square-o"
        self.style.button_color = "lightblue"
        # Set on click behavior.
        self.on_click(self.select_files)
        global FilesUploadedBool
        FilesUploadedBool = False

    @staticmethod
    def select_files(b):
        """Generate instance of tkinter.filedialog.
        Parameters
        ----------
        b : obj:
            An instance of ipywidgets.widgets.Button
        """
        # Create Tk root
        root = Tk()
        # Hide the main window
        root.withdraw()
        # Raise the root to the top of all windows.
        root.call('wm', 'attributes', '.', '-topmost', True)
        # List of selected fileswill be set to b.value
        
        #global FilesToPass

        b.files = [filedialog.askopenfilename(multiple= True)]

        if b.files[0]!= '':
            b.description = str(len(b.files[0]))+ " Files Selected"
            b.icon = "check-square-o"
            b.style.button_color = "lightgreen"
            b.files = list(b.files[0])

        return b
# ================== Select One File =============================
class SelectOneFileButton(widgets.Button):
    """A file widget that leverages tkinter.filedialog."""

    def __init__(self, *args, **kwargs):
        """Initialize the SelectFilesButton class."""
        super(SelectOneFileButton, self).__init__(*args, **kwargs)
        # Add the selected_files trait
        self.add_traits(files=traitlets.traitlets.List())
        # Create the button.
        self.description = "Select One File"
        self.icon = "square-o"
        self.style.button_color = "lightblue"
        # Set on click behavior.
        self.on_click(self.select_files)

    @staticmethod
    def select_files(b):
        """Generate instance of tkinter.filedialog.
        Parameters
        ----------
        b : obj:
            An instance of ipywidgets.widgets.Button
        """
        # Create Tk root
        root = Tk()
        # Hide the main window
        root.withdraw()
        # Raise the root to the top of all windows.
        root.call('wm', 'attributes', '.', '-topmost', True)
        # List of selected fileswill be set to b.value
        
        
        b.files = [filedialog.askopenfilename(multiple= False)]
        
        if b.files[0]!= '':
            b.description = "One File Selected"
            b.icon = "check-square-o"
            b.style.button_color = "lightgreen"

# ============== Select Folder Button ==================
class SelectFolderButton(widgets.Button):
    """A file widget that leverages tkinter.filedialog."""

    def __init__(self, *args, **kwargs):
        """Initialize the SelectFilesButton class."""
        super(SelectFolderButton, self).__init__(*args, **kwargs)
        # Add the selected_files trait
        self.add_traits(files=traitlets.traitlets.List())
        # Create the button.
        self.description = "Select Folder"
        self.icon = "square-o"
        self.style.button_color = "orange"
        # Set on click behavior.
        self.on_click(self.select_files)

    @staticmethod
    def select_files(b):
        """Generate instance of tkinter.filedialog.
        Parameters
        ----------
        b : obj:
            An instance of ipywidgets.widgets.Button
        """
        # Create Tk root
        root = Tk()
        # Hide the main window
        root.withdraw()
        # Raise the root to the top of all windows.
        root.call('wm', 'attributes', '.', '-topmost', True)
        # List of selected fileswill be set to b.value
        
        # the initial folder will be the current working directory
        b.fold = [filedialog.askdirectory(initialdir=os.getcwd())]
        
        if b.fold[0]!= '':
            b.description = "Folder Selected"
            b.icon = "check-square-o"
            b.style.button_color = "yellow"