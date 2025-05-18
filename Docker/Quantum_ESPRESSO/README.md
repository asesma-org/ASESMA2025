## Building the image
To build the image run:

`docker build  --network=host -t asesma_qe:final -f dockerfile ./`

This creates a docker image called `asesma_qe:final`

You can check that the building was successful if you run `docker images` and see the image.

You can save the image to file:

`docker save asesma_qe:final > asesma_qe.tar`

 this will be a very large file (>20 Gb)

The point of docker is that to now load the same image with everything installed in it in another machine thatuses docker, one can copy the `asesma_qe.tar` and run

`docker load < asesma_qe.tar`

## Entrypoint for running the container interactively
It is important to have the `entrypoint.sh` file together with these lines in the dockerfile 

```
RUN apt-get update &&  DEBIAN_FRONTEND=noninteractive apt-get install -y curl sudo wget git less rsync nano openssl ca-certificates

...

EXPOSE 8378

COPY entrypoint.sh /usr/local/bin/entrypoint.sh

RUN ["chmod", "+x", "/usr/local/bin/entrypoint.sh"]

# change user and group id to match host machine if options are passed accordingly
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
```


You can then use the command:
```
alias asesma_qe="docker run -p 8888:8888 --rm -it --shm-size=4g -e USER_ID=`id -u` -e GROUP_ID=`id -g` -v /home:/home asesma_qe:final bash"
```

This will be in the `.bashrc` of the workstation and will allow to use the command `asesma_qe` to enter an interactive docker container for which the `/home` folder is mounted to the same `/home` folder of the workstation

If you run now `asesma_qe`, congrats! You should now be inside the dockerfile.

