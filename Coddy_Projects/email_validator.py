def clean_email_list(emails):
    # 1. Standardize: lowercase and strip whitespace
    standardized = map(lambda e: e.strip().lower(), emails)
    
    # 2. Filter: 
    # - Exactly one '@'
    # - Not starting with '@' (at least one char before)
    # - Not ending with '@' (at least one char after)
    valid_emails = filter(
        lambda e: e.count('@') == 1 and not e.startswith('@') and not e.endswith('@'), 
        standardized
    )
    
    return list(valid_emails)
