# Edge Impulse / balena demo
[Edge Impulse](https://edgeimpulse.com/) impulses can be [deployed](https://docs.edgeimpulse.com/docs/run-inference/docker) as Docker containers. The [balena platform](https://www.balena.io/) makes deploying containers to one or 100,000+ edge devices a breeze, so this demo shows how they can work beautifully together.

## What you'll need

This demo is intended for the Raspberry Pi 4 - any version of that board should work. You should plug a standard USB webcam into one of the USB ports of your Pi.

You'll also need a free or paid Edge Impulse account and an impulse that does image detection (sample public impulses for this are available that you can clone)

Finally, a free or paid balenaCloud account which you can sign up for [here](https://dashboard.balena-cloud.com/signup).

## Getting started

Create a new fleet in your balena account and deploy a Pi 4 device. (See our [Getting Started Guide](https://docs.balena.io/learn/getting-started/raspberrypi3/python/) for more information!)

Clone this repository to your development machine and also install the [balena CLI](https://github.com/balena-io/balena-cli/blob/master/INSTALL.md)

Clone or create an impulse in Edge Impulse that uses image recognition.

On the Edge Impulse "Deployment" screen, enter "Docker" for the "Search deployment options." You'll see instructions for how to run your model as a Docker container. Note the "Container" and "Arguments" which you'll need to add to the Dockerfile in the ei folder of this cloned repo.

Copy the "Container" value to replace the partial example value after the `FROM` in line one of the Dockerfile.

Copy the API key (just the part that begins with `ei_`) to the second string in the `CMD` command in the last line of the Dockerfile.

Deploy the updated code to your balena device(s) [by issuing](https://docs.balena.io/learn/deploy/deployment/) `balena push` in the balena CLI. 

After the balena builder builds and packages the code, the containers will be pushed to your device(s) and the inferencing engine in the Edge Impulse container should begin to run. The "cam" service will start executing a Python script that submits an image from the webcam every 4 seconds to the local Edge Impulse inference container, with the results printed to your terminal.

## How it works

Your model (impulse) is automatically downloaded and run by the Edge Impulse container. It exposes an API which the "cam" service uses to get repeated inferences from the images captured by the webcam. Note the "cam" service has no Edge Impulse-specific code. It uses OpenCV and the Requests module to obtain inferences from the "ei" container.

Use the device variable `SLEEP_TIME` to set the wait period in seconds between capture events. (Default value is 4.)

The Edge Impulse model UI is available on port 80 of your device.

An Express webserver provides a page on port 8080 where you can view the current photo and the annotated version of the photo, with bounding boxes drawn where the EI model detects class item(s). This page is set to auto refresh every five seconds.

You can add additional Dockerfiles for more running models. Use the `EI_IMG` device variable to tell the cam service which model to use. Set the value to the name of the service. (Be sure to use a different name for each service!)

## Troubleshooting

If your camera is not found it may not be on port "0" - if so you can change the `camera_port` value in the cam service Python file.

