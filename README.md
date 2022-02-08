
# discord.py bot template
### A discord.py bot template for with easy deployment through Github Actions. You can use this template to just run a Python instance, Docker image, or Docker compose with other microservices. This is why it features a mockup API aswell, to showcase the flexibility of it.

## Registering a new bot
Go to [Discord Developer Applications Portal](https://discord.com/developers/applications) And create a new application. Then go to **Bot -> Add Bot**. Give it a name and the required permissions for your use case.
Now use **Click to Reveal Token** to get your token, you will need this in configuration. *Do not share this with anyone!* If for some reason the token got leaked, you can regenerate a new one. This means you need to this this in the configuration later on aswell, so only do this when necessary.

## Configuration
First you'll have to create a .env file. This is a file where all configuration is stored for this bot.
**If you are going to run this in a simple way locally**, use the **example.env** file and fill in the field with your discord token. And save this with the file name only being: *".env"* The script will now use this file to access the token.

**Suggested: If you are planning to take the automated deployment approach**, you will put this key inside the repository secrets under **Settings -> Secrets -> Actions** and create a new secret with the same key value pair. Now the token is accessible by Github Actions, but remains anonymous. Also other people with access to the repo can't see it, including yourself.

![image](https://user-images.githubusercontent.com/55881698/153018959-99ff61a5-73cb-48ba-8486-086770a27a82.png)

## Running in docker
I'm going straight to running in docker. First you will have to build the docker image. You can do this by going inside the directory that contains the dockerfile and running the command:

    docker build . -t <image tag>
To run the bot you can use:

    docker run --env-file <env file> <image tag>

you can add the **-d** flag to run in detached mode.

## Automated deployment pipeline

Instructions in progress...
