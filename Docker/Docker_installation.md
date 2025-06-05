This reports the steps in: https://docs.docker.com/engine/install/ubuntu/

# Installing Docker engine (Ubuntu 24.04)
1) First purge conflicting packages:
`for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done`

2) Add new repository references:
```
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

3) Install docker:
   `sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin`

4) Verify installation:
` sudo docker run hello-world`

## Allow docker to be used without sudo
Run the following commands
1)  `sudo groupadd docker`
2)  `sudo usermod -aG docker $USER`

Restart the computer

# Downloading and using docker image

The precompiled image is available on Dockerhub, once the docker engine is installed run
```
docker pull cartaalberto/asesma_2025:latest
```
You can now run an interactive terminal by using the command:
```
docker run -p 8888:8888 --rm -it --shm-size=4g -e USER_ID=`id -u` -e GROUP_ID=`id -g` -v /home:/home cartaalberto/asesma_2025:latest bash
```

You might want to alias the command and put it in the .bashrc
```
alias asesma_qe="docker run -p 8888:8888 --rm -it --shm-size=4g -e USER_ID=`id -u` -e GROUP_ID=`id -g` -v /home:/home cartaalberto/asesma_2025:latest bash"
```




