// src/server.js
const express = require('express');
const mongoose = require('mongoose');
const Transaction = require('./models/Transaction'); // Import Transaction model
const app = express();
const path = require('path'); // Add this line to import the path module

// Connect to MongoDB
mongoose.connect('mongodb://localhost/money_tracker', {
  useNewUrlParser: true,
  useUnifiedTopology: true
})
  .then(() => console.log('Connected to MongoDB'))
  .catch(err => console.error('Could not connect to MongoDB', err));

// Middleware
app.use(express.json());

// Routes
// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

// Define a route to handle the homepage
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Define a route for the root URL
app.get('/', (req, res) => {
    res.send('Welcome to the Money Tracker App');
});

// Create a transaction
app.post('/transactions', async (req, res) => {
  try {
    const transaction = new Transaction(req.body);
    await transaction.save();
    res.send(transaction);
  } catch (err) {
    res.status(400).send(err.message);
  }
});

// Get all transactions
app.get('/transactions', async (req, res) => {
  try {
    const transactions = await Transaction.find();
    res.send(transactions);
  } catch (err) {
    res.status(500).send('Internal Server Error');
  }
});

// Get transaction by ID
app.get('/transactions/:id', async (req, res) => {
  try {
    const transaction = await Transaction.findById(req.params.id);
    if (!transaction) return res.status(404).send('Transaction not found');
    res.send(transaction);
  } catch (err) {
    res.status(500).send('Internal Server Error');
  }
});

// Update transaction
app.put('/transactions/:id', async (req, res) => {
  try {
    const transaction = await Transaction.findByIdAndUpdate(req.params.id, req.body, { new: true });
    if (!transaction) return res.status(404).send('Transaction not found');
    res.send(transaction);
  } catch (err) {
    res.status(400).send(err.message);
  }
});

// Delete transaction
app.delete('/transactions/:id', async (req, res) => {
  try {
    const transaction = await Transaction.findByIdAndDelete(req.params.id);
    if (!transaction) return res.status(404).send('Transaction not found');
    res.send(transaction);
  } catch (err) {
    res.status(500).send('Internal Server Error');
  }
});

// Start the server
const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`Server is running on port ${port}`));
