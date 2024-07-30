import axios from 'axios';

const API_URL = '/api';

export const getSales = (filters) => {
    return axios.get(`${API_URL}/sales/`, { params: filters });
};

export const getSale = (id) => {
    return axios.get(`${API_URL}/sales/${id}`);
};

export const getStores = () => {
    return axios.get(`${API_URL}/stores`);
};

export const getStore = (id) => {
    return axios.get(`${API_URL}/stores/${id}`);
};

export const getCategories = () => {
    return axios.get(`${API_URL}/categories`);
};

export const getCategory = (id) => {
    return axios.get(`${API_URL}/categories/${id}`);
};

export const getVendors = () => {
    return axios.get(`${API_URL}/vendors`);
};

export const getVendor = (id) => {
    return axios.get(`${API_URL}/vendors/${id}`);
};
