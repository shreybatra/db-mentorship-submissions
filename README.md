# DB Mentorship Program

## Instructions
- Everyday, we will be sending tasks on Discord along with Task Number (Task ID).
- You need to pull the repo everyday and complete the file `tasks/task_{taskId}.py` as per the instructions given.

## First Time Setup Guide
- Clone this repo.
- Create a virtualenv - `python3.10 -m venv venv` (yes twice, it creates a folder venv inside the current directory)
- Activate the virtualenv -
  - Linux/Mac - `source venv/bin/activate`
  - Windows (command prompt) - `source venv\Scripts\activate.bat`
  - Windows (git bash) - `source venv/Scripts/activate`
- Install requirements file - `pip install -r requirements.txt`
- Ask for `.env` file on Discord or find it on your registered email.
- Paste the `.env` file in the root directory of the project.

## Daily Task Submission
- Pull the lastest changes everyday - `git pull origin main`
- Complete the task as per the instructions.
- Run the following command to submit -
```bash
python main.py --task_num {taskId} --email {registered_email}
```

Example - 
```
python main.py --task_num 3 --email abc@example.com
```

## Note
- Make sure not to make any changes in the scripts.