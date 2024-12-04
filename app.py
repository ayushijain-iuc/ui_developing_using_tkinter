import tkinter as tk
from PIL import Image, ImageTk  # Import PIL modules to handle .jpg and other formats
from PIL import ImageGrab
import os
import time  # To add a small delay before taking the screenshot


def create_gui():
    # Main window
    root = tk.Tk()
    root.title("System programming")
    root.geometry("1200x700")  # Adjust the size as needed
    
    # Set the favicon
    p1 = tk.PhotoImage(file=r'C:\Users\User\Desktop\task project\images\quotationjob.png')
    root.iconphoto(False, p1)
    
    # Set the favicon
    # root.iconbitmap(r"C:\Users\User\Desktop\task project\images\manament1.png")  # Update the path for your favicon

    # Dictionary to store references to PhotoImage objects
    icon_refs = {}

    # Uniform icon size
    icon_size = (25, 25)

    # Menu bar
    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)

    # Adding menu options with icons
    menu_items = [
        ("routine work", r"C:\Users\User\Desktop\task project\images\basicinformation.png"),
        ("Basic Information", r"C:\Users\User\Desktop\task project\images\basicinformation.png"),
        ("Account Operations", r"C:\Users\User\Desktop\task project\images\basicinformation.png"),
        ("Report Job", r"C:\Users\User\Desktop\task project\images\basicinformation.png"),
        ("System Settings", r"C:\Users\User\Desktop\task project\images\basicinformation.png")
    ]

    for item, icon_path in menu_items:
        # Load the icon for the menu item using PIL to handle .jpg and .png
        image = Image.open(icon_path)
        icon = ImageTk.PhotoImage(image.resize(icon_size))  # Resize image to uniform size
        icon_refs[item] = icon  # Store reference to prevent garbage collection
        
        # Create a menu for each item
        menu = tk.Menu(menu_bar, tearoff=0)
        
        # Add submenus to each menu item
        menu.add_command(label=f"{item} Submenu 1", image=icon, compound="left")
        menu.add_command(label=f"{item} Submenu 2", image=icon, compound="left")
        
        # Add the menu to the menu bar with label and icon
        menu_bar.add_cascade(label=item, menu=menu)

    # Top panel for features with icons (No background box)
    top_frame = tk.Frame(root, bg="lightblue", height=50)
    top_frame.pack(fill=tk.X)
    
    features = [
        ("management system", r"C:\Users\User\Desktop\task project\images\management system.jpg"),
        ("pacakaging operation", r"C:\Users\User\Desktop\task project\images\pacaging operations.jpg"),
        ("accounting general ledger", r"C:\Users\User\Desktop\task project\images\accounting general.jpg"),
        ("Caller ID", r"C:\Users\User\Desktop\task project\images\caller id.jpg"),
        ("Message Notification", r"C:\Users\User\Desktop\task project\images\message notifivcation.png"),
        ("User", r"C:\Users\User\Desktop\task project\images\user.png"),
        ("Manual Call", r"C:\Users\User\Desktop\task project\images\manual call.jpg")
    ]
    
    for feature, icon_path in features:
        image = Image.open(icon_path)
        icon = ImageTk.PhotoImage(image.resize(icon_size))  # Use uniform size for top panel icons
        icon_refs[feature] = icon  # Store reference
        tk.Label(top_frame, text=feature, image=icon, compound="left", bg="lightblue", padx=10).pack(side=tk.LEFT, padx=5, pady=5)
    
    # Main content area
    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    # Left panel for categories with icons (No box)
    left_frame = tk.Frame(main_frame, bg="lightyellow", width=200)
    left_frame.pack(side=tk.LEFT, fill=tk.Y)
    
    categories = [
        ("routine work", r"C:\Users\User\Desktop\task project\images\basicinformation.png"),
        ("Basic Information", r"C:\Users\User\Desktop\task project\images\basicinformation.png"),
        ("Account Operations", r"C:\Users\User\Desktop\task project\images\accountoperation.png"),
        ("Report Job", r"C:\Users\User\Desktop\task project\images\systemsettings.jpg"),
        ("System Settings", r"C:\Users\User\Desktop\task project\images\systemsettings.jpg")
    ]
# Grid layout for categories
    row = 0
    for category, icon_path in categories:
        image = Image.open(icon_path)
        icon = ImageTk.PhotoImage(image.resize(icon_size))  # Resize to uniform size
        icon_refs[category] = icon  # Store reference
        
        if category == "Report Job":
            # Add left padding for "Report Job" label
            tk.Label(left_frame, text=category, image=icon, compound="left", bg="lightyellow", padx=10).grid(row=row, column=0, sticky="w", pady=2)  # Adding padding to the left side only
        else:
            tk.Label(left_frame, text=category, image=icon, compound="left", bg="lightyellow", padx=0).grid(row=row, column=0, sticky="w", pady=2)  # No padding for other items
        
        row += 1
    
    # Right panel for task options with icons (No box)
    right_frame = tk.Frame(main_frame, bg="lightcyan")
    right_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    
    tasks = [
        ("Order Management", r"C:\Users\User\Desktop\task project\images\ordermangement.jpg"),
        ("Sales Operations", r"C:\Users\User\Desktop\task project\images\salesoperations.png"),
        ("Purchase Operation", r"C:\Users\User\Desktop\task project\images\Purchase Operation.png"),
        ("Quotation Job", r"C:\Users\User\Desktop\task project\images\quotationjob.png"),
        ("Inventory Work", r"C:\Users\User\Desktop\task project\images\Inventory Work.jpg"),
        ("Vehicle Condition Record", r"C:\Users\User\Desktop\task project\images\vehicle-condition-report-main.jpg"),
        ("Basic Daily Settings", r"C:\Users\User\Desktop\task project\images\Basic Daily Settings.jpg"),
        ("Vehicle Fueling Record", r"C:\Users\User\Desktop\task project\images\Vehicle Fueling Record.png"),
        ("Gas Abnormality Login", r"C:\Users\User\Desktop\task project\images\Gas Abnormality Login.jpg"),
        ("Flow Meter Login Job", r"C:\Users\User\Desktop\task project\images\Flow Meter Login Job.jpg"),
        ("transfer operations", r"C:\Users\User\Desktop\task project\images\transfer operations.jpg"),
        ("train management", r"C:\Users\User\Desktop\task project\images\train management.jpg"),
        ("delivery management", r"C:\Users\User\Desktop\task project\images\delivery management.jpg"),
        ("invoice insurance operation", r"C:\Users\User\Desktop\task project\images\invoice insurance operation.jpg"),
        ("peer cylinder login", r"C:\Users\User\Desktop\task project\images\peercylinerlogin.jpg"),
        ("abnormal cylinder handling", r"C:\Users\User\Desktop\task project\images\abnormal cylinder handling.jpg"),
        ("retreat login operation", r"C:\Users\User\Desktop\task project\images\retreat login.jpg")
    ]
    
    # Using grid to arrange task labels with 10 items per column
    row = 0
    col = 0
    for task, icon_path in tasks:
        image = Image.open(icon_path)
        icon = ImageTk.PhotoImage(image.resize(icon_size))  # Ensure all icons are the same size
        icon_refs[task] = icon  # Store reference
        task_label = tk.Label(right_frame, text=task, image=icon, compound="left", anchor="w", bg="lightcyan", padx=5)
        task_label.grid(row=row, column=col, sticky="w", padx=10, pady=5)
        
        # Move to the next row in the same column
        row += 1
        
        # After 10 items, move to the next column and reset row to 0
        if row >= 14:  # If there are 10 labels in a column, start a new column
            row = 0
            col += 1
            
            
            
            

    # Footer with company info and table inside a single border
    footer_frame = tk.Frame(root, bg="lightgray", height=200)
    footer_frame.pack(side=tk.BOTTOM, fill=tk.X)

    # Create a container for the table content with a single border around the entire table
    footer_table = tk.Frame(footer_frame, bg="lightgray", relief="solid", bd=1)
    footer_table.pack(padx=20, pady=5, fill=tk.X)

    # Table content (rows of data)
    table_data = [
        ("Company:WL Bandung Liquefied Petroleum Gas Co., Ltd. - automatic ordering", " ", " "),
    ]

    # Configure columns to allow dynamic sizing
    for col_num in range(3):  # Adjusted for 3 columns
        footer_table.grid_columnconfigure(col_num, weight=1)  # Uniform column sizing

    # Displaying the table rows
    for row_num, row_data in enumerate(table_data):
        for col_num, data in enumerate(row_data):
            button = tk.Button(
                footer_table,
                text=data,
                bg="lightgray",
                font=("Arial", 10),
                relief="solid",
                bd=1,
            )
            button.grid(row=row_num, column=col_num, sticky="nsew", ipadx=50, ipady=5)  # Increased `ipadx` for better fit

    # Second row (User and customer ordering section)
    bottom_frame = tk.Frame(footer_frame, bg="lightgray")
    bottom_frame.pack(fill=tk.X, padx=20, pady=5)

    # "User: Admin" label
    user_label = tk.Label(bottom_frame, text="User: Admin", bg="lightgray", font=("Arial", 10))
    user_label.pack(side=tk.LEFT, padx=10)

    # Icon for Customer ordering
    icon = Image.open(r"C:\Users\User\Desktop\task project\images\custom ordering.jpg")
    icon = ImageTk.PhotoImage(icon.resize((15, 15)))
    icon_label = tk.Label(bottom_frame, image=icon, bg="lightgray")
    icon_label.image = icon  # Keep a reference to the icon
    icon_label.pack(side=tk.LEFT, padx=10)

    # "customer ordering" label
    customer_ordering_label = tk.Label(bottom_frame, text="customer ordering", bg="lightgray", font=("Arial", 10))
    customer_ordering_label.pack(side=tk.LEFT, padx=10)

    # Company info text below
    row1_label = tk.Label(
        footer_frame,
        text="Department A subpackaging department",
        bg="lightgray",
        font=("Arial", 12),
    )
    row1_label.pack(pady=5, anchor="w", padx=20)
    
    
    
    

    root.mainloop()

# Run the application
create_gui()
