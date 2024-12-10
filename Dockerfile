# Use the official Python 3.12 Alpine image
FROM python:3.12-alpine

# Install dependencies
RUN apk update \
    && apk add --no-cache gcc musl-dev postgresql-dev

# Create and set the working directory
WORKDIR /app

# Command to keep the container running
CMD ["tail", "-f", "/dev/null"]