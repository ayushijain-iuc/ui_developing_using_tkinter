# **Management System GUI**

This is a Python-based graphical user interface (GUI) application designed for system management tasks. The application is built using the **Tkinter** library and incorporates **PIL (Python Imaging Library)** for enhanced image handling and a better visual experience.

---

## **Features**

### 1. **Main Window**
- A clean, interactive GUI with a structured layout.
- Custom window icon for branding.
- Adjustable window dimensions to ensure flexibility across different screen sizes.

### 2. **Menu Bar**
- The menu bar includes several categories for efficient navigation:
  - **Routine Work**
  - **Basic Information**
  - **Account Operations**
  - **Report Job**
  - **System Settings**

Each category has associated submenus, and descriptive icons are used for easy identification.

### 3. **Panels**
- **Top Panel:**
  - Displays system features such as "Management System" and "Packaging Operations".
  - Includes icons for easy identification of features.

- **Left Panel:**
  - Lists task categories like "Basic Information" and "Account Operations".
  - Icons are displayed alongside text labels for clarity and ease of navigation.

- **Right Panel:**
  - Displays specific tasks such as "Order Management", "Sales Operations", and "Inventory Work".
  - Tasks are arranged in a responsive grid layout for quick access.

- **Footer Section:**
  - Shows company details such as "WL Bandung Liquefied Petroleum Gas Co., Ltd.".
  - Displays user information and "Customer Ordering" details with icons for easy reference.

---

## **Technologies Used**

- **Tkinter:** For creating GUI components, including buttons, labels, frames, and menus.
- **PIL (Pillow):** For loading, resizing, and displaying icons and images across the GUI.

---

## **How It Works**

### **Dynamic Layout:**
- The layout adapts to the window size using **`pack()`** and **`grid()`** geometry managers, ensuring a responsive design.

### **Image Handling:**
- Icons are loaded, resized, and displayed in a uniform size (25x25 pixels) to maintain consistency throughout the application.

### **Event Loop:**
- The application runs interactively until the user closes it, managed by Tkinter's `mainloop()`.

---

## **Installation Instructions**

1. **Clone the Repository** (if applicable):
   ```bash
   git clone <repository_url>
