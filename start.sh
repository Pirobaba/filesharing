if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/@ronak0910/MovieBot.git /MovieBot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /MovieBot
fi
cd /MovieBot
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
