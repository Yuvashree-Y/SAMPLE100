const express = require('express');
const app = express();

app.use(express.json());

let products = [
  { id: 1, name: 'Laptop', price: 75000 },
  { id: 2, name: 'Mouse', price: 500 },
  { id: 3, name: 'Keyboard', price: 1200 }
];

let nextId = 4;

// FIXED: changed > to =>
app.get('/products', (req, res) => {
  res.json(products);
});

app.get('/products/:id', (req, res) => {
  const product = products.find(p => p.id === parseInt(req.params.id));
  if (!product) return res.status(404).json({ error: 'Product not found' });
  res.json(product);
});

app.post('/products', (req, res) => {
  if (!req.body.name || !req.body.price) {
    return res.status(400).json({ error: 'Name and price required' });
  }
  const product = {
    id: nextId++,
    name: req.body.name,
    price: req.body.price
  };
  products.push(product);
  res.status(201).json(product);
});

app.listen(3000, () => {
  console.log('Server running on http://localhost:3000');
});