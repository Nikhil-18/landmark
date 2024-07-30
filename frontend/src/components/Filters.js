import React, { useState, useEffect } from 'react';
import Select from 'react-select';
import { getCategories, getStores, getVendors } from '../api/api';

const Filters = ({ onFilterChange }) => {
    const [stores, setStores] = useState([]);
    const [categories, setCategories] = useState([]);
    const [vendors, setVendors] = useState([]);
    const [selectedFilters, setSelectedFilters] = useState({});

    useEffect(() => {
        getStores().then(res => setStores(res.data));
        getCategories().then(res => setCategories(res.data));
        getVendors().then(res => setVendors(res.data));
    }, []);

    const mapToQueryParams = (filters) => {
        const query = {};
        if (filters.store_name) query['store__store_name'] = filters.store_name;
        if (filters.category_name) query['category__category_name'] = filters.category_name;
        if (filters.vendor_name) query['vendor__vendor_name'] = filters.vendor_name;
        return query;
    };

    const handleChange = (selectedOption, { name }) => {
        const filters = { ...selectedFilters, [name]: selectedOption.value };
        const queryFilters = mapToQueryParams(filters);
        setSelectedFilters(filters);
        onFilterChange(queryFilters);
    };

    return (
        <div>
            <Select
                name="store_name"
                options={stores.map(store => ({ value: store.store_name, label: store.store_name }))}
                onChange={handleChange}
                placeholder="Select Store"
            />
            <Select
                name="category_name"
                options={categories.map(category => ({ value: category.category_name, label: category.category_name }))}
                onChange={handleChange}
                placeholder="Select Category"
            />
            <Select
                name="vendor_name"
                options={vendors.map(vendor => ({ value: vendor.vendor_name, label: vendor.vendor_name }))}
                onChange={handleChange}
                placeholder="Select Vendor"
            />
        </div>
    );
};

export default Filters;
