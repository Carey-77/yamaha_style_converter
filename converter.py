import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import struct

# Class to handle Yamaha file parsing and conversion logic
class YamahaFileConverter:
    def __init__(self):
        pass

    def read_cpi_file(self, file_path):
        """ Reads and parses the binary content of a CPI file. """
        try:
            with open(file_path, 'rb') as file:
                data = file.read()
                print(f"Successfully read {len(data)} bytes from {file_path}")
                parsed_data = self.parse_cpi_data(data)
                return parsed_data
        except FileNotFoundError:
            print("File not found!")
            return None

    def parse_cpi_data(self, data):
        """ Parses the binary content of a CPI file. """
        # Example parsing of binary data - adapt as needed based on file structure
        magic_number = struct.unpack('4s', data[0:4])[0]  # First 4 bytes (example)
        file_size = struct.unpack('<I', data[4:8])[0]      # Next 4 bytes as unsigned int
        print(f"Magic Number: {magic_number}, File Size: {file_size}")
        # Further parsing logic should be implemented here.
        return data  # Returning raw data for now

    def write_ppi_file(self, parsed_data, new_file_path):
        """ Writes the parsed data into a new PPI file. """
        try:
            with open(new_file_path, 'wb') as file:
                file.write(parsed_data)
                print(f"Successfully wrote the file as {new_file_path}")
        except Exception as e:
            print(f"Failed to write PPI file: {e}")

    def convert_cpi_to_ppi(self, cpi_file_path, new_file_name=None):
        """ Converts a CPI file to a PPI file, with an optional new file name. """
        parsed_data = self.read_cpi_file(cpi_file_path)
        if parsed_data:
            new_file_path = new_file_name if new_file_name else cpi_file_path.replace('.cpi', '.ppi')
            self.write_ppi_file(parsed_data, new_file_path)

    def read_cpf_file(self, file_path):
        """ Reads and parses the binary content of a CPF file. """
        try:
            with open(file_path, 'rb') as file:
                data = file.read()
                print(f"Successfully read {len(data)} bytes from {file_path}")
                parsed_data = self.parse_cpf_data(data)
                return parsed_data
        except FileNotFoundError:
            print("File not found!")
            return None

    def parse_cpf_data(self, data):
        """ Parses the binary content of a CPF file. """
        # Implement the parsing logic for CPF files here
        return data  # Returning raw data for now

    def write_ppf_file(self, parsed_data, new_file_path):
        """ Writes the parsed data into a new PPF file. """
        try:
            with open(new_file_path, 'wb') as file:
                file.write(parsed_data)
                print(f"Successfully wrote the file as {new_file_path}")
        except Exception as e:
            print(f"Failed to write PPF file: {e}")

    def convert_cpf_to_ppf(self, cpf_file_path, new_file_name=None):
        """ Converts a CPF file to a PPF file, with an optional new file name. """
        parsed_data = self.read_cpf_file(cpf_file_path)
        if parsed_data:
            new_file_path = new_file_name if new_file_name else cpf_file_path.replace('.cpf', '.ppf')
            self.write_ppf_file(parsed_data, new_file_path)


# Class for the GUI interface
class YamahaStyleConverterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Yamaha Style Converter")
        self.root.geometry("400x200")
        self.converter = YamahaFileConverter()

        # Minimal and modern ttk styles
        style = ttk.Style()
        style.theme_use('clam')

        # Label for instructions
        self.label = ttk.Label(root, text="Select a Yamaha style file", font=("Arial", 12))
        self.label.pack(pady=10)

        # Button to select a file
        self.select_file_button = ttk.Button(root, text="Select Style File", command=self.open_file_dialog)
        self.select_file_button.pack(pady=10)

        # Label to show the selected file path
        self.file_label = ttk.Label(root, text="No file selected", font=("Arial", 10))
        self.file_label.pack(pady=5)

        # Entry for renaming the output file
        self.rename_label = ttk.Label(root, text="New File Name (optional):")
        self.rename_label.pack(pady=5)
        self.new_file_name = ttk.Entry(root)
        self.new_file_name.pack(pady=5)

        # Buttons for conversion
        self.convert_ppi_button = ttk.Button(root, text="Convert to PPI", state=tk.DISABLED, command=self.convert_to_ppi)
        self.convert_ppi_button.pack(pady=5)

        self.convert_ppf_button = ttk.Button(root, text="Convert to PPF", state=tk.DISABLED, command=self.convert_to_ppf)
        self.convert_ppf_button.pack(pady=5)

    def open_file_dialog(self):
        file_types = [("Yamaha Styles", "*.cpi *.cpf"), ("All files", "*.*")]
        file_path = filedialog.askopenfilename(filetypes=file_types)
        
        if file_path:
            self.file_label.config(text=file_path)
            self.file_extension = os.path.splitext(file_path)[1].lower()

            # Enable the appropriate conversion button based on file extension
            if self.file_extension == '.cpi':
                self.convert_ppi_button.config(state=tk.NORMAL)
                self.convert_ppf_button.config(state=tk.DISABLED)
            elif self.file_extension == '.cpf':
                self.convert_ppi_button.config(state=tk.DISABLED)
                self.convert_ppf_button.config(state=tk.NORMAL)
            else:
                messagebox.showerror("Invalid File", "Please select a valid Yamaha style file (.cpi, .cpf)")

    def convert_to_ppi(self):
        file_path = self.file_label.cget("text")
        if file_path.endswith(".cpi"):
            new_file_name = self.new_file_name.get()
            new_file_name = new_file_name if new_file_name else None
            self.converter.convert_cpi_to_ppi(file_path, new_file_name)
            messagebox.showinfo("Success", f"File successfully converted to PPI!")

    def convert_to_ppf(self):
        file_path = self.file_label.cget("text")
        if file_path.endswith(".cpf"):
            new_file_name = self.new_file_name.get()
            new_file_name = new_file_name if new_file_name else None
            self.converter.convert_cpf_to_ppf(file_path, new_file_name)
            messagebox.showinfo("Success", f"File successfully converted to PPF!")


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = YamahaStyleConverterGUI(root)
    root.mainloop()
