// public/app.js
const transactionForm = document.getElementById('transaction-form');

transactionForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const formData = new FormData(transactionForm);
    const type = formData.get('type');
    const amount = parseFloat(formData.get('amount'));
    const description = formData.get('description');

    try {
        const response = await fetch('/transactions', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                type,
                amount,
                description
            })
        });
        document.getElementById('check-balance-btn').addEventListener('click', () => {
            fetch('/balance')
                .then(response => response.json())
                .then(data => {
                    alert(`Your current balance is: $${data.balance.toFixed(2)}`);
                })
                .catch(error => {
                    console.error('Error fetching balance:', error);
                });
        });
        if (!response.ok) {
            throw new Error('Failed to add transaction');
        }

        const transaction = await response.json();
        console.log('Transaction added:', transaction);

        // Clear form fields
        transactionForm.reset();
    } catch (error) {
        console.error('Error adding transaction:', error.message);
    }
});
