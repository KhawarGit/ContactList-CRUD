# ContactList-CRUD

ContactsList-CRUD is a web application created using the Django web framework, HTML, and CSS. It allows users to manage their contacts by providing CRUD (Create, Read, Update, Delete) functionality. The application displays contacts from the database, including fields such as firstName, lastName, Email, and Comment (colleague, friend, brother, etc.). Users can edit or delete each contact and add new contacts through a user-friendly interface.
(<strong>Author:</strong> Khawar Khan)
## Features

- View a list of contacts with details.
- Edit existing contacts with updated information.
- Delete unwanted contacts from the list.
- Add new contacts with a simple form.

## Prerequisites

Before running this project, make sure you have the following prerequisites installed on your system:

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/) (install using `pip install Django`)
- [Git](https://git-scm.com/)

## Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/KhawarGit/ContactList-CRUD.git
2. **Navigate to the Project Directory:**
   ```bash
   cd ContactList-CRUD/contactsProject
3. **Apply Migrations:**
   ```bash
   python manage.py migrate

4. **Run the Server:**
   ```bash
   python manage.py runserver
5. **Open the Web Browser and visit:**
   ```plaintext
   http://localhost:8000/display-contacts
## Usage
* View the list of contacts on the home page.
* Use the `Add New Contact` button to create a new contact with the provided form.
* Click `Edit` to open the edit form for the respective contact.
* Click `Delete` to delete a contact.
<hr>
Enjoy managing your contacts with ContactList-CRUD!

## Author
Khawar Khan
