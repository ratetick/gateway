import subprocess

recipient = "+16465268677"
message = "hello"

# Run the signal-cli command to send a message
subprocess.run(["signal-cli", "-a", "+13479036038", "send", "-m", message, recipient])
