import requests
import hashlib
import json
from Crypto.PublicKey import RSA
from OpenSSL import crypto

def load_rsa_public_key(pem_path):
    with open(pem_path, "r") as file:
        key = RSA.importKey(file.read())
    return key.public_key().exportKey(format='DER')

def get_certificate_info(der_key):
    sha256_hash = hashlib.sha256(der_key).hexdigest()
    url = f"https://crt.sh/?spkisha256={sha256_hash}&output=json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    return json.loads(response.content.decode('utf-8'))

def download_certificate(cert_id):
    url = f"https://crt.sh/?d={cert_id}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    return requests.get(url, headers=headers).content.decode('utf-8')

def extract_common_name(pem_cert):
    cert = crypto.load_certificate(crypto.FILETYPE_PEM, pem_cert)
    return cert.get_subject().commonName

def fetch_flag_from_cn(common_name):
    url = f"https://{common_name}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    return response.content.decode('utf-8')

if __name__ == "__main__":
    pem_path = "transparency.pem"
    der_key = load_rsa_public_key(pem_path)
    cert_info = get_certificate_info(der_key)
    
    if cert_info:
        cert_id = cert_info[0]["id"]
        pem_cert = download_certificate(cert_id)
        print("✅ El certificado es:", pem_cert)
        
        cn = extract_common_name(pem_cert)
        print("✅ El subdominio del certificado es:", cn)
        
        flag = fetch_flag_from_cn(cn)
        print("🏁 Bandera:", flag)
    else:
        print("❌ No se encontró información del certificado.")
