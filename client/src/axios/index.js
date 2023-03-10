import axios from "axios"

const API_URL = "http://127.0.0.1:8000/api/v1"

export const axiosInstance = axios.create({
    baseURL: API_URL,
    withCredentials: true,
    headers: {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
})

export const axiosPrivateInstance = axios.create({
    baseURL: API_URL,
    withCredentials: true,
    headers: {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
})