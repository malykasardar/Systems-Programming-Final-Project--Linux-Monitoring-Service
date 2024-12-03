import smtplib
import services as services

def send_alert_email(subject, message):
    """Send an email alert."""
    sender_email = "mikaeelmark@gmail.com"  # Replace with your email
    receiver_email = "mikaeelmark@gmail.com"
    password = "11261126qM"  # Replace with your email password

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            email_message = f"Subject: {subject}\n\n{message}"
            server.sendmail(sender_email, receiver_email, email_message)
        print(f"Alert email sent: {subject}")
    except Exception as e:
        print(f"Failed to send alert email: {e}")

def monitor_resources_once():
    """Check system resource thresholds once and send alerts if necessary."""
    # Parse the log file
    resource_data = services.track_resources()
    lines = resource_data.splitlines()

    try:
        cpu_usage = float(lines[0].split(":")[1].strip().replace("%", ""))
        memory_usage = int(lines[1].split(",")[1].strip().split()[1].replace("Mi", ""))
    except (IndexError, ValueError) as e:
        print("Error parsing resource data:", e)
        return

    # Check CPU threshold
    if cpu_usage > 1.5:
        send_alert_email("High CPU Usage Alert", f"CPU usage has exceeded 1.5%. Current usage: {cpu_usage}%")

    # Check Memory threshold
    if memory_usage > 453:
        send_alert_email("High Memory Usage Alert", f"Memory usage has exceeded 453 Mi. Current usage: {memory_usage} Mi")