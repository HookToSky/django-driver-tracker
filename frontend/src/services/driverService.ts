import axios, { AxiosRequestConfig } from 'axios';
// import jsonData from '../constants/drivers.get.json'

export const getDrivers = async () => {
    try {
        const options: AxiosRequestConfig = {
            url: '/api/markers/',
            method: 'GET',
            headers: {
                'Access-Control-Allow-Origin' : '*'
            }
        };
        const response = await axios(options);
        return response.data;
    } catch (error) {
        throw new Error(error);
    }
};
