# Docker Rollbar Agent
This is a container for running the docker rollbar agent. It reads logs written to /log, so you can mount shared volumes to this directory allowing your other applications to post rollbar logs that this agent can pick up and read.

## Usage
```
docker run --name rollbar_agent -d -v /path/on/local:/logs -e "ACCESS_TOKEN=YOUR_ROLLBAR_TOKEN" -e "ENVIRONMENT=YOUR_ROLLBAR_ENVIRONMENT" siosphere/rollbar-agent
```

You can optionally overwrite the rollbar-agent.conf by extending this image, or mounting the file as a volume where supported.