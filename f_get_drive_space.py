import shutil

def get_drive_space(drive_letter):
    total, used, free = shutil.disk_usage(drive_letter)

        # Convert bytes to gigabytes for readability
    total_gb = total / (1024 ** 3)
    used_gb = used / (1024 ** 3)
    free_gb = free / (1024 ** 3)
    return total_gb, used_gb, free_gb
