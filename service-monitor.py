import smtplib
import requests

SERVICES = {
    "Google": "https://www.google.com",
    "GitHub": "https://www.github.com"
}

def check_services():
    results = {}
    for name, url in SERVICES.items():
        try:
            response = requests.get(url, timeout=5)
            results[name] = response.status_code == 200
        except requests.exceptions.RequestException:
            results[name] = False
    return results

def send_email_alert(service_name):
    server = smtplib.SMTP("smtp.domain.com", 587)
    server.starttls()
    server.login("you@domain.com", "password")
    message = f"Subject: Service Down Alert\n\nThe service {service_name} is down!"
    server.sendmail("you@domain.com", "recipient@domain.com", message)
    server.quit()

if __name__ == "__main__":
    statuses = check_services()
    for service, is_up in statuses.items():
        if not is_up:
            send_email_alert(service)
