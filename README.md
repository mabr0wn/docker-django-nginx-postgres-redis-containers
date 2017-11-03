# Django-Docker
Build a simple web app using Django with Docker
# 1. Install Docker for Mac
The first step is to install the [Docker for Mac](https://www.docker.com/docker-mac) or [Docker for Windows](https://www.docker.com/docker-windows) if that's your cup of tea.

# 2. Get familiar with Docker
Open a shell (using an application like Terminal or iTerm), and run the following command:

```
docker run -it ubuntu:16.04 bash
```

Let's take a look at what this command does.

The **docker run** command lets you start a container from an image. In this case, you are creating a container from the **ubuntu:16.04** image. This is the **ubuntu** image with the **16.04** tag.

Each Docker container should run a single process. So the **docker run** command lets you specify a single command to run inside of the container. In our case, we are going to run a **bash** shell. So we've specified the command to run as bash. Since we are running a bash shell we are going to want to allocate a pseudo-TTY and keep STDIN open. This is why we've added the options **-it** to the run command.

After running this command you should see something like this:

```
root@69129699ac86:/#
```

This is the bash shell running inside of the container you just created from the ubuntu image. You can run **ps** to see which processes are running in this container.

```
root@69129699ac86:/# ps
  PID TTY          TIME CMD
    1 ?        00:00:00 bash
   18 ?        00:00:00 ps
```
