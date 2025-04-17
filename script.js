fetch('data/sales_history.json')
  .then(res => res.json())
  .then(data => {
    const labels = data.map(entry => entry.date);
    const goals = data.map(entry => entry.goal);
    const actuals = data.map(entry => entry.actual);

    const ctx = document.getElementById('salesChart').getContext('2d');
    new Chart(ctx, {
      type: 'line',
      data: {
        labels: labels,
        datasets: [
          {
            label: 'Goal',
            data: goals,
            borderColor: 'blue',
            borderWidth: 2,
            fill: false
          },
          {
            label: 'Actual Sales',
            data: actuals,
            borderColor: 'green',
            borderWidth: 2,
            fill: false
          }
        ]
      },
      options: {
        responsive: true,
        plugins: {
          title: {
            display: true,
            text: 'Daily Sales vs. Goal'
          }
        }
      }
    });
  });
