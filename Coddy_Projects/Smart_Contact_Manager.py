def organize_contacts(contact_list):
    # 1. Helper functions
    def is_valid_email(email):
        if not isinstance(email, str):
            return False
        if " " in email:
            return False
        return "@" in email and "." in email

    def clean_and_validate_phone(phone):
        if not isinstance(phone, str):
            phone = str(phone)
        digits = "".join(ch for ch in phone if ch.isdigit())
        return digits if len(digits) == 10 else None

    # 2. Process contacts
    cleaned_contacts = []
    seen_emails = set()
    seen_phones = set()

    for contact in contact_list:
        name = contact.get("name")
        email = contact.get("email", "")
        phone = contact.get("phone", "")

        # Standardize email
        email_clean = email.lower() if isinstance(email, str) else ""

        # Validate email
        if not is_valid_email(email_clean):
            continue

        # Clean and validate phone
        phone_clean = clean_and_validate_phone(phone)
        if not phone_clean:
            continue

        # Remove duplicates by email or phone
        if email_clean in seen_emails or phone_clean in seen_phones:
            continue

        seen_emails.add(email_clean)
        seen_phones.add(phone_clean)

        cleaned_contacts.append({
            "name": name,
            "email": email_clean,
            "phone": phone_clean
        })

    # 3. Return cleaned list
    return cleaned_contacts
