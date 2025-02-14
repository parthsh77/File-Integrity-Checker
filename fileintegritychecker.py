import hashlib
import os

banner = """
    .                                                .
   c;l,.                                          .,l;:
    x;c.                                          .c;x
   c'll                                            lo,c
  ;'ol,'                                          ',oo,,
  lc.';l                                          l:..cl
 ,'l  o';                                        :.l  o;.
 c.l .ooO,                                      :kdl. o':
 0:k.  l'c       .,'''''''''..'''''''',,.       c'c  .Oc0
 c.:    lc.   :,'                        ',:   .:o    c'c
 :.l    ;'l   ,,,.                      .,,,   l,,    l,,
 .;l     ll.      .,':;''''','''''':;',.      .cl     oc
  lc.     .          ,.     ;.     ,.          .     .cl
  l.c                ,.     ;.     ,.                l.:
   lo                ..     ;.     ..                ll
    .         ⢀⣴⣾⣿⣿⣿⡶⢦⣄⠀⠀⠀⠀ ;.⠀⠀⠀⠀⢀⣠⠴⢾⣿⣿⣿⣷⣦⡀⠀⠀ ⠀    .
        ⠀⠀   ⣰⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⠀⠀⠀ ;.⠀⠀⠀⠀⣡⣴⣾⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀
        ⠀⠀   ⠉⠀⠀⠀⠀⠈⠙⠻⣿⣿⣿⣷⡄⠀ ;.  ⠀⣰⣿⣿⣿⡿⠛⠉⠁⠀⠀⠀⠈⠉⠀⠀
        ⠀⠀ ⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣯⠁⠀⠀;. ⠀⢈⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀ ⠀⠀  ⢀⡴⢖⣛⣧⣴⣶⣤⣄⠹⡆⡀ ;. ⠀⡼⢃⣤⣴⣶⣧⣽⣛⡲⣤⠀⠀⠀⠀⠀
        ⠀   ⢱⣄⣴⣟⠾⣿⣿⣿⣿⣿⣿⣿⡇⠀⡇⠀⠀⠀⡇⠀⣿⣿⣿⣿⣿⣿⣿⣿⣞⣷⣄⣴⠃⠀
           ⢠⠟⠉⠉⠉⠛⠓⠿⠏⠸⠟⠛⠉⠀⢠⡇⠀⠀⠀⣿⠀⠀⠉⠛⠻⠇⠿⠟⠛⠋⠉⠉⠙⠻⡀
        ⠀   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡇⠀⠀⠀⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⢿⡇⠀⠀⠀⢿⠿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀   ⡄⠀⠀⠀⠀⠀⠀⠀⣀⣤⢴⠏⠀⣸⠁⠀⠀⠀⢸⡆⠈⢳⡀⣤⡀⠀⠀⠀⠀⠀⠀⠀⡄⠀
        ⠀   ⢹⣶⢤⣤⡤⠴⠶⠛⠉⠀⠸⠀⣄⢻⣄⠀⠀⢀⣸⢃⣀⠰⠃⠈⠙⠓⠶⠤⣤⣤⢤⣾⠃⠀
        ⠀   ⠈⢿⣆⠻⣿⣄⠀⠀⠀⠀⠀⠀⠉⣱⣬⣍⣉⣯⣥⡉⠁⠀⠀⠀⠀⠀⠀⣴⣿⢃⣾⡏⠀⠀
        ⠀⠀   ⠈⢿⣆⠹⣿⣧⣀⣀⣀⣀⣤⣴⣿⣿⠟⠙⢿⣿⣿⣦⣄⣀⣀⣀⣠⣾⡿⠁⣼⠟⠀⠀⠀
        ⠀⠀⠀   ⠈⢿⣦⡈⠻⠿⠿⠿⠿⢿⣿⣿⣋⣀⣀⣀⣻⣿⣿⠿⠿⠿⠿⠿⠛⣠⣾⠏⠀⠀⠀⠀
        ⠀⠀⠀⠀    ⠻⣎⠓⢤⣀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⣀⠴⢊⡿⠋⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀    ⠘⢧⠀⠀⠀⠀⠀⠀⠀⢤⣄⣀⣠⡄⠀⠀⠀⠀⠀⠀⢠⠞⠁⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀     ⠱⣄⠀⠀⠀⠀⠀ ⣿⣿⡏⠀⠀⠀⠀⠀⠀⡠⠃⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀  ⠀⠈⠀⠀⠀⠀⠀⠀  ⣿⣿⣷⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀     ⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀ ⠀    ⠀⠀⠀⠀⠀⠀⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀ ⠀⠀    ⠀⠀⠀⠀⠀⢻⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

        ██████╗  █████╗ ██████╗ ████████╗██╗  ██╗
        ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██║  ██║
        ██████╔╝███████║██████╔╝   ██║   ███████║
        ██╔═══╝ ██╔══██║██╔══██╗   ██║   ██╔══██║
        ██║     ██║  ██║██║  ██║   ██║   ██║  ██║
        ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝
                                         
"""
# Pipe the banner output to lolcat for colorized text
result = os.system(f'echo "{banner}" | lolcat')
print(result)



def calculate_file_hash(file_path, algorithm='sha256'):
    """Calculate the hash of a file using the specified algorithm."""
    hash_func = hashlib.new(algorithm)
    try:
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

def save_hash_to_file(file_path, hash_value):
    """Save the hash value to a file."""
    hash_file = file_path + '.hash'
    try:
        with open(hash_file, 'w') as f:
            f.write(hash_value)
        print(f"Hash saved to '{hash_file}'.")
    except IOError:
        print(f"Error: Unable to save hash to '{hash_file}'.")

def load_hash_from_file(file_path):
    """Load the hash value from a file."""
    hash_file = file_path + '.hash'
    try:
        with open(hash_file, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        print(f"Error: Hash file '{hash_file}' not found.")
        return None

def check_file_integrity(file_path):
    """Check the integrity of a file by comparing its current hash with the stored hash."""
    stored_hash = load_hash_from_file(file_path)
    if not stored_hash:
        print("No stored hash found. Please generate a hash first.")
        return

    current_hash = calculate_file_hash(file_path)
    if not current_hash:
        return

    if current_hash == stored_hash:
        print("File integrity verified. The file has not been manipulated.")
    else:
        print("Warning: File integrity check failed! The file has been manipulated.")

def main():
    print("File Integrity Checker")
    print("1. Generate and save file hash")
    print("2. Check file integrity")
    choice = input("Enter your choice (1 or 2): ")

    file_path = input("Enter the file path: ")

    if choice == '1':
        hash_value = calculate_file_hash(file_path)
        if hash_value:
            save_hash_to_file(file_path, hash_value)
    elif choice == '2':
        check_file_integrity(file_path)
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
