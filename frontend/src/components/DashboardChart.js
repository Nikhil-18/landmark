import React from 'react';
import { Bar } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

const SalesChart = ({ salesData }) => {
    const chartData = {
        labels: salesData.map(sale => sale.store.store_name),
        datasets: [
            {
                label: 'Sales Dollars',
                data: salesData.map(sale => sale.sale_dollars),
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1,
            },
            {
                label: 'Profit',
                data: salesData.map(sale => sale.sale_dollars - (sale.bottles_sold * sale.item.state_bottle_cost)),  // TODO: include this in table
                backgroundColor: 'rgba(153, 102, 255, 0.2)',
                borderColor: 'rgba(153, 102, 255, 1)',
                borderWidth: 1,
            },
        ],
    };

    const options = {
        responsive: true,
        plugins: {
            legend: {
                position: 'top',
            },
            title: {
                display: true,
                text: 'Sales and Profit by Store',
            },
        },
    };

    return <Bar data={chartData} options={options} />;
};

export default SalesChart;
