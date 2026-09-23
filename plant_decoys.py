import os

# Where decoys will be placed (we'll point this at a Docker container later)
DECOY_DIR = "./decoys_output"

def create_fake_env():
    content = """DB_PASSWORD=Pr0dDB_2024!
API_KEY=sk_live_51Hf8x9K2mN7pQ3rT
AWS_SECRET=wJalrXUtnFEMI_fake_key_example
"""
    path = os.path.join(DECOY_DIR, ".env")
    with open(path, "w") as f:
        f.write(content)
    print(f"Created decoy: {path}")

def create_fake_ssh_key():
    content = """-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
QyNTUxOQAAACAf4k9x7z2FAKE_EXAMPLE_ONLY_NOT_A_REAL_KEY_VALUE12345
-----END OPENSSH PRIVATE KEY-----
"""
    path = os.path.join(DECOY_DIR, "id_rsa")
    with open(path, "w") as f:
        f.write(content)
    print(f"Created decoy: {path}")

def create_fake_aws_creds():
    content = """[default]
aws_access_key_id = AKIAFAKEKEYEXAMPLE1
aws_secret_access_key = fakeSecretKeyExample1234567890abcdEXAMPLE
"""
    path = os.path.join(DECOY_DIR, "credentials")
    with open(path, "w") as f:
        f.write(content)
    print(f"Created decoy: {path}")

def main():
    os.makedirs(DECOY_DIR, exist_ok=True)
    create_fake_env()
    create_fake_ssh_key()
    create_fake_aws_creds()
    print("\nAll decoys planted.")

if __name__ == "__main__":
    main()