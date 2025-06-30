import re

def luhn_algorithm(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10 == 0


def get_card_issuer(card_number):
    card_number = str(card_number)
    card_pattern = {
        "Visa": r"^4\d{15}$",
        "MasterCard": r"^(5[1-5]\d{14}|2(2[2-9]\d{12}|[3-6]\d{13}|7[01]\d{12}|720\d{12}))$",
        "Elo": r"^(4011\d{12}|4312\d{12}|4389\d{12}|4514\d{12}|4576\d{12}|5041\d{12}|5066\d{12}|5067\d{12}|509\d{13}|6277\d{12}|6362\d{12}|6363\d{12}|650\d{13}|6516\d{12}|6550\d{12})$",
        "American Express": r"^3[47]\d{13}$",
        "Discover": r"^(6011\d{12}|65\d{14}|64[4-9]\d{13})$",
        "Hipercard": r"^6062\d{12}$",
        "Diners Club": r"^3(0[0-5]\d{11}|[68]\d{12})$",
        "EnRoute": r"^(2014\d{11}|2149\d{11})$",
        "JCB": r"^35(2[89]|[3-8][0-9])\d{12}$",
        "Voyager": r"^8699\d{11}$",
        "Aura": r"^(50\d{14}|56\d{14}|57\d{14}|58\d{14})$"
    }    
    for issuer, pattern in card_pattern.items():
        if re.match(pattern, card_number):
            return issuer
    return "Unknown"


def validate_credit_card(card_number):
    if luhn_algorithm(card_number):
        bandeira = get_card_issuer(card_number)
        return {"valid": True, "bandeira": bandeira}
    else:
        return {"valid": False, "bandeira": None}


# Example usage:
card_number = 5042216951795880  # Example Aura card number
result = validate_credit_card(card_number)
print(result)
