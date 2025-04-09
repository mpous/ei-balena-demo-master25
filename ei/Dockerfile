# Use the specified base image
# Replace with your container address after FROM

#FROM public.ecr.aws/g7a8t7v6/inference-container:49ef46c7e9f063a4aabb5a680c74cc7d60c9d8f7
FROM public.ecr.aws/g7a8t7v6/inference-container:87049ffdac97814578a8eb90610fb89620f843bd

# Expose port 1337 on the container to the host is standard for the Edge Impulse Docker container, we will change this to 80
EXPOSE 1337

# Start the inference server when the container launches
# Set your API key in the second position in the command below
CMD ["--api-key", "ei_1b9cfec1eb4ea2ff602abf11e592678347d82cd051f05ba2", "--run-http-server", "1337", "--impulse-id", "1", "--force-variant", "int8"]

