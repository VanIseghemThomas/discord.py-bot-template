
# discord.py bot template
### A discord.py bot template for with easy deployment through Github Actions. You can use this template to just run a Python instance, Docker image, or Docker compose with other microservices. This is why it features a mockup API aswell, to showcase the flexibility of it.

## Registering a new bot
Go to [Discord Developer Applications Portal](https://discord.com/developers/applications) And create a new application. Then go to **Bot -> Add Bot**. Give it a name and the required permissions for your use case.
Now use **Click to Reveal Token** to get your token, you will need this in configuration. *Do not share this with anyone!* If for some reason the token got leaked, you can regenerate a new one. This means you need to this this in the configuration later on aswell, so only do this when necessary.

## Configuration
First you'll have to create a .env file. This is a file where all configuration is stored for this bot.
**If you are going to run this in a simple way locally**, use the **example.env** file and fill in the field with your discord token. And save this with the file name only being: *".env"* The script will now use this file to access the token.

**Suggested: If you are planning to take the automated deployment approach**, you will not need to put this key inside the .env file. Go to the *Automated deployment pipeline* section to set this up.

## Running in docker
I'm going straight to running in docker. First you will have to build the docker image. You can do this by going inside the directory that contains the dockerfile and running the command:

    docker build . -t <image tag>
To run the bot you can use:

    docker run --env-file <env file> <image tag>

you can add the **-d** flag to run in detached mode.

## Automated deployment pipeline
First you'll have to generate a [**Personal Access Token**](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).
Keep a copy of this, you wont be able to access it once it's generated.
You will put this key and the discord token inside the repository secrets under **Settings -> Secrets -> Actions** and create a new secret with the same key value pair. Now the tokens are accessible by Github Actions, but remain anonymous. Also other people with access to the repo can't see it, including yourself. From now on you're only able to write to these. Also add your user

![image](https://user-images.githubusercontent.com/55881698/153042695-5a218782-3468-417e-8bc2-d69e573a2fb1.png)

Now set up a self-hosted runner. Ideally this is configured as a service so that it runs permanently and launches on startup. You can add a runner by going to **Settings -> Actions -> Runners** and add a new one. Follow the instructions for your platform. For this example I did it in my WSL Debian. Make sure docker is installed on this machine when running the action runner.

![image](https://user-images.githubusercontent.com/55881698/153045303-8634d5b5-1824-4ddc-b30b-16a1c5115994.png)

When starting the runner you should see the it appear with the **idle** status. I recommend [this doc](https://docs.github.com/en/actions/hosting-your-own-runners/configuring-the-self-hosted-runner-application-as-a-service) to get it up and running as a service. If you want to just quickly run it using the run.sh script, make sure that your user has the right privileges to do this. Check out [this post](https://docs.docker.com/engine/install/linux-postinstall/) if you encounter an error due to this problem.

![image](https://user-images.githubusercontent.com/55881698/153045424-193ef313-8106-4f3f-8152-005ca40e8112.png)

Now Github Actions will use this machine to deploy the bot.
