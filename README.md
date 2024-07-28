# Keybind Training

This repository serves as a training ground to become more comfortable with VSCode Keybinds.
Don't use your mouse!!
If you want to send your time in slack, run these commands:
```
sudo mkdir -p -m 775 /usr/local/bin
sudo ln -sf "$HOME/.slack/bin/slack" "/usr/local/bin/slack"
sudo curl -fsSL https://downloads.slack-edge.com/slack-cli/install.sh | bash
```
You'll also need to set the slack webhook URL as an environment variable. (Founding members should message Ben to get theirs)
If using fish, add this line to your config.fish:
```
set -gx PATH $PATH $HOME/.slack/bin
```
Then run
```
source ~/.config/fish/config.fish
```
Your time begins when you first run 
```
python run_tasks.py
```
Complete the tasks as quickly as possible! Time stops when run_tasks.py executes with no errors.