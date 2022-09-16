
# About the project

- Name: pyCliAddressBook
- Main idea of the project: creating a personal assistant with a command line interface
- Deadline: MVP - 3 days, Prod - 2 days, presentation - 1 day
- Stack of technologies used: OOP, functional programming, Pylint, GitHub, git, Trello, Agile, Debugging, Profiling


## About the Team

- [@Yurii Skiter](https://github.com/yuragoit) Team Lead, Dev
- [@Valerii Sydorenko](https://github.com/ErizoUA) PM, Dev
- [@Dmytro Levoshko](https://github.com/DmytroLievoshko) Scrum Master, Dev


## Functionality / Documentation
- save contacts with names, addresses, phone numbers, emails and birthdays to the contact book [add]
- checking the correctness of the entered phone number and email when creating or editing a record, notifying the user in case of incorrect entry (validator function)
- search for contacts from the contact book, view all contacts, find contacts by any field [search, view_all, find]
- edit and delete entries from the contact book, reset all contacts [update, delete, reset]
- display a list of contacts who have a birthday in a specified number of days from the current date [sort_birthday]
- save notes with text information [add_notes]
- searching by notes [search_notes]
- edit and delete notes, reset all notes [update_notes, delete_notes, reset_notes]
- add "tags" to the notes, keywords that describe the topic and subject of the record [add_notes]
- search and sort notes by keywords (tags) [search_notes]
- sorting files in the specified folder by category (images, documents, videos, etc.) [file_sort]
- call documentation in interactive mode [help]
- completion of the program [exit]
- The bot analyzes the entered text and tries to guess what the user wants from it and offers the nearest command for execution
- The bot can be called anywhere in the system with the assistant command (after installing the package)
- personal assistant stores information on the hard drive in the user folder and can be restarted without data loss




## Lessons Learned

- experience in planning and task setting
- experience in the development of OOP principles and functional programming
- experience of working with Trello
- experience in the position of Team lead, Scrum master, PM team
- team collaboration and work with Git
- project branching and merging skills
- conflict resolution after the merger of branches
- project presentation experience


## Optimizations in our code

Refactors, accessibility


## Installation

Install project with pip

```bash
  pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple pyCliAddressBook==1.0.22
```


## Run Locally

Clone the project

```bash
  git clone https://github.com/yuragoit/pyCliAddressBook
```

Go to the project directory

```bash
  cd pyCliAddressBook
```

Install dependencies

```bash
  pip install python-dateutil
  pip install rich
  pip install prompt-toolkit
  pip install phonenumbers
```

Start assistant from file

```bash
  py main.py
```
Then use contextual commands with appropriate prompts in the interactive mode of the terminal


## Usage after installing the package / Examples

```bash/sh/cmd
>> assistant
```
Then use contextual commands with appropriate prompts in the interactive mode of the terminal


## Screenshots

![App Screenshot](https://user-images.githubusercontent.com/101989870/190389161-f42acfc2-9a54-4604-8c9c-4b667986814a.jpg)
![table_format](https://user-images.githubusercontent.com/101989870/190399225-1605ba4d-65c3-464c-8129-ea18269a720f.png)
## License

[MIT](https://choosealicense.com/licenses/mit/)


## Used By

This project is used by the following companies:

- LLC GoIT

