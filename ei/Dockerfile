# Use the specified base image
# Replace with your container address after FROM
FROM public.ecr.aws/g7a8t7v6/inference-container:...

# Set the API key as an environment variable (optional, for security reasons you might want to handle this differently)
ENV API_KEY=ei_82ab...

# Expose port 1337 on the container to the host is standard for the Edge Impulse Docker container, we will change this to 80
EXPOSE 80

# Start the inference server when the container launches
# Also set your API key in the second position in the command below
CMD ["--api-key", "ei_82ab4...", "--run-http-server", "80"]
