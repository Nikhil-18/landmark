import React, { useState, useEffect } from "react";
import { getSales } from "../api/api";
import Filters from "./Filters";
import DashboardChart from "./DashboardChart";

const Dashboard = () => {
  const [salesData, setSalesData] = useState([]);
  const [filters, setFilters] = useState({});

  useEffect(() => {
    fetchSales(filters);
  }, [filters]);

  const fetchSales = (filters) => {
    getSales(filters)
      .then((res) => setSalesData(res.data))
      .catch((err) => console.error(err));
  };

  console.log(salesData);

  return (
    <div>
      <Filters onFilterChange={setFilters} />
      <h2>Sales Dashboard</h2>
      <table>
        <thead>
          <tr>
            <th>Store Name</th>
            <th>Category</th>
            <th>Vendor</th>
            <th>Sales Dollars</th>
            <th>Bottles Sold</th>
          </tr>
        </thead>
        <tbody>
          {salesData.map((sale) => (
            <tr key={sale.id}>
              <td>{sale.store.store_name}</td>
              <td>{sale.category.category_name}</td>
              <td>{sale.vendor.vendor_name}</td>
              <td>{sale.sale_dollars}</td>
              <td>{sale.bottles_sold}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <DashboardChart salesData={salesData} />
    </div>
  );
};

export default Dashboard;
