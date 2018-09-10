```
# SET EMAIL ENVIRONMENT VARIABLE
vim ~/.bashrc # or ~/.bash_profile
export WOKE_EMAIL=you@gmail.com

# CLONE REPO, TRY IT ONCE
git clone git@github.com:dancrew32/woke.git
cd woke 
make venv deps run

# INSTALL CRONTAB
crontab -e
6 30 * * * /home/ubuntu/woke/app.py
```
