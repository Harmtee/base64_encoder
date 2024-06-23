import base64
import hashlib
import json
import random
import string

def encode_payload(payload):
    """Encode the payload with salt key and index."""
    if not isinstance(payload, str):
        payload = json.dumps(payload)
        salt_key = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        salt_index = random.randint(0, len(payload) - 1)
        
    if not 0 <= salt_index < len(payload):
        raise ValueError("Salt index is out of range of the payload length.")

    salt_hash = hashlib.sha256(salt_key.encode()).hexdigest()
 
    salted_payload = payload[:salt_index] + salt_hash + payload[salt_index:]
    
    encoded = base64.urlsafe_b64encode(salted_payload.encode()).decode()
    return encoded, salt_key, salt_index

def decode_payload(encoded_payload, salt_key, salt_index):
    """Decode the payload with salt key and index."""

    salt_hash = hashlib.sha256(salt_key.encode()).hexdigest()
    
    # Decode from Base64
    decoded_bytes = base64.urlsafe_b64decode(encoded_payload)
    decoded = decoded_bytes.decode()
    
    # Verify the salt position
    if decoded[salt_index:salt_index+len(salt_hash)] == salt_hash:
        # Extract the original payload
        original_payload = decoded[:salt_index] + decoded[salt_index+len(salt_hash):]
        try:
            original_payload = json.loads(original_payload)
        except ValueError:
            pass
        return original_payload
    else:
        raise ValueError("Invalid salt key or salt index.")
