#!/bin/bash

# A little script that switches you to the best available
# lab machine on login
# Put this in your /priv folder

function start_agent {
    echo "Initialising new SSH agent..."
    /usr/bin/ssh-agent | sed 's/^echo/#echo/' > "${SSH_ENV}"
    echo succeeded
    chmod 600 "${SSH_ENV}"
    . "${SSH_ENV}" > /dev/null
    /usr/bin/ssh-add;
}

if [ $HOSTNAME = "lab0z" ]; then

SSH_ENV="$HOME/.ssh/environment"

	if [ -f "${SSH_ENV}" ]; then
	    . "${SSH_ENV}" > /dev/null
	    #ps ${SSH_AGENT_PID} doesn't work under cywgin
	    ps -ef | grep ${SSH_AGENT_PID} | grep ssh-agent$ > /dev/null || {
		start_agent;
	    }
	else
	    start_agent;
	fi

	if [ ! -f $HOME/.ssh/autoSwitchKey ]; then

		printf "\n\nNo autoSwitch OpenSSH key found. one will be generated\n"
		echo "Do not leave the key password blank!"
		echo "The key will be held by the ssh-agent when you log in"
		echo "You will be asked to enter your key password to add it to the agent"
		read -p "Press enter to continue"

		ssh-keygen -t rsa -C "$HOSTNAME" -f "$HOME/.ssh/autoSwitchKey"
		echo "Enter your password to add the new key to ssh-agent"
		ssh-add "$HOME/.ssh/autoSwitchKey"

		printf "\nOpenSSH key will be added to your authorized keys\n"
		echo "This allows you to ssh between lab machines without entering your password"
		printf "\nThis script will never see your password\n"
		read -p "Press enter to continue and enter your password when prompted"

		ssh-copy-id -i "$HOME/.ssh/autoSwitchKey" "$HOSTNAME"

		echo "----------------------------------------------"	
		printf "\nSetup Done!\n"

		printf "\nRun this script again to get ssh'd to the best available lab machine\n"
		printf "\nTo run this script everytime you log in, add this line to your .profile file\n"
		printf "\n\tbash \$HOME/priv/$FILE\n\n"
	else
		machine=$(head -c 5 /tmp/labmachines)
		printf "\nSwitching to lab machine $machine\n"
		ssh "$machine"
	fi
fi

