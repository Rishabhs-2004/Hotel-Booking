from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key in production

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Here you would typically save this to a database or send an email
        # For now, we'll just flash a message
        flash(f'Thank you {name}, your message has been received!', 'success')
        return redirect(url_for('index'))
    
    return render_template('contact.html', title='Contact')

@app.route('/rooms')
def rooms():
    # Sample room data - in a real application, this would come from a database
    rooms = [
        {
            'id': 1,
            'name': 'Deluxe Room',
            'description': 'Spacious room with a king-size bed and city view.',
            'price': 150,
            'image': 'room1.svg'
        },
        {
            'id': 2,
            'name': 'Executive Suite',
            'description': 'Luxury suite with separate living area and panoramic views.',
            'price': 250,
            'image': 'room2.svg'
        },
        {
            'id': 3,
            'name': 'Family Room',
            'description': 'Perfect for families with two queen beds and extra space.',
            'price': 200,
            'image': 'room1.svg'
        }
    ]
    return render_template('rooms.html', title='Our Rooms', rooms=rooms)

@app.route('/booking/<int:room_id>', methods=['GET', 'POST'])
def booking(room_id):
    # Sample room data - in a real application, this would come from a database
    rooms = {
        1: {'name': 'Deluxe Room', 'price': 150},
        2: {'name': 'Executive Suite', 'price': 250},
        3: {'name': 'Family Room', 'price': 200}
    }
    
    room = rooms.get(room_id)
    if not room:
        flash('Room not found', 'danger')
        return redirect(url_for('rooms'))
    
    if request.method == 'POST':
        check_in = request.form.get('check_in')
        check_out = request.form.get('check_out')
        guests = request.form.get('guests')
        name = request.form.get('name')
        email = request.form.get('email')
        
        # Here you would typically save the booking to a database
        # For now, we'll just flash a message
        flash(f'Thank you {name}, your booking for {room["name"]} has been confirmed!', 'success')
        return redirect(url_for('index'))
    
    return render_template('booking.html', title='Book a Room', room=room, room_id=room_id)

if __name__ == '__main__':
    app.run(debug=True)