# Edge Impulse / balena demo
[Edge Impulse](https://edgeimpulse.com/) impulses can be deployed as Docker containers. The [balena platform](https://www.balena.io/) makes deploying containers to one or 100,000+ edge devices a breeze, so this demo shows how they can work beautifully together.

## What you'll need

This demo is intended for the Raspberry Pi 4 - any version of that board should work.

You'll also need a free or paid Edge Impulse account and an impulse that does image detection (sample public impulses for this are available that you can clone)

Finally, a free or paid balenaCloud account which you can sign up for [here](https://dashboard.balena-cloud.com/signup).

## Getting started

Create a new fleet in your balena account and deploy a Pi 4 device. (See our [Getting Started Guide](https://docs.balena.io/learn/getting-started/raspberrypi3/python/) for more information!)

Clone this repository to your development machine and also install the [balena CLI](https://github.com/balena-io/balena-cli/blob/master/INSTALL.md)

Clone or create an impulse in Edge Impulse that uses image recognition.

On the Edge Impulse "Deployment" screen, enter "Docker" for the "Search deployment options." You'll see instructions for how to run your model as a Docker container. Note the "Container" and "Arguments" which you'll need to add to the Dockerfile in the ei folder of this cloned repo.

Copy the "Container" value to replace the partial example value after the `FROM` in line one of the Dockerfile.

Copy the API key (just the part that begins with `ei_`) to the line that starts `ENV API_KEY=` and also to the second string in the `CMD` command in the last line of the Dockerfile.




