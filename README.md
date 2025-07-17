# Hotel Booking Web Application

A modern hotel booking web application built with Flask, featuring a responsive design, room listings, booking functionality, and real hotel images.

## Features

- Modern, responsive design using Bootstrap and custom CSS
- Dynamic hotel room listings with images and pricing
- Room booking system with form validation
- Multiple page routes (Home, Rooms, About, Contact, Booking)
- Interactive elements including carousels and testimonials
- Contact form with validation
- Flash messages for user feedback
- Real hotel and room images from Pixabay

## Installation

1. Clone this repository or download the files

2. Create a virtual environment (recommended)

```bash
python -m venv venv
```

3. Activate the virtual environment

- On Windows:
```bash
venv\Scripts\activate
```

- On macOS/Linux:
```bash
source venv/bin/activate
```

4. Install the required packages

```bash
pip install -r requirements.txt
```

## Running the Application

1. With the virtual environment activated, run:

```bash
python app.py
```

2. Open your web browser and navigate to:

```
http://127.0.0.1:5000/
```

## Project Structure

```
flask_project/
├── app.py                  # Main application file with routes
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
├── static/                 # Static files
│   ├── css/
│   │   └── style.css       # Custom CSS for hotel styling
│   ├── images/             # Hotel and room images
│   │   └── README.md       # Image credits and sources
│   └── js/
│       └── script.js       # Custom JavaScript
└── templates/              # HTML templates
    ├── base.html           # Base template with layout
    ├── index.html          # Home page with hotel showcase
    ├── rooms.html          # Room listings page
    ├── booking.html        # Room booking form
    ├── about.html          # About page with hotel information
    └── contact.html        # Contact page with form
```

## Key Features Explained

### Home Page
- Hero carousel with featured hotel images
- Quick booking search form
- Featured rooms section
- Hotel amenities and features
- Customer testimonials

### Rooms Page
- Detailed room listings with images
- Room descriptions and pricing
- "Book Now" buttons linking to the booking form

### Booking System
- Room-specific booking forms
- Date selection for check-in and check-out
- Guest information collection
- Booking confirmation with flash messages

### About Page
- Hotel story and mission
- Key differentiators and unique selling points
- Sustainability commitment
- Customer testimonials

## Customization

You can customize this application by:

- Adding more room types in the `rooms` route in `app.py`
- Updating room images in the templates
- Modifying the booking form in `booking.html`
- Adding authentication for user accounts
- Connecting to a database for persistent storage

## Future Enhancements

- User authentication and accounts
- Payment processing integration
- Room availability calendar
- Admin dashboard for managing bookings
- Email confirmation system
- Reviews and ratings system

## Production Deployment

Before deploying to production:

1. Change the secret key in `app.py` to a secure random string
2. Set `debug=False` in the `app.run()` call
3. Consider using a production WSGI server like Gunicorn or uWSGI
4. Implement a database for storing room and booking information

## License

This project is open source and available under the [MIT License](LICENSE).

## Credits

All hotel and room images are sourced from Pixabay and are free for commercial use.