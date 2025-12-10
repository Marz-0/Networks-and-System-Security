import hashlib

# Change this path if your Procmon.exe is somewhere else
sample = r"C:\Users\Marzhan\Downloads\ProcessMonitor\Procmon.exe"

def compute_hash(path, algorithm):
    h = hashlib.new(algorithm)
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()

print("=== HASHES ===")
print("MD5:   ", compute_hash(sample, "md5"))
print("SHA1:  ", compute_hash(sample, "sha1"))
print("SHA256:", compute_hash(sample, "sha256"))
