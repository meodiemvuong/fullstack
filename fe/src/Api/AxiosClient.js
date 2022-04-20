import axios from 'axios';

const axiosClient = axios.create({
    baseURL: 'http://127.0.0.1:8000',
    headers: {
        'Content-Type': 'application/json',
        'Accept' : 'application/json'
    },
});

axiosClient.interceptors.request.use(async (config) => {
    let token = localStorage.getItem('Token')
    if(token) {
        config.headers.Authorization = `Token ${token}`;
    }
    return config;
})
axiosClient.interceptors.response.use((response) => {
    if (response && response.data) {
        return response;
    }
    return response;
}, (error) => {
    throw error;
});

export default axiosClient;