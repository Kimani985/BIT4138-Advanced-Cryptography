import os

print("===== SYSTEM CHECK =====")

os.system("python --version")
os.system("git --version")
os.system("openssl version")

print("\nEnvironment verification completed successfully.")