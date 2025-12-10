import pefile

# pip install pefile
sample = r"C:\Users\Marzhan\Downloads\ProcessMonitor\Procmon.exe"

pe = pefile.PE(sample)

print("=== PE HEADER INFORMATION ===")
print("Entry Point:", hex(pe.OPTIONAL_HEADER.AddressOfEntryPoint))
print("Image Base:", hex(pe.OPTIONAL_HEADER.ImageBase))

print("\nImported DLLs and first 5 functions from each:")
for entry in pe.DIRECTORY_ENTRY_IMPORT:
    dll_name = entry.dll.decode(errors="ignore")
    print(" ", dll_name)
    for imp in entry.imports[:5]:
        func_name = imp.name.decode(errors="ignore") if imp.name else "None"
        print("   -", func_name)
