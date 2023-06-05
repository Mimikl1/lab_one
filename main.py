import os
import shutil
import datetime

class FileService:
    def __init__(self):
        self.files = {}
        self.backup_interval = 24  # hours
        self.backup_version = 1
        self.backup_folder = "backup"
        
    def save_file(self, file_path):
        file_id = self.generate_unique_id()
        shutil.copy(file_path, file_id)
        self.files[file_id] = file_path
        return file_id
    
    def output_file(self, file_id):
        if file_id in self.files:
            return self.files[file_id]
        return None
    
    def delete_file(self, file_id):
        if file_id in self.files:
            file_path = self.files[file_id]
            del self.files[file_id]
            os.remove(file_path)
    
    def change_file_id(self, old_id, new_id):
        if old_id in self.files:
            file_path = self.files[old_id]
            del self.files[old_id]
            self.files[new_id] = file_path
    
    def get_files_by_ids(self, file_ids):
        files = []
        for file_id in file_ids:
            if file_id in self.files:
                files.append(self.files[file_id])
        return files
    
    def get_all_files(self):
        return list(self.files.values())
    
    def backup_files(self):
        if not os.path.exists(self.backup_folder):
            os.makedirs(self.backup_folder)
        
        backup_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = os.path.join(self.backup_folder, f"backup_{backup_time}")
        
        shutil.copytree(".", backup_path)
        self.backup_version += 1
        
    def recover_from_backup(self, backup_version):
        backup_path = os.path.join(self.backup_folder, f"backup_{backup_version}")
        
        if os.path.exists(backup_path):
            shutil.rmtree(".")
            shutil.copytree(backup_path, ".")
            return True
        
        return False
    
    def cancel_recovery(self, current_version):
        backup_path = os.path.join(self.backup_folder, f"backup_{current_version}")
        
        if os.path.exists(backup_path):
            shutil.rmtree(backup_path)
            return True
        
        return False
    
    def generate_unique_id(self):
        return str(datetime.datetime.now().timestamp())




file_service = FileService()

# Save a file
file_id = file_service.save_file("/home/student/Desktop/lab_one/file.txt")
print("File saved with ID:", file_id)

# Output a file
output_path = file_service.output_file(file_id)
if output_path:
    print("File output path:", output_path)
else:
    print("File not found.")

# Delete a file
def delete_file():
    file_service.delete_file(file_id)
    print("File deleted.")

# Change file ID
def change_file_id():
    new_id = file_service.generate_unique_id()
    file_service.change_file_id(file_id, new_id)
    print("File ID changed from", file_id, "to", new_id)

# Get files by IDs
# Get files by IDs
def get_files_id():
    file_ids = ["id1", "id2", "id3"]
    files = file_service.get_files_by_ids(file_ids)
    print("Files:", files)

# Get all files
def get_all_files():
    all_files = file_service.get_all_files()
    print("All files:", all_files)

# Backup files
def backup_files():
    file_service.backup_files()
    print("Files backed up.")

# Recover from backup
def recover_backup():
    backup_version = 1
    recovery_successful = file_service.recover_from_backup(backup_version)
    if recovery_successful:
        print("Recovery successful.")
    else:
        print("Backup version not found.")

# Cancel recovery
def cancel_recovery():
    current_version = file_service.backup_version - 1  # assuming backup just occurred
    cancel_successful = file_service.cancel_recovery(current_version)
    if cancel_successful:
        print("Recovery cancelled.")
    else:
        print("Backup version not found.")

