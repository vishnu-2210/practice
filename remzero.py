def parse_encoded_string(encoded):
    parts = encoded.split('0')
    
    clean_parts = []
    for part in parts:
        if part != "": 
            clean_parts.append(part)

    return {
        "first_name": clean_parts[0],
        "last_name": clean_parts[1],
        "id": clean_parts[2]
    }

print(parse_encoded_string("Robert000Smith000123"))