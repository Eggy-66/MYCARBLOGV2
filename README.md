<img width="1197" alt="Screenshot 2025-02-25 at 12 36 51" src="https://github.com/user-attachments/assets/3c5c109d-01ad-4f75-9e1a-06d58c2a3df7" />


# MyCarBlog

MyCarBlog is a Django-based web application for car enthusiasts to share and explore car-related projects and articles.

## Features

- User authentication and profile management
- Create, read, update, and delete car projects
- Responsive design with Bootstrap
- Image handling with Pillow
- Crispy forms for better form rendering

## Requirements

- Python 3.x
- Django
- Pillow
- Django Crispy Forms
- Crispy Bootstrap4

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/mycarblog.git
    cd mycarblog
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```sh
    python manage.py migrate
    ```

5. Create a superuser:

    ```sh
    python [manage.py](http://_vscodecontentref_/0) createsuperuser
    ```

6. Run the development server:

    ```sh
    python [manage.py](http://_vscodecontentref_/1) runserver
    ```

7. Open your browser and go to `http://127.0.0.1:8000/`

## Project Structure

- `blog/`: Contains the blog application
- `main/`: Contains the main application
- `media/`: Contains media files
- `mycarblog/`: Project configuration
- `requirements.txt`: List of dependencies
- `manage.py`: Django's command-line utility

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some feature'`)
5. Push to the branch (`git push origin feature-branch`)
6. Open a pull request

## License

This project is licensed under the MIT License.
