# Using the Amazon Linux image
FROM amazonlinux:2023

# Run updates and install basic diagnostic tools
RUN dnf update -y && dnf install -y shadow-utils tar gzip

# Create a Windows-style environment for a list of users
RUN for user in mark karma lily erik ned; do \
        useradd -m -s /bin/bash "$user" && \
        mkdir -p /home/"$user"/Desktop /home/"$user"/Downloads /home/"$user"/Documents /home/"$user"/Pictures /home/"$user"/Videos && \
        chown -R "$user":"$user" /home/"$user"; \
    done

# Login as the user
USER root

# Method to keep the container alive, infinite loop to prevent Fargate from exiting
CMD ["tail", "-f", "/dev/null"]