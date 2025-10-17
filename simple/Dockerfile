# Start from a small Python base image
FROM python:3.11-slim


# Set a working directory
WORKDIR /appy


# Install build deps and cleanup to keep image small
RUN apt-get update \
&& apt-get install -y --no-install-recommends gcc libpq-dev ca-certificates \
&& rm -rf /var/lib/apt/lists/*


# Copy requirements and install
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


# Copy application code
COPY . /appy


# Expose the port gunicorn will run on
EXPOSE 5000


# Use a non-root user for safety (optional)
RUN useradd --create-home appuser || true
USER appuser


# Run gunicorn with 2 workers — production entrypoint
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "appy:appy", "--workers", "2"]