# Use the specified base image
# Replace with your container address after FROM

FROM public.ecr.aws/g7a8t7v6/inference-container:49ef...

# Expose port 1337 on the container to the host is standard for the Edge Impulse Docker container, we will change this to 80
EXPOSE 80

# Start the inference server when the container launches
# Set your API key in the second position in the command below
CMD ["--api-key", "ei_82ab4...", "--run-http-server", "80"]
