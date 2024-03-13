const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

const app = express();
const port = 3000;

// MongoDB connection
mongoose.connect('mongodb://localhost/registration_form_db', {
    useNewUrlParser: true,
    useUnifiedTopology: true
});
const db = mongoose.connection;
db.on('error', console.error.bind(console, 'MongoDB connection error:'));

// Define schema for user registration
const userSchema = new mongoose.Schema({
    username: String,
    email: String,
    password: String
});
const User = mongoose.model('User', userSchema);

// Body parser middleware
app.use(bodyParser.urlencoded({ extended: true }));

// Serve static files
app.use(express.static('public'));

// Route to handle registration form submission
app.post('/register', (req, res) => {
    const { username, email, password } = req.body;
    
    // Create a new user document
    const newUser = new User({ username, email, password });
    
    // Save the new user to the database
    newUser.save((err, savedUser) => {
        if (err) {
            console.error(err);
            res.status(500).send('Error registering user');
        } else {
            res.status(200).send('User registered successfully');
        }
    });
});

// Start server
app.listen(port, () => {
    console.log(`Registration Form app listening at http://localhost:${port}`);
});
