from exercicio3 import validate_email


def generate_valid_email_list(email_list: list):
    valid_emails = []

    for email in email_list:
        try:
            valid_emails.append(email if validate_email(email) else None)
        except ValueError:
            pass

    return valid_emails
