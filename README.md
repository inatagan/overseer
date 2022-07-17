# overseer
Overseer as the name implies is a reddit bot to help display status information about a submitter in every submission in a given subreddit.

### How to install
Clone this repository to it's destination, your home dir is preferable.

On the root directory of this project run the command to install all the necessary dependencies:

    pip install -r requirements.txt

Use the env_template to set all your info required for the `.env` file.

### [Optional] Create a background service to run the main file with systemd.

    sudo nano /lib/systemd/system/overseer.service

On the `extra` directory there is already a template file for the service, if you don't have any custom changes you can just copy the `.service` file to `/lib/systemd/system/` with the command:

    sudo cp ~/overseer/overseer.service /lib/systemd/system/overseer.service

Change the permission of the file to 644:

    sudo chmod 644 /lib/systemd/system/overseer.service

Reload the system manager configuration by using the following command:

    sudo systemctl daemon-reload

Start the service using the following command:

    sudo systemctl start overseer.service

Stop the service using the following command:

    sudo systemctl stop overseer.service

You can enable the service to start at boot as below:

    sudo systemctl enable overseer.service